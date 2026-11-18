import csv, json, os, re
from datetime import date
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = str(Path(__file__).resolve().parents[2])
OUT = os.path.join(ROOT, 'outputs', 'issue-5-expert-course')
BUILD = os.path.join(ROOT, '.build', 'expert-course')
DATA = json.load(open(os.path.join(BUILD, 'course_modules.json'), encoding='utf-8'))
DISCLAIMER = 'BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU.'
NAVY='102B3F'; TEAL='087E8B'; PALE='DDF3EE'; AMBER='FFF2D8'; RED='FCE8E6'; GREY='536777'; WHITE='FFFFFF'

def shade(cell, color):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),color); tcPr.append(shd)
def set_cell_text(cell, text, bold=False, color='172B3A', size=9):
    cell.text=''; p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(2)
    r=p.add_run(str(text)); r.bold=bold; r.font.name='Aptos'; r.font.size=Pt(size); r.font.color.rgb=RGBColor.from_string(color)
    cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
def set_repeat_table_header(row):
    trPr=row._tr.get_or_add_trPr(); el=OxmlElement('w:tblHeader'); el.set(qn('w:val'),'true'); trPr.append(el)
def page_field(p):
    p.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    r=p.add_run('CTIC Vietnam · CBAM Expert 12h · DRAFT  |  '); r.font.size=Pt(8); r.font.color.rgb=RGBColor.from_string(GREY)
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); p._p.append(fld)
def base_doc(title, subtitle):
    d=Document(); sec=d.sections[0]; sec.top_margin=Inches(.62); sec.bottom_margin=Inches(.62); sec.left_margin=Inches(.72); sec.right_margin=Inches(.72)
    styles=d.styles
    styles['Normal'].font.name='Aptos'; styles['Normal'].font.size=Pt(9.3); styles['Normal'].font.color.rgb=RGBColor.from_string('172B3A')
    styles['Normal'].paragraph_format.space_after=Pt(5)
    for sty,size,col in [('Title',28,NAVY),('Heading 1',18,NAVY),('Heading 2',12,TEAL),('Heading 3',10,NAVY)]:
        styles[sty].font.name='Aptos Display' if sty=='Title' else 'Aptos'; styles[sty].font.size=Pt(size); styles[sty].font.bold=True; styles[sty].font.color.rgb=RGBColor.from_string(col)
    h=sec.header.paragraphs[0]; h.text='CTIC VIETNAM  /  CHƯƠNG TRÌNH ĐÀO TẠO CBAM'; h.style='Caption'; h.runs[0].font.color.rgb=RGBColor.from_string(TEAL); h.runs[0].font.bold=True
    page_field(sec.footer.paragraphs[0])
    p=d.add_paragraph(); p.paragraph_format.space_before=Pt(12); p.alignment=WD_ALIGN_PARAGRAPH.LEFT
    p.style='Title'; p.add_run(title)
    p=d.add_paragraph(subtitle); p.style='Subtitle'; p.runs[0].font.color.rgb=RGBColor.from_string(GREY)
    p=d.add_paragraph(DISCLAIMER); p.paragraph_format.space_after=Pt(10)
    for r in p.runs: r.font.bold=True; r.font.size=Pt(8.5); r.font.color.rgb=RGBColor.from_string('A53832')
    return d
def add_bullet(d, text, style='List Bullet'):
    p=d.add_paragraph(style=style); p.paragraph_format.space_after=Pt(2); p.add_run(str(text)); return p
def add_label(d,label,text):
    p=d.add_paragraph(); p.paragraph_format.space_after=Pt(4)
    r=p.add_run(label+'  '); r.bold=True; r.font.color.rgb=RGBColor.from_string(TEAL)
    p.add_run(str(text)); return p
def add_meta(d, rows):
    t=d.add_table(rows=0, cols=2); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Light Shading Accent 1'
    for a,b in rows:
        cells=t.add_row().cells; set_cell_text(cells[0],a,True,TEAL,8); set_cell_text(cells[1],b,False,'172B3A',8)
    return t
def legal_cite_line(c):
    src=c.get('source',{}); return f"{src.get('id','SOURCE-ID-MISSING')} · {src.get('title','')} · {c.get('provision','')} · {src.get('url','')} · {c.get('status','NEEDS_LEGAL_REVIEW')}"

# Per-module 1:1 instructor scripts
all_rows=[]
for m in DATA:
    doc=base_doc(f"{m['code']} · {m['name']}",f"Kịch bản giảng viên theo từng slide · {m['slideCount']} slide · {m['duration']} phút · DRAFT cho CTIC hiệu đính")
    doc.add_heading('Mục tiêu module',1)
    for obj in m['objectives']: add_bullet(doc,obj)
    add_meta(doc,[('Thời lượng',f"{m['duration']} phút ({m['duration']/60:g} giờ)"),('Phạm vi',f"{m['slideCount']} slide; thời lượng từng slide được ghi bên dưới"),('Cách sử dụng','Mở PowerPoint ở chế độ presenter; dùng câu hỏi và đáp án trong script để điều phối thảo luận.'),('Tình trạng pháp lý','Nội dung tham khảo; mọi điểm còn mở được đánh dấu NEEDS_LEGAL_REVIEW; không phải legal sign-off.')])
    doc.add_page_break()
    for i,s in enumerate(m['slides']):
        doc.add_heading(f"SLIDE {i+1:02d} · {s['title']}",1)
        doc.add_paragraph(f"Thời lượng: {s['duration']} phút  |  Mục tiêu: {m['objectives'][i%len(m['objectives'])]}")
        # A Vietnamese facilitation guide with the complete source narrative retained beneath it.
        add_label(doc,'Cách dẫn giảng bằng tiếng Việt',f"Mở đầu bằng chủ đề “{s['title']}”. Nối nội dung với hồ sơ vận hành và yêu cầu truy xuất. Yêu cầu học viên chỉ ra bằng chứng, đơn vị, kỳ báo cáo và người chịu trách nhiệm trước khi chấp nhận một con số.")
        add_label(doc,'Nội dung chuyên môn / lời giảng đầy đủ',s.get('explain',''))
        if s.get('bullets'):
            p=doc.add_paragraph(); r=p.add_run('Điểm cần nhấn mạnh'); r.bold=True; r.font.color.rgb=RGBColor.from_string(TEAL)
            for b in s['bullets']: add_bullet(doc,b)
        add_label(doc,'Ví dụ hoặc thao tác',s.get('explain',''))
        add_label(doc,'Câu hỏi cho lớp',s.get('prompt',''))
        add_label(doc,'Đáp án / hướng dẫn giảng viên',s.get('answer',''))
        add_label(doc,'Lỗi cần tránh',s.get('pitfall','Không biến dữ liệu tổng hợp thành số liệu thực tế hoặc kết luận pháp lý.'))
        nxt=m['slides'][i+1]['title'] if i+1<len(m['slides']) else 'Kết thúc module và chuyển sang phần kế tiếp.'
        add_label(doc,'Câu chuyển tiếp',f"Từ nội dung vừa thảo luận, chuyển sang “{nxt}”.")
        doc.add_heading('Nguồn và truy xuất điều khoản',2)
        for c in s.get('citations',[]):
            p=doc.add_paragraph(style='List Bullet'); p.paragraph_format.space_after=Pt(2); p.add_run(legal_cite_line(c))
            all_rows.append({'module':m['code'],'slide':i+1,'claim_title':s['title'],'provision':c.get('provision',''),'source_id':c.get('source',{}).get('id',''),'source_title':c.get('source',{}).get('title',''),'url':c.get('source',{}).get('url',''),'status':c.get('status','NEEDS_LEGAL_REVIEW')})
        if not s.get('citations'):
            add_label(doc,'Tình trạng nguồn','NEEDS_LEGAL_REVIEW — slide chưa có source citation. Không dùng làm claim pháp lý trước khi CTIC bổ sung nguồn.')
        if i+1<len(m['slides']): doc.add_page_break()
    suffix={'EXP-02':'Steel','EXP-03':'Aluminium','EXP-04':'Cement_Other_Sectors','EXP-05':'Monitoring_MRV','EXP-06':'OER_SEE_SEFA_Benchmark','EXP-07':'Verification_Accreditation'}[m['code']]
    file=os.path.join(OUT,f"CTIC_{m['code'].replace('-','')}_{suffix}_Lecture_Script_VI_DRAFT.docx")
    doc.save(file); m['script_docx']=os.path.basename(file)

# Student handbook and delivery schedule
hand=base_doc('SỔ TAY HỌC VIÊN · CBAM CHUYÊN GIA 12 GIỜ','Bản dùng trong lớp · dành cho operator, sustainability, finance, customs và assurance teams')
hand.add_heading('Khóa học giúp học viên làm được gì?',1)
for line in ['Đọc chuỗi nghĩa vụ CBAM theo đúng vai trò và kỳ áp dụng.','Vẽ process boundary, truy source streams và kiểm soát dữ liệu phát thải.','Thực hành thép, nhôm, xi măng; nối SEE với precursor, SEFA và hồ sơ verifier.','Nhận biết phần nào là luật hiện hành, hướng dẫn, giả định đào tạo hoặc đề xuất chưa thành luật.']:
    add_bullet(hand,line)
hand.add_heading('Cách dùng bộ tài liệu',1)
add_bullet(hand,'Mở workbook và chỉ sửa ô được đánh dấu input; mọi dữ liệu case là tổng hợp.')
add_bullet(hand,'Đọc nguyên ngữ tiếng Anh và phiên bản văn bản trước khi dùng một claim pháp lý.')
add_bullet(hand,'Ghi NEEDS_LEGAL_REVIEW cho phân loại CN, boundary, indirect treatment, benchmark hoặc Registry field chưa xác nhận.')
add_bullet(hand,'Không đưa dữ liệu cơ sở/nhà cung cấp hoặc chứng từ thẩm tra vào kho public.')
hand.add_heading('Lộ trình theo module',1)
t=hand.add_table(rows=1,cols=3); t.style='Light Shading Accent 1'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
for c,txt in zip(t.rows[0].cells,['Module','Phút','Đầu ra học tập']): set_cell_text(c,txt,True,WHITE,8); shade(c,NAVY)
for m in DATA:
    cells=t.add_row().cells; set_cell_text(cells[0],f"{m['code']} · {m['name']}"); set_cell_text(cells[1],m['duration']); set_cell_text(cells[2],'; '.join(m['objectives']),False,'172B3A',8)
set_repeat_table_header(t.rows[0])
hand.add_heading('Ba nguyên tắc cần giữ trong mọi bài tập',1)
for line in ['Actual, default và verified là ba thuộc tính khác nhau; lưu riêng nguồn và trạng thái.','SEE và SEFA/free-allocation adjustment là hai đại lượng khác nhau; không áp benchmark thành tỷ lệ miễn trừ của actual SEE.','Một phép tính đúng không chứng minh dữ liệu đầu vào đúng hoặc kết luận đã được thẩm tra.']:
    add_bullet(hand,line)
hand.add_heading('Danh sách chuẩn bị cho hồ sơ operator',1)
for line in ['CN / product specification / origin / period / production route.','Installation and process flow; product groups; functional unit; output records.','Meter IDs, fuel/electricity data, sampling/lab results, calibration and source stream register.','Precursor identity, supplier installation, period, actual/default status, quantity received/consumed and stock reconciliation.','Calculation workpapers, controls, review approvals, change log, exception register and evidence index.']:
    add_bullet(hand,line)
hand.add_heading('Checklist verifier',1)
for line in ['Confirm accreditation and activity group match the engagement scope.','Understand report criteria and installation/process boundary before sampling.','Tie sample values to source records and reperform formulas.','Assess qualitative and quantitative issues; Article 5(1) 5% is not a blanket tolerance or automatic pass.','Record finding, criterion, evidence, cause, effect, correction and retest.','Keep the independent reviewer separate from verification fieldwork. For 2026–27, any verifier acting as carbon-price independent person must use the conditional Article 11 route and satisfy its separate requirements; carbon-price-report certification is not SEE verification.']:
    add_bullet(hand,line)
hand.add_heading('Câu hỏi còn chờ CTIC xác nhận',1)
for line in ['Regulation 2025/2547: Equations 12–15 are in Annex II B.3.2 in the inspected English OJ; Annex I steel cross-references differ.','Whether/how 2026/1412 affects future CBAM benchmarks: no automatic substitution for 2025/2620.','Whether a binding CBAM benchmark update applies from 2027.','Regulation 2026/2498 Articles 10–11: confirm accreditation/competence, independence safeguards, temporary verifier opt-in, Registry role assignment and reporting-period implementation with CTIC; keep carbon-price-report certification separate from embedded-emissions verification. Article 32 dates: OJ 16 Nov 2026; force 19 Nov; applies from 1 Jan 2026.','Current Registry screens/templates and reporting fields; do not treat CTIC workbook as official form.','Product-specific CN, precursor and indirect-emissions decisions for live cases.']:
    add_bullet(hand,line)
hand_path=os.path.join(OUT,'CTIC_CBAM_Expert_Student_Handbook_VI_DRAFT.docx'); hand.save(hand_path)

# Two-day timetable: breaks are outside the 360 minutes of teaching each day.
schedule=[
 ['Ngày 1','09:00','10:30','EXP-01','Nền tảng CBAM đã bàn giao','90'],
 ['Ngày 1','10:30','10:45','NGHỈ','Tea break','0'],
 ['Ngày 1','10:45','12:45','EXP-02','Sắt thép','120'],
 ['Ngày 1','12:45','13:45','NGHỈ','Nghỉ trưa','0'],
 ['Ngày 1','13:45','15:45','EXP-03','Nhôm','120'],
 ['Ngày 1','15:45','16:00','NGHỈ','Tea break','0'],
 ['Ngày 1','16:00','16:30','EXP-04','Xi măng · phần 1 (slides 1–6)','30'],
 ['Ngày 2','09:00','10:00','EXP-04','Xi măng · phần 2 (60 phút còn lại)','60'],
 ['Ngày 2','10:00','10:15','NGHỈ','Tea break','0'],
 ['Ngày 2','10:15','12:15','EXP-05','Monitoring Plan và MRV','120'],
 ['Ngày 2','12:15','13:15','NGHỈ','Nghỉ trưa','0'],
 ['Ngày 2','13:15','14:45','EXP-06','OER, SEE, SEFA và benchmark','90'],
 ['Ngày 2','14:45','15:00','NGHỈ','Tea break','0'],
 ['Ngày 2','15:00','16:30','EXP-07','Thẩm tra và accreditation','90'],
]
assert sum(int(r[5]) for r in schedule if r[0]=='Ngày 1')==360
assert sum(int(r[5]) for r in schedule if r[0]=='Ngày 2')==360
sch=base_doc('LỊCH GIẢNG DẠY · 2 NGÀY / 12 GIỜ','360 phút nội dung mỗi ngày; nghỉ giải lao và nghỉ trưa không tính vào 12 giờ giảng')
t=sch.add_table(rows=1,cols=6); t.style='Light Shading Accent 1'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
for c,x in zip(t.rows[0].cells,['Ngày','Bắt đầu','Kết thúc','Module','Nội dung','Phút đào tạo']): set_cell_text(c,x,True,WHITE,8);shade(c,NAVY)
for r in schedule:
    cells=t.add_row().cells
    for c,x in zip(cells,r):set_cell_text(c,x,False,'172B3A',8)
    if r[3]=='NGHỈ':
        for c in cells:shade(c,'E9EEF1')
set_repeat_table_header(t.rows[0])
add_label(sch,'Tổng ngày 1','360 phút đào tạo = EXP-01 90 + EXP-02 120 + EXP-03 120 + EXP-04 phần đầu 30.')
add_label(sch,'Tổng ngày 2','360 phút đào tạo = EXP-04 phần còn lại 60 + EXP-05 120 + EXP-06 90 + EXP-07 90.')
sch.save(os.path.join(OUT,'CTIC_CBAM_Expert_Two_Day_Schedule_VI_DRAFT.docx'))

# Assessment with a separate instructor key.
questions=[
('Một tên thương mại thép “steel bar” có đủ để chốt mã CN không?',['Có, nếu supplier ghi trên invoice','Không; phải đối chiếu thông số hàng và CN hiện hành','Có, nếu route EAF','Chỉ cần website supplier'],'B'),
('Trong mass balance carbon, dòng outflow được đánh dấu thế nào theo ví dụ khóa học?',['Dương','Âm','Luôn bằng 0','Lấy trị tuyệt đối'],'B'),
('Eq.12–15 trong Regulation 2025/2547 bản OJ EN được xác định ở đâu?',['Annex I B.3.2','Annex II B.3.2','Annex III B.3.2','Annex IV B.3.2'],'B'),
('Cross-reference của một số điểm Annex I thép tới Annex III B.3.2 nên xử lý thế nào?',['Âm thầm sửa','Xóa reference','Ghi nhận khác biệt và NEEDS_LEGAL_REVIEW','Tự đổi phép tính'],'C'),
('Cân bằng carbon subtotal trong Excel tự động là complete SEE?',['Đúng','Chỉ với EAF','Không; còn boundary, source streams, precursors, attribution và scope','Chỉ nếu công thức chạy'],'C'),
('Trong billet case, consumed quantity bằng 50 + 1,000 − 30 là bao nhiêu?',['980 t','1,000 t','1,020 t','1,050 t'],'C'),
('PFC slope method sử dụng cặp gì?',['AEM với SEF và technology factor tương ứng','OVC với SEF của Table 2','AEM với electricity factor','Invoice với GWP'],'A'),
('Collection efficiency bị thiếu có thể mặc định 100% không có chứng cứ?',['Có','Không','Chỉ cho PFPB M','Chỉ cho năm 2026'],'B'),
('Minimum EF 0.525 tCO₂/t clinker trong tài liệu dùng như gì?',['Default value cho mọi hàng cement','Điều kiện phương pháp Method B trong phạm vi Annex II B.9.2.2','Giá trị SEE cuối cùng','CBAM benchmark'],'B'),
('Nếu output clinker stock tăng, dùng dấu tồn kho thế nào?',['Theo đúng định nghĩa/dấu trong Eq.27','Luôn cộng','Luôn trừ','Bỏ tồn kho'],'A'),
('Monitoring Plan cần được tổ chức bắt đầu từ đâu?',['Bảng Excel trống','Process flow, boundary và source streams','Mẫu Registry cũ','Báo giá verifier'],'B'),
('Monitoring Plan tự tạo của CTIC có thể gọi là official Registry template?',['Có','Không nếu chưa xác minh trực tiếp','Có nếu có logo','Có nếu lưu XLSX'],'B'),
('Actual, default và verified có phải cùng một trạng thái?',['Có','Không; theo dõi riêng','Verified luôn là default','Actual luôn verified'],'B'),
('SEFA và actual SEE có quan hệ nào?',['SEFA là tỷ lệ miễn actual SEE','Là đại lượng riêng; không áp benchmark như miễn trừ theo % actual SEE','Hai thuật ngữ thay thế nhau','SEFA chỉ là chi phí'],'B'),
('Regulation 2026/1412 là gì trong bối cảnh benchmark?',['Tự động sửa CBAM 2025/2620','EU ETS benchmark act; không tự động thay benchmark CBAM','Default value act','Carbon price credit act'],'B'),
('Một benchmark CBAM 2027 update đã được xác nhận trong source set?',['Có, đã có số row','Không; ghi NEEDS_LEGAL_REVIEW','Lấy từ EU ETS 2026/1412','Lấy từ model workbook'],'B'),
('COM(2026) 616 cần trình bày ra sao?',['Luật áp dụng 2028–2038','Proposal only, not law','Guidance binding','Directive in force'],'B'),
('Hiện hành từ 2034: cách ghi factor?',['0% factor','Không còn factor áp dụng theo nội dung được trích','14%','15%'],'B'),
('5% trong Article 5(1) của 2025/2546 là gì?',['Sai số operator được phép','Automatic pass threshold','Một thành tố quy tắc risk/materiality verifier; không phải blanket tolerance','Lượng mẫu tối thiểu'],'C'),
('Article 5(2) có thể yêu cầu đánh giá dưới 5%?',['Không','Có; expert judgement và tham số khác vẫn cần xem xét','Chỉ với cement','Chỉ nếu Registry yêu cầu'],'B'),
('Independent reviewer theo 2025/2551 nên được hiểu thế nào?',['Thành viên operator','Reviewer độc lập trong framework accreditation, không tự review phần mình làm','Carbon-price independent person mặc định','Importer'],'B'),
('Regulation 2026/2498, theo ngày 18-11-2026, trạng thái nào?',['Đã có hiệu lực 16-11','Được công bố 16-11, có hiệu lực 19-11, áp dụng từ 1-1-2026 theo văn bản','Chưa công bố','Chỉ áp dụng từ 2027'],'B'),
('Verifier theo 2025/2551 có tự động trở thành independent person cho báo cáo giá carbon?',['Có, tự động theo cùng phạm vi','Không tự động; Article 11 cho phép opt-in có điều kiện qua Registry trong kỳ 2026–27; đối tượng assurance vẫn riêng','Không thể trong bất kỳ trường hợp nào','Chỉ cần chữ ký operator'],'B'),
('Một workbook tính đúng chứng minh điều gì?',['Data source valid and verified','Arithmetic is correct under inputs only; source and legal validity remain separate','Legal approval','CN is correct'],'B'),
]
assessment=base_doc('KIỂM TRA KIẾN THỨC · 28 CÂU','Bài đánh giá học viên · 24 câu chọn đáp án + 4 câu ngắn · dùng sau toàn khóa')
for i,(q,opts,key) in enumerate(questions,1):
    p=assessment.add_paragraph();p.paragraph_format.keep_with_next=True;r=p.add_run(f'{i:02d}. {q}');r.bold=True;r.font.color.rgb=RGBColor.from_string(NAVY)
    for label,opt in zip('ABCD',opts): add_bullet(assessment,f'{label}. {opt}')
assessment.add_heading('Câu hỏi ngắn',1)
for q in ['Nêu 5 bằng chứng cần có để truy một giá trị precursor SEE đến hàng cuối cùng.','Giải thích vì sao SEFA/free-allocation adjustment không phải phần trăm miễn trừ của actual SEE.','Liệt kê 3 yếu tố verifier cần cân nhắc khi sai lệch dưới 5%.','Phân biệt ngày công bố, ngày có hiệu lực và ngày áp dụng của Regulation 2026/2498 theo tình trạng tại 18-11-2026.']:
    add_bullet(assessment,q)
assessment.add_paragraph('Đề chưa được CTIC phê duyệt. Có thể dùng formative assessment; không dùng để tuyên bố năng lực hành nghề hoặc công nhận pháp lý.')
assessment.save(os.path.join(OUT,'CTIC_CBAM_Expert_28Q_Assessment_VI_DRAFT.docx'))
keydoc=base_doc('ĐÁP ÁN GIẢNG VIÊN · 28 CÂU','24 câu trắc nghiệm và 4 câu ngắn · tài liệu riêng, không phát trước khi làm bài')
keydoc.add_heading('Đáp án trắc nghiệm',1)
t=keydoc.add_table(rows=1,cols=4);t.style='Light Shading Accent 1'
for c,x in zip(t.rows[0].cells,['Câu','Đáp án','Giải thích ngắn','Nguồn chính']):set_cell_text(c,x,True,WHITE,8);shade(c,NAVY)
why=['Mã CN cần thông số và quy tắc phân loại.','Signed mass balance dùng outflow âm.','OJ EN đặt công thức tại Annex II B.3.2.','Giữ bất nhất nguồn; không tự chữa.','Một subtotal không bằng SEE hoàn chỉnh.','50+1000−30=1020.','AEM, SEF và technology factor cùng method.','Eq.20 cần collection efficiency có chứng cứ.','0.525 chỉ trong Method B và điều kiện áp dụng.','Giữ dấu theo Eq.27.','MP bắt đầu bằng quy trình và ranh giới.','Không xác nhận mẫu Registry khi chưa kiểm tra.','Ba trạng thái phải tách.','SEFA là adjustment riêng.','2026/1412 là EU ETS benchmark act.','Không tìm thấy update binding trong source set.','COM proposal chưa phải luật.','No factor applies is not a 0% factor.','5% không phải blanket tolerance.','Article 5(2) vẫn đòi judgement.','Independent reviewer phải độc lập.','Article 32 tách ngày OJ, ngày có hiệu lực và ngày áp dụng.','Article 11 là opt-in có điều kiện; đối tượng carbon-price report khác SEE verification.','Formula QA không xác nhận source/legal validity.']
for i,((q,opts,k),ex) in enumerate(zip(questions,why),1):
    cells=t.add_row().cells
    if i in [3,4,5]: cite='2025/2547 Annex II B.3.2'
    elif i==22: cite='2026/2498 Article 32'
    elif i==23: cite='2026/2498 Articles 2(1), 10–11; 2025/2551 Annex I'
    else: cite='2025/2546 Art.5; 2025/2551 Annex II; see slide claim matrix for provision-level sources'
    for c,x in zip(cells,[i,k,ex,cite]):set_cell_text(c,x,False,'172B3A',8)
set_repeat_table_header(t.rows[0])
keydoc.add_heading('Gợi ý đáp án 4 câu ngắn',1)
for h,body in [
 ('1 · Precursor evidence','Supplier and installation identity; precursor CN/route; period and method; supplier value and verifier status/report; goods receipt and opening/closing stock; consumed quantity and link to output; control/version trail.'),
 ('2 · SEE versus SEFA','SEE describes attributed embedded emissions per functional unit. SEFA/free allocation is a separate benchmark-based adjustment derived under 2025/2620. Show both in same mass/period, but do not describe benchmark coverage as an equal percent reduction from actual SEE.'),
 ('3 · Under 5%','Expert judgement; qualitative/materiality nature; other parameters under Article 5(2); aggregate/cumulative effects; risk and source reliability; whether correction is necessary. There is no automatic safe harbour.'),
 ('4 · Dates 2026/2498','Article 32: published in OJ on 16 Nov 2026, enters into force on the third day after publication (19 Nov 2026), and applies from 1 Jan 2026. At the 18 Nov 2026 course cut-off it is published but not yet in force. Article 11 creates a conditional opt-in route for eligible verifiers for the 2026–27 reporting periods; it is not automatic and needs CTIC implementation review.')]:
    keydoc.add_heading(h,2);keydoc.add_paragraph(body)
keydoc.add_paragraph('Đáp án là tài liệu đào tạo, không chứng nhận legal interpretation hoặc năng lực verifier. Cần CTIC legal/technical review.')
keydoc.save(os.path.join(OUT,'CTIC_CBAM_Expert_28Q_Instructor_Key_VI_DRAFT.docx'))

# Glossary and provision-level claim matrix
glossary=[
('Actual emissions','Phát thải thực tế','Calculation status under applicable method; not automatically verified.'),('Accreditation scope','Phạm vi công nhận','Activity group and technical scope a verifier is authorised to cover.'),('Activity data','Dữ liệu hoạt động','Measured quantities feeding an emissions calculation.'),('Aggregated goods category','Nhóm hàng tổng hợp','Category used by the methodology; confirm mapping to CN and route.'),('Anode effect','Hiệu ứng anode','Electrolysis event relevant to aluminium PFC monitoring.'),('Authorised declarant','Người khai báo được uỷ quyền','Importer-side CBAM role under Regulation 2023/956.'),('Benchmark','Giá trị chuẩn','Keep CBAM benchmark separate from EU ETS benchmark.'),('Carbon balance','Cân bằng carbon','Balance of carbon streams under specified sign convention.'),('Carbon-price credit','Khoản khấu trừ giá carbon','Foreign carbon price actually paid, subject to legal conditions.'),('Carbon content','Hàm lượng carbon','Carbon mass per unit of stream; retain basis and unit.'),('CBAM factor','Hệ số CBAM','Factor in free-allocation adjustment; not a percent exemption of actual SEE.'),('CN code','Mã CN','Combined Nomenclature code; classify by legal product characteristics.'),('Collection efficiency','Hiệu suất thu gom','Used to reconcile duct/stack PFC with total including fugitive.'),('Complex goods','Hàng hoá phức hợp','Goods whose embedded emissions include precursor contribution.'),('CSCF','Hệ số điều chỉnh liên ngành','Cross-sectoral correction factor in applicable free allocation method.'),('Default value','Giá trị mặc định','Legal value matching exact year, origin, CN, route and version.'),('Direct emissions','Phát thải trực tiếp','Keep distinct from indirect emissions and installation energy.'),('Embedded emissions','Phát thải hàm chứa','Emissions attributed to covered goods and precursors under prescribed method.'),('Emission factor','Hệ số phát thải','Factor with source, unit, method, version and validity period.'),('Functional unit','Đơn vị chức năng','Denominator for goods-specific emission intensity.'),('Free-allocation adjustment (FAA)','Điều chỉnh phân bổ miễn phí','SEFA per unit × mass under Regulation 2025/2620.'),('Fugitive emissions','Phát thải thất thoát','Emissions not captured by ducts/stack; method-specific adjustment may apply.'),('GWP','Tiềm năng nóng lên toàn cầu','Gas-specific factor; use table required by applicable method.'),('Independent reviewer','Người rà soát độc lập','Reviewer in verifier accreditation system; not same as fieldwork reviewer.'),('Installation','Cơ sở lắp đặt','Installation-level reporting boundary, not identical to goods boundary.'),('Monitoring Plan','Kế hoạch giám sát','Operator plan describing monitoring method and controls.'),('OER','Báo cáo phát thải của người vận hành','Operator Emissions Report; check current Registry process and fields.'),('Operator','Người vận hành','Installation-side operator, distinct from importer/declarant.'),('PFC','Perfluorocarbon / khí perfluorocarbon','CF4/C2F6 emissions under aluminium monitoring method.'),('Precursor','Tiền chất','Input good whose embedded emissions may carry into complex good.'),('SEFA','Phát thải hàm chứa cụ thể dùng cho điều chỉnh phân bổ','Specific embedded free allocation; distinct from actual SEE.'),('SEE','Phát thải hàm chứa cụ thể','Specific embedded emissions per applicable functional unit.'),('Source stream','Dòng nguồn','Fuel/material/gas/electricity stream mapped to monitorable data.'),('Verified actual value','Giá trị thực tế đã được thẩm tra','Keep method status and verification status explicit.'),('Verifier','Tổ chức thẩm tra','Independent entity working within applicable accreditation scope.'),('Registry','Cơ quan đăng ký CBAM','European Commission CBAM Registry; public UI/templates may be incomplete.'),('Mass balance','Cân bằng khối lượng','Reconciliation of inputs, outputs, stocks and residues.'),('Uncertainty','Độ không đảm bảo','Characterisation and control of measurement/calculation uncertainty.'),('Primary aluminium','Nhôm sơ cấp','Route-specific variable for PFC method, not all aluminium output.'),('PFPB M','Anode công nghệ PFPB M','Technology designation used to match Table 2/3 factors.'),('Independent person','Pháp nhân độc lập chứng nhận báo cáo giá carbon','Regulation 2026/2498 Article 2(1); main accreditation, independence and competence requirements are in Article 10; eligible verifiers may opt in for reporting periods 2026–27 under Article 11, subject to conditions. This is distinct from SEE verification; implementation needs CTIC review.'),('Materiality','Tính trọng yếu','Verifier judgement context; not a blanket operator tolerance.'),('Activity group','Nhóm hoạt động','Accreditation category per 2025/2551 Annex I.'),('Functional boundary','Ranh giới chức năng','Process and attribution scope used for one goods group.'),('Annex','Phụ lục','Preserve roman numeral and point numbering in citations.'),('Corrigendum','Đính chính','Check language/version; a corrigendum in another language may not alter EN text.')]
with open(os.path.join(OUT,'CTIC_CBAM_EN_VI_Glossary_DRAFT.csv'),'w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['English','Vietnamese term','Definition / usage note','Status']);w.writerows([(*row,'CHỜ HIỆU ĐÍNH') for row in glossary])
with open(os.path.join(OUT,'CTIC_Expert_Claim_Traceability_Matrix_DRAFT.csv'),'w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['module','slide','claim_title','provision','source_id','source_title','url','status']);w.writeheader();w.writerows(all_rows)

# Course inventory, schedules and legal/source coverage dashboard.
inventory=[{'module':'EXP-01','slides':18,'minutes':90,'status':'Retained as delivered; not regenerated'},*({'module':m['code'],'slides':m['slideCount'],'minutes':m['duration'],'status':'Generated for CTIC review'} for m in DATA)]
assert sum(x['minutes'] for x in inventory)==720
assert 130<=sum(x['slides'] for x in inventory)<=150
coverage=[]
regulations=['2023/956','2023/959','2025/2547','2025/2546','2025/2551','2025/2620','2025/2621','2026/1740','2026/1412','2026/2498','COM(2026) 616']
for reg in regulations:
    hits=[r for r in all_rows if reg in r['source_title'] or reg in r['source_id'] or reg.replace('/','-') in r['source_id']]
    provisions=sorted(set(r['provision'] for r in hits))
    coverage.append([reg,len(hits),len(provisions),'SELECTED PROVISIONS CITED IN TRAINING; NOT FULL LEGAL TRANSLATION','CHỜ HIỆU ĐÍNH','NEEDS_LEGAL_REVIEW where flagged'])
with open(os.path.join(OUT,'CTIC_Expert_Translation_Coverage_Dashboard_DRAFT.csv'),'w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['Instrument','Claim-slide citations','Distinct provision strings','Coverage status','Translation status','Review status']);w.writerows(coverage)

road=base_doc('ROADMAP VÀ BÀN GIAO · EXPERT 12 GIỜ','Tổng khóa: 12 giờ · 2 ngày · dữ liệu tổng hợp · Draft PR #12')
road.add_heading('Tình trạng bàn giao',1)
t=road.add_table(rows=1,cols=4);t.style='Light Shading Accent 1'
for c,x in zip(t.rows[0].cells,['Module','Slide','Phút','Sản phẩm']):set_cell_text(c,x,True,WHITE,8);shade(c,NAVY)
for x in inventory:
    cells=t.add_row().cells
    for c,v in zip(cells,[x['module'],x['slides'],x['minutes'],x['status']]):set_cell_text(c,v,False,'172B3A',8)
road.add_paragraph('Tổng: 136 slide và 720 phút đào tạo (12 giờ). EXP-01 giữ nguyên 18 slide / 90 phút; module EXP-02–07 cộng 118 slide / 630 phút.')
road.add_heading('Tài liệu bàn giao',1)
for fn in sorted(os.listdir(OUT)):
    if fn.lower().endswith(('.pptx','.docx','.xlsx','.csv','.pdf','.png')) and not fn.endswith('.inspect.ndjson') and not fn.endswith('_PREVIEW.pdf') and not fn.endswith('_CONTACT_SHEET.png'):
        add_bullet(road,fn)
road.add_heading('Tài sản nền tảng được tái sử dụng',2)
road.add_paragraph('PR #10 (Draft, base SHA bd81ce59a8c2962836a7237e3949f32f7575dfdb) retains the 150-minute client course and its aluminium / steel-cement practice workbooks. Use these for the introductory client cases; the PR #12 workbook extends them for expert-level steel carbon balance, aluminium PFC/precursor, cement and SFA/SEFA calculations.')
road.add_paragraph('PR #11 (Draft, head SHA 0692a0324c38ceffa729d8a5810988e5d20f239f) contains the detailed Monitoring Plan, MRV, OER, evidence and verifier dossier workbook and guide. Use that package for the form-based exercises; no duplicate form workbook is copied into PR #12.')
road.add_paragraph('PR #10: https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/10  |  PR #11: https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/11')
road.add_heading('Danh sách NEEDS_LEGAL_REVIEW / CTIC decisions',1)
for item in ['Steel mass-balance Eq.12–15: Annex II B.3.2 versus Annex I steel cross-reference to Annex III B.3.2.','Regulation 2025/2547 Annex I point 3.3.2 English wording for clinker; preserve source wording pending review/corrigendum.','Product-specific CN, boundary, precursor and direct/indirect treatment for all live goods.','Whether a binding CBAM benchmark update applies from 2027; do not substitute Regulation 2026/1412 EU ETS values.','Regulation 2026/2498 Articles 10–11: Annex IV accreditation/competence/independence, conditional verifier opt-in for reporting periods 2026–27 and Registry assignment; Article 32 dates and retrospective application need CTIC implementation review.','Current Registry OER and verification report fields/templates: no public standalone template verified in reviewed source set.','Current consolidated amendments / legal version set for each actual reporting period.','The AI-assisted Vietnamese course text remains a reference draft, not a complete translation of any EU act.']:
    add_bullet(road,item)
road.add_heading('QA limitations',1)
for item in ['Artifact Tool rendered all EXP-02–07 slides; preview PDFs are compiled from the rendered slide PNGs. Visual inspection includes contact sheets and selected full-size slides; Office-native rendering was unavailable.','Workbook formulas recalculated and checked with Artifact Tool; exact outputs are recorded in WORKBOOK_QA.json. Native Excel recalculation could not be tested in this environment.','Word files are generated with controlled styles. Run render_docx.py before external training; native Word/Office is unavailable.','No legal reviewer or CTIC approver has signed off this package.']:
    add_bullet(road,item)
road.save(os.path.join(OUT,'CTIC_CBAM_Expert_Course_Roadmap_and_Handoff_VI_DRAFT.docx'))

print(json.dumps({'modules':inventory,'slide_total':sum(x['slides'] for x in inventory),'minutes':sum(x['minutes'] for x in inventory),'claim_rows':len(all_rows),'glossary_terms':len(glossary),'outputs':sorted(os.listdir(OUT))},ensure_ascii=True,indent=2))
