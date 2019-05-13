from fpdf import FPDF
import textwrap
import sys

LINES_PER_CARD = 10

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

    return readableList

pdf = FPDF()    
pdf.add_page()
pdf.set_font('Arial', 'B', 12)

with open(sys.argv[1], "r") as f:
    # we want to split text up so that it does not overflow cell
    # Note that this only works for current font
    stringSplit = split(f.read(), 40)
    print(stringSplit)

    newCardCount = 0
    for string in stringSplit:
        # determine if we are to start a new card
        if newCardCount == LINES_PER_CARD:
            pdf.cell(65, 2, "", 0, 1, 'L')
            newCardCount = 0

        pdf.cell(65, 5, string, 0, 1, 'L')
        newCardCount += 1

pdf.output('palmCards.pdf', 'F')