# Import FPDF class
from fpdf import FPDF
 
# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
pdf=FPDF(format='letter', unit='in')
 
# Add new page. Without this you cannot create the document.
pdf.add_page()
 
# Remember to always put one of these at least once.
pdf.set_font('Times','',10.0) 
 
# Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin
 
# Set column width to 1/4 of effective page width to distribute content 
# evenly across table and page
col_width = epw/2
 
# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.
 
data = [['First name im an going to put wang to happpen','Last name'],
['Jules','Smith'],
['Mary','Ramos'],[
'Carlson','Banks']]
 
# Document title centered, 'B'old, 14 pt
pdf.set_font('Times','',10.0) 
pdf.ln(0.5)
 
# Text height is the same as current font size
th = pdf.font_size
 
# Here we add more padding by passing 2*th as height
for row in data:
    
    for datum in row:
        # Enter data in colums
        pdf.multicell(col_width, 5*th, str(datum), border=0)
        
    pdf.ln(5*th)
 
pdf.output('table-using-cell-borders.pdf','F')