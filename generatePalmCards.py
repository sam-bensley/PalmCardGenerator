# Generates Palm Cards from text file in cmd line input

from fpdf import FPDF
import textwrap
import sys

# PARAMETERS FOR PRINTING CELL
CELL_WIDTH = 70
CELL_HEIGHT = 6
BORDER_FLAG = 0
LN = 2          # where the pointer moves after the cell is printed
TEXT_ALIGNMENT = 'L'

# PARAMETERS FOR MARGIN
LEFT_MARGIN = 254
RIGHT_MARGIN = -254
TOP_MARGIN = 254

# PARAMETERS FOR CARDS
LINES_PER_CARD = 10
CARDS_PER_COLUMN = 4
COLUMNS_PER_PAGE = 2

# PARAMTERS FOR FONT
FONT_SIZE = 12

# split up text into a list of lines which
# are readable and do not contain half cut
# off words
def split(text, maximumCharacters):
    readableList = []
    splitText = text.split(" ")
    
    line = ""
    for word in splitText:
        # if adding this word exceeds maxmimumCharacters
        # append existing line to readable list and
        if len(line) + len(word) > maximumCharacters:
            readableList.append(line)
            line = ""
        
        # otherwise we can add this word to the line
        line += (word + " ")    
    
    # append the last line
    readableList.append(line)
    return readableList

def convertTextToPDF(text, fileName):
    # create pdf object
    pdf = FPDF('P', 'mm', 'A4')    
    pdf.add_page()
    pdf.set_margins(LEFT_MARGIN, TOP_MARGIN, RIGHT_MARGIN)
    pdf.set_font('Arial', 'B', FONT_SIZE)

    # we want to split text up so that it does not overflow cell
    # Note that this only works for current font
    stringSplit = split(text, 40)

    linesOnCard = 0
    cardsOnColumn = 0
    columnsOnPage = 0
    for string in stringSplit:
        # determine if we are to start a new card
        if linesOnCard == LINES_PER_CARD:
            pdf.cell(CELL_WIDTH, CELL_HEIGHT, "", BORDER_FLAG, LN, TEXT_ALIGNMENT)
            linesOnCard = 0
            cardsOnColumn += 1

        # determine if we are to start a new column
        if cardsOnColumn == CARDS_PER_COLUMN:
            # update the pointer
            pdf.set_xy(110, 10)     # this is not measured in mm...

            cardsOnColumn = 0
            columnsOnPage += 1

        # determine if we are to start a new page
        if columnsOnPage == COLUMNS_PER_PAGE:
            pdf.add_page()
            pdf.set_xy(10, 10)      # don't know why I have to set this again
            columnsOnPage = 0

        # now we add the line
        pdf.cell(CELL_WIDTH, CELL_HEIGHT, string, BORDER_FLAG, LN, TEXT_ALIGNMENT)
        linesOnCard += 1

    pdf.output("speeches/"+fileName, 'F')

