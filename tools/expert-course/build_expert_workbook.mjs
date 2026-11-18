import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const OUT=path.join(ROOT,'outputs/issue-5-expert-course');
const BUILD=path.join(ROOT,'.build/expert-course');
const C={navy:'#102B3F',teal:'#087E8B',mint:'#DDF3EE',paper:'#F4F7F8',white:'#FFFFFF',ink:'#172B3A',muted:'#526777',amber:'#FFF2D8',red:'#FCE8E6',grid:'#D7E1E7',input:'#FFF7DA',formula:'#E7F3F0'};
const SOURCES=[
 ['ACT-2025-2547','Commission Implementing Regulation (EU) 2025/2547','https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng'],
 ['ACT-2023-956-CONS-2025-10-20','Regulation (EU) 2023/956 consolidated text dated 20 October 2025; check amending acts','https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng'],
 ['ACT-2025-2620','Commission Implementing Regulation (EU) 2025/2620','https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng'],
 ['ACT-2026-1412','Commission Implementing Regulation (EU) 2026/1412 — EU ETS benchmarks, not CBAM benchmarks','https://eur-lex.europa.eu/eli/reg_impl/2026/1412/oj/eng'],
 ['ACT-2023-959','Directive (EU) 2023/959, Article 1 amending Directive 2003/87/EC, Article 10a(1a)','https://eur-lex.europa.eu/eli/dir/2023/959/oj/eng'],
 ['PROP-COM-2026-616','COM(2026) 616 final — proposal only, 2026/0212(COD)','https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0616'],
 ['ACT-2026-2498','Commission Implementing Regulation (EU) 2026/2498 — OJ 16 Nov 2026; enters into force 19 Nov 2026; applies from 1 Jan 2026','https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng']
];
const wb=Workbook.create();
function sheet(name,title,subtitle,headers) {
 const s=wb.worksheets.add(name); s.showGridLines=false;
 const last=String.fromCharCode(64+headers.length);
 s.getRange(`A1:${last}1`).merge();s.getRange('A1').values=[[title]];
 s.getRange(`A2:${last}2`).merge();s.getRange('A2').values=[[subtitle]];
 s.getRange(`A1:${last}1`).format={fill:C.navy,font:{name:'Aptos Display',size:18,bold:true,color:C.white},verticalAlignment:'center',wrapText:true};
 s.getRange(`A2:${last}2`).format={fill:C.amber,font:{name:'Aptos',size:10,bold:true,color:'#7A4B00'},verticalAlignment:'center',wrapText:true};
 s.getRange(`A4:${last}4`).values=[headers];s.getRange(`A4:${last}4`).format={fill:C.teal,font:{name:'Aptos',size:10,bold:true,color:C.white},verticalAlignment:'center',wrapText:true,borders:{preset:'all',style:'thin',color:C.grid}};
 s.getRange(`A1:${last}1`).format.rowHeight=34;s.getRange(`A2:${last}2`).format.rowHeight=36;s.getRange(`A4:${last}4`).format.rowHeight=34;
 s.freezePanes.freezeRows(4);s.tabColor=C.teal;return s;
}
function styleRange(s,range,fill,fontColor=C.ink,bold=false){s.getRange(range).format={fill,font:{name:'Aptos',size:10,color:fontColor,bold},verticalAlignment:'center',wrapText:true,borders:{preset:'all',style:'thin',color:C.grid}};}
function widths(s,vals){vals.forEach((v,i)=>{const col=String.fromCharCode(65+i);s.getRange(`${col}:${col}`).format.columnWidth=v;});}

let s=sheet('Start Here','CTIC VIETNAM · BÀI TẬP EXCEL CBAM','DRAFT — số liệu hoạt động là tổng hợp; workbook phục vụ đào tạo, không phải OER/Registry form chính thức, không xác nhận SEE hoặc chi phí pháp lý. Tất cả bản tiếng Việt CHỜ HIỆU ĐÍNH.', ['Mục','Hướng dẫn','Trạng thái']);
s.getRange('A5:C12').values=[
 ['01 · Màu vàng','Input do người học sửa trong phạm vi bài tập.','SYNTHETIC TRAINING DATA'],
 ['02 · Màu xanh nhạt','Ô công thức. Không ghi đè formula; đọc comment/citation trong dòng nguồn.','FORMULA / TRAINING ONLY'],
 ['03 · Steel Balance','Signed activity × carbon content; check net carbon subtotal and tCO₂ conversion. This is not complete SEE.','2025/2547 Annex II B.3.2 Eq.12–15; note Annex I cross-reference conflict.'],
 ['04 · Aluminium','Reconcile precursor consumed from inventory; include scrap/output mass check and local emissions.','Arithmetic is synthetic; confirm specific legal boundary.'],
 ['05 · PFC','Practice the slope method for a synthetic PFPB M case; legal factor pair and GWP must match route/version.','2025/2547 Annex II B.7; Table 2 and Table 6.'],
 ['06 · Cement','Illustrate a clinker/cement calculation; electricity inputs are separate and treatment depends on applicable product rules.','2025/2547 Annex II B.9.2.2; Annex III Eq.64.'],
 ['07 · SEFA & cost','Separate embedded emissions, SEFA/free-allocation adjustment and hypothetical certificate price. No carbon-price credit included.','2025/2620 Annex Eqs.1–6; synthetic inputs, not payable amount.'],
 ['08 · Current/proposal factors','Separate current-law factor schedule from COM(2026)616 proposal. Proposal is not law; from 2034 current law says no factor applies.','2023/959; COM(2026)616; proposal status must be rechecked.']
];styleRange(s,'A5:C12',C.white);styleRange(s,'B5:B12',C.input);widths(s,[28,78,78]);s.getRange('A5:C12').format.rowHeight=48;
const startSheet=s;

s=sheet('Steel Balance','SẮT THÉP · CÂN BẰNG CARBON CÓ DẤU','All values are synthetic. Inputs +, outputs −. Carbon balance subtotal does not equal complete product SEE. Formula source: Regulation (EU) 2025/2547 Annex II B.3.2 Eq.12–15; steel Annex I has a differing B.3.2 cross-reference that remains NEEDS_LEGAL_REVIEW.', ['Source stream','Type','Activity (t)','Signed activity (t)','Carbon fraction (tC/t)','Carbon (tC)','Source / status']);
s.getRange('A5:C9').values=[['Pig iron','Input',10000],['Steel scrap','Input',5000],['EAF carbon charge','Input',150],['Carbon electrode','Input',20],['Crude steel','Output',14000]];
s.getRange('D5').formulas=[['=IF(B5="Output",-C5,C5)']];s.getRange('D5:D9').fillDown();
s.getRange('E5:E9').values=[[0.0409],[0.0109],[0.8297],[0.8188],[0.002]];
s.getRange('F5').formulas=[['=D5*E5']];s.getRange('F5:F9').fillDown();
s.getRange('G5:G9').values=Array(5).fill(['Synthetic training fixture; factor/content values are illustrative assumptions, not actual plant data.']);
s.getRange('A11:B14').values=[['Net carbon balance (tC)',''],['CO₂ subtotal (tCO₂)',''],['Intensity subtotal (tCO₂/t crude steel)',''],['Independent check difference (tCO₂)','']];
s.getRange('B11').formulas=[['=SUM(F5:F9)']];s.getRange('B12').formulas=[['=B11*3.664']];s.getRange('B13').formulas=[['=B12/C9']];
s.getRange('B14').formulas=[['=B12-((10000*0.0409+5000*0.0109+150*0.8297+20*0.8188-14000*0.002)*3.664)']];
s.getRange('A16:G18').merge();s.getRange('A16').values=[['LEGAL CONTROL: Equations 12–15 were located in Annex II B.3.2 in the English OJ text. Steel Annex I cross-references point to Annex III B.3.2. Preserve both facts; interpretation/cross-reference remains NEEDS_LEGAL_REVIEW. This subtotal omits other required source streams, attribution, precursors, and scope checks.']];styleRange(s,'A16:G18',C.amber,'#7A4B00',true);s.getRange('A16:G18').format.rowHeight=30;
styleRange(s,'A5:G9',C.white);styleRange(s,'C5:C9',C.input);styleRange(s,'E5:E9',C.input);styleRange(s,'D5:D9',C.formula);styleRange(s,'F5:F9',C.formula);styleRange(s,'A11:B14',C.mint);s.getRange('B11:B14').format.numberFormat='0.0000';widths(s,[26,14,18,20,22,18,78]);s.getRange('A5:G9').format.rowHeight=35;
const steelSheet=s;

s=sheet('Aluminium','NHÔM · ĐỐI SOÁT TIỀN CHẤT','Synthetic billet→profile case. Keep tonnes, inventory, output and precursor emissions separate; do not double-count purchased billet. Source methods must be confirmed for a real good/CN/period.', ['Driver / result','Value','Unit','Source / status']);
s.getRange('A5:D15').values=[
 ['Opening billet stock',50,'t','Synthetic'],['Billet receipts',1000,'t','Synthetic'],['Closing billet stock',30,'t','Synthetic'],['Billet consumed',null,'t','Formula'],['Profile output',1000,'t','Synthetic'],['Scrap / dross',20,'t','Synthetic'],['Mass balance variance',null,'t','Formula'],['Precursor SEE',1.5,'tCO₂e/t billet','Synthetic supplier value'],['Local process emissions',22,'tCO₂e','Synthetic'],['Total training emissions',null,'tCO₂e','Formula'],['Specific intensity',null,'tCO₂e/t profile','Formula']
];
s.getRange('B8').formulas=[['=B5+B6-B7']];s.getRange('B11').formulas=[['=B8-B9-B10']];s.getRange('B14').formulas=[['=B8*B12+B13']];s.getRange('B15').formulas=[['=B14/B9']];
styleRange(s,'A5:D15',C.white);styleRange(s,'B5:B7',C.input);styleRange(s,'B9:B10',C.input);styleRange(s,'B12:B13',C.input);styleRange(s,'B8:B8',C.formula);styleRange(s,'B11:B11',C.formula);styleRange(s,'B14:B15',C.formula);s.getRange('B5:B15').format.numberFormat='0.000';widths(s,[36,18,24,70]);s.getRange('A17:D19').merge();s.getRange('A17').values=[['Answer check: billet consumed = 1,020 t; mass variance = 0 t; precursor contribution = 1,530 tCO₂e; total = 1,552 tCO₂e; training intensity = 1.552 tCO₂e/t. Not verified SEE. Sources: Regulation (EU) 2025/2547 Article 4 and Annex III B, Eqs.59–64.']];styleRange(s,'A17:D19',C.mint,C.ink,true);s.getRange('A17:D19').format.rowHeight=29;
const aluminiumSheet=s;

s=sheet('Al PFC','NHÔM · THỰC HÀNH PFC SLOPE METHOD','Synthetic activity data; legal factors from the named technology row in 2025/2547 Annex II Table 2 and GWP Table 6. Verify technology before application; do not mix method A/B.', ['Variable / result','Value','Unit','Source / status']);
s.getRange('A5:D19').values=[
 ['AE frequency',0.08,'events/cell-day','Synthetic'],['Average AE duration',1.4,'minutes/event','Synthetic'],['AEM',null,'AE-min/cell-day','Formula'],['Primary aluminium output',20000,'t','Synthetic'],['SEF CF₄ · PFPB M',0.104,'kg CF₄/(AE-min·t Al)','2025/2547 Annex II B.7.1 Table 2'],['C₂F₆/CF₄ fraction · PFPB M',0.057,'t/t','2025/2547 Annex II B.7.1 Table 2'],['CF₄ duct/stack',null,'t CF₄','Formula: Eq.21'],['C₂F₆ duct/stack',null,'t C₂F₆','Formula: Eq.22'],['Collection efficiency',0.9,'% (decimal)','Synthetic; needs measured support'],['CF₄ total incl. fugitive',null,'t CF₄','Formula: Eq.20'],['C₂F₆ total incl. fugitive',null,'t C₂F₆','Formula: Eq.20'],['GWP CF₄',6630,'tCO₂e/t','2025/2547 Annex II point G Table 6'],['GWP C₂F₆',11100,'tCO₂e/t','2025/2547 Annex II point G Table 6'],['PFC emissions',null,'tCO₂e','Formula: Eq.26'],['Verification status','SYNTHETIC','—','Not actual / not verified']
];
s.getRange('B7').formulas=[['=B5*B6']];s.getRange('B11').formulas=[['=B7*B9*B8/1000']];s.getRange('B12').formulas=[['=B11*B10']];s.getRange('B14').formulas=[['=B11/B13']];s.getRange('B15').formulas=[['=B12/B13']];s.getRange('B18').formulas=[['=B14*B16+B15*B17']];
styleRange(s,'A5:D20',C.white);styleRange(s,'B5:B6',C.input);styleRange(s,'B8:B10',C.input);styleRange(s,'B13:B13',C.input);styleRange(s,'B16:B17',C.input);styleRange(s,'B7:B7',C.formula);styleRange(s,'B11:B12',C.formula);styleRange(s,'B14:B15',C.formula);styleRange(s,'B18:B18',C.formula);s.getRange('B5:B18').format.numberFormat='0.0000';widths(s,[39,18,32,72]);s.getRange('A22:D24').merge();s.getRange('A22').values=[['Control: CF₄ duct = AEM × SEF × primary Al / 1,000. Eq.20 adjusts total for measured collection efficiency. This case uses PFPB M technology factors only. No conclusion about any plant is implied.']];styleRange(s,'A22:D24',C.amber,'#7A4B00',true);s.getRange('A22:D24').format.rowHeight=28;
const pfcSheet=s;

s=sheet('Cement','XI MĂNG · CLINKER → CEMENT','Training illustration only. Eq.27 / Method B minimum factor condition and Eq.64 are cited; local fuel/electricity inputs and clinker fraction are synthetic. Validate product boundary and direct/indirect treatment by CN and period.', ['Driver / result','Value','Unit','Source / status']);
s.getRange('A5:D15').values=[
 ['Clinker output',1000,'t','Synthetic'],['Method B minimum factor',0.525,'tCO₂/t clinker','2025/2547 Annex II B.9.2.2'],['Clinker process emissions',null,'tCO₂','Formula illustration'],['Fuel emissions',200,'tCO₂','Synthetic'],['Electricity',120,'MWh','Synthetic'],['Electricity factor',0.5,'tCO₂/MWh','Synthetic; scope dependent'],['Electricity emissions',null,'tCO₂e','Formula illustration'],['Training total',null,'tCO₂e','Formula; scope review required'],['Clinker content in cement',0.86,'fraction','Synthetic'],['Training clinker component',null,'tCO₂e/t cement','Simplified illustration only'],['Method/source note','CHECK','—','Not legal SEE or default']
];
s.getRange('B7').formulas=[['=B5*B6']];s.getRange('B11').formulas=[['=B9*B10']];s.getRange('B12').formulas=[['=B7+B8+B11']];s.getRange('B14').formulas=[['=B12/B5*B13']];
styleRange(s,'A5:D15',C.white);styleRange(s,'B5:B6',C.input);styleRange(s,'B8:B10',C.input);styleRange(s,'B13:B13',C.input);styleRange(s,'B7:B7',C.formula);styleRange(s,'B11:B12',C.formula);styleRange(s,'B14:B14',C.formula);styleRange(s,'A17:D19',C.amber,'#7A4B00',true);s.getRange('A17:D19').merge();s.getRange('A17').values=[['Workbook arithmetic: clinker process 525 + fuel 200 + electricity 60 = 785 tCO₂e; 0.785 tCO₂e/t clinker; simplified clinker component 0.6751 tCO₂e/t cement. The last figure is not final cement SEE. Eq.27 is clinker quantity method; Eq.64 is attribution under its exact terms.']];s.getRange('A17:D19').format.rowHeight=28;s.getRange('B5:B14').format.numberFormat='0.0000';widths(s,[39,18,27,72]);
const cementSheet=s;

s=sheet('SEE SEFA Cost','SEE · SEFA · KỊCH BẢN CHỨNG CHỈ','Do not apply SEFA as an exemption percentage to actual SEE. Benchmark/CSCF/factor are explicitly synthetic. Carbon-price credit is excluded pending separate evidence and legal review; cost is not payable amount.', ['Driver / result','Value','Unit','Source / status']);
s.getRange('A5:D16').values=[
 ['Imported goods mass',1000,'t','Synthetic'],['Actual SEE',1.8,'tCO₂e/t','Synthetic; not verified'],['CBAM factor',0.9,'fraction','Synthetic scenario only'],['CSCF',0.85,'fraction','Synthetic scenario only'],['CBAM benchmark',0.5,'tCO₂e/t','Synthetic scenario only'],['SFA process-level',null,'tCO₂e/t','Regulation 2025/2620 Annex, Eq.2'],['SEFA simple good',null,'tCO₂e/t','Regulation 2025/2620 Annex, Eq.3'],['FAA (SEFA × mass)',null,'tCO₂e','Regulation 2025/2620 Annex, Eq.1'],['Embedded emissions',null,'tCO₂e','Formula'],['Scenario certificates before carbon-price credit',null,'t','Formula only'],['Certificate price',70,'EUR/t','Synthetic'],['Gross scenario cost',null,'EUR','No carbon-price credit or legal adjustments']
];
s.getRange('B10').formulas=[['=B7*B8*B9']];s.getRange('B11').formulas=[['=B10']];s.getRange('B12').formulas=[['=B11*B5']];s.getRange('B13').formulas=[['=B5*B6']];s.getRange('B14').formulas=[['=MAX(B13-B12,0)']];s.getRange('B16').formulas=[['=B14*B15']];
styleRange(s,'A5:D16',C.white);styleRange(s,'B5:B9',C.input);styleRange(s,'B15:B15',C.input);styleRange(s,'B10:B14',C.formula);styleRange(s,'B16:B16',C.formula);s.getRange('B5:B16').format.numberFormat='0.0000';s.getRange('B16').format.numberFormat='€#,##0.00';widths(s,[54,20,27,75]);s.getRange('A18:D21').merge();s.getRange('A18').values=[['Illustration: process SFA (Eq.2)=0.3825 tCO₂e/t; simple-good SEFA (Eq.3)=0.3825; FAA (Eq.1)=382.5 tCO₂e; embedded emissions=1,800; scenario certificates=1,417.5; gross scenario cost=€99,225. Every driver is synthetic. Legal calculation must match applicable good, year, benchmark, actual/default status, period and eligible adjustments.']];styleRange(s,'A18:D21',C.amber,'#7A4B00',true);s.getRange('A18:D21').format.rowHeight=27;
const sefaSheet=s;

s=sheet('Factors','CURRENT LAW · PROPOSAL RIÊNG','Factors apply to free allocation calculations as specified by governing legal acts; they are not a percentage exemption from actual SEE. Proposal column is not law.', ['Year','Current-law factor','Legal status','COM(2026) 616 proposed factor','Proposal status']);
s.getRange('A5:E15').values=[
 [2028,0.9,'Directive 2003/87 Art.10a(1a), as amended by 2023/959',0.915,'Proposal only'],
 [2029,0.775,'Directive 2003/87 Art.10a(1a), as amended by 2023/959',0.81,'Proposal only'],
 [2030,0.515,'Directive 2003/87 Art.10a(1a), as amended by 2023/959',0.59,'Proposal only'],
 [2031,0.39,'Directive 2003/87 Art.10a(1a), as amended by 2023/959',0.48,'Proposal only'],
 [2032,0.265,'Directive 2003/87 Art.10a(1a), as amended by 2023/959',0.375,'Proposal only'],
 [2033,0.14,'Directive 2003/87 Art.10a(1a), as amended by 2023/959',0.27,'Proposal only'],
 [2034,null,'No factor applies from 2034 under cited current-law text',0.15,'Proposal only'],
 [2035,null,'No factor applies from 2034 under cited current-law text',0.15,'Proposal only'],
 [2036,null,'No factor applies from 2034 under cited current-law text',0.15,'Proposal only'],
 [2037,null,'No factor applies from 2034 under cited current-law text',0.15,'Proposal only'],
 [2038,null,'No factor applies from 2034 under cited current-law text',0,'Proposal only']
];styleRange(s,'A5:E15',C.white);styleRange(s,'B5:B15',C.formula);styleRange(s,'D5:E15',C.amber);s.getRange('B5:B15').format.numberFormat='0.0%';s.getRange('D5:D15').format.numberFormat='0.0%';widths(s,[14,21,68,32,25]);
s.getRange('A17:E20').merge();s.getRange('A17').values=[['Source: 2023/959 Article 1 amendments to Directive 2003/87 Article 10a(1a); COM(2026)616 final, procedure 2026/0212(COD), proposal only. “No factor applies from 2034” is not restated as a 0% current-law factor. Proposal 2038 shows 0% only in the proposal column. Recheck legal status before use.']];styleRange(s,'A17:E20',C.red,'#8A2220',true);s.getRange('A17:E20').format.rowHeight=27;

s=sheet('Source Register','NGUỒN VÀ ĐIỀU KHOẢN','EUR-Lex / Commission public sources. Guidance is not binding law; proposal is not law. This workbook has not received CTIC legal approval.', ['Source ID','Instrument / source','Provision used','URL','Status']);
s.getRange('A5:E11').values=[
 [SOURCES[0][0],SOURCES[0][1],'Annex II B.3.2 Eq.12–15; Annex II B.7 Eq.20–26 Tables 2/6; Annex II B.9.2.2 Eq.27; Annex III Eq.64',SOURCES[0][2],'Official OJ EN source; interpretation CHỜ CTIC review'],
 [SOURCES[1][0],SOURCES[1][1],'Articles 7–9; Annexes II and IV',SOURCES[1][2],'Consolidated text dated 2025-10-20; verify amendments'],
 [SOURCES[2][0],SOURCES[2][1],'Annex, Equations 1–6',SOURCES[2][2],'Official OJ EN source'],
 [SOURCES[3][0],SOURCES[3][1],'Title / Article 1–2; EU ETS benchmark act',SOURCES[3][2],'Do not substitute for CBAM 2025/2620 benchmark'],
 [SOURCES[4][0],SOURCES[4][1],'Article 1 amending Art.10a(1a)',SOURCES[4][2],'Current-law factor schedule; legal review pending'],
 [SOURCES[5][0],SOURCES[5][1],'Proposal and procedure 2026/0212(COD)',SOURCES[5][2],'PROPOSAL ONLY — NOT LAW'],
 [SOURCES[6][0],SOURCES[6][1],'Articles 2(1), 10(1)–(3), 11(1)–(4), 32; Annex IV',SOURCES[6][2],'NEEDS_LEGAL_REVIEW: EUR-Lex metadata checked; full official text retrieval blocked in runner; CTIC must verify provisions and implementation dates']
];styleRange(s,'A5:E11',C.white);s.getRange('D5:D11').format.font={name:'Aptos',size:9,color:C.teal};widths(s,[34,63,76,84,64]);s.getRange('A5:E11').format.rowHeight=55;

await fs.mkdir(OUT,{recursive:true});await fs.mkdir(BUILD,{recursive:true});wb.recalculate();
const results={steelBalance:steelSheet.getRange('B11:B14').values,aluminium:aluminiumSheet.getRange('B8:B15').values,pfc:pfcSheet.getRange('B7:B18').values,cement:cementSheet.getRange('B7:B14').values,sefa:sefaSheet.getRange('B10:B16').values};
const numeric=x=>Number(x?.[0]?.[0]);const near=(name,actual,expected)=>{if(!Number.isFinite(actual)||Math.abs(actual-expected)>1e-8)throw new Error(`${name}: expected ${expected}, got ${actual}`);};
near('steel net carbon tC',numeric(results.steelBalance),576.331);near('steel CO2 subtotal',numeric(results.steelBalance.slice(1)),576.331*3.664);near('steel independent check',numeric(results.steelBalance.slice(3)),0);
near('aluminium billet consumed',numeric(results.aluminium),1020);near('aluminium variance',numeric(results.aluminium.slice(3)),0);near('aluminium intensity',numeric(results.aluminium.slice(7)),1.552);
near('PFC AEM',numeric(results.pfc),0.112);near('PFC total CO2e',numeric(results.pfc.slice(11)),((0.112*0.104*20000/1000)/0.9*6630 + ((0.112*0.104*20000/1000*0.057)/0.9)*11100));
near('cement training total',numeric(results.cement.slice(5)),785);near('SFA process-level',numeric(results.sefa),0.3825);near('SEFA simple good',numeric(results.sefa.slice(1)),0.3825);near('FAA',numeric(results.sefa.slice(2)),382.5);near('cost scenario',numeric(results.sefa.slice(6)),99225);
const formulaError=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:300},summary:'expert course workbook formula error scan'});
await fs.writeFile(`${BUILD}/workbook_error_scan.ndjson`,formulaError.ndjson??'','utf8');
const xlsx=await SpreadsheetFile.exportXlsx(wb);await xlsx.save(`${OUT}/CTIC_Expert_CBAM_Practice_Workbook_VI_DRAFT.xlsx`);
const sheetNames=['Start Here','Steel Balance','Aluminium','Al PFC','Cement','SEE SEFA Cost','Factors','Source Register'];
for(const name of sheetNames){const blob=await wb.render({sheetName:name,autoCrop:'all',scale:1,format:'png'});await fs.writeFile(`${BUILD}/workbook_${name.toLowerCase().replace(/[^a-z0-9]+/g,'_')}.png`,new Uint8Array(await blob.arrayBuffer()));}
const qa={sheetNames,formulaErrors:formulaError.ndjson,results,expected:{steelNetCarbon_tC:576.331,aluminiumIntensity:1.552,pfcMethod:'PFPB M formula chain',cementIllustration_tCO2e:785,sfaProcessLevelEq2:0.3825,sefaSimpleGoodEq3:0.3825,freeAllocationAdjustmentEq1_tCO2e:382.5,embeddedEmissions_tCO2e:1800,scenarioCertificates:1417.5,grossScenarioCostEUR:99225},limitations:['Not opened/recalculated in native Excel; no Office available in this environment.','No legal approval; all non-source workbook values are synthetic.','Workbook errors scan and Artifact Tool calculation only.']};
await fs.writeFile(`${OUT}/WORKBOOK_QA.json`,JSON.stringify(qa,null,2),'utf8');console.log(JSON.stringify(qa,null,2));
