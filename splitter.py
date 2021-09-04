import PyPDF2
from PyPDF2.pdf import PageObject
import sys
import math

def main(inputPdf, outputPdf):

    print(inputPdf + outputPdf)

    # creating input pdf file object
    pdfFileObj = open(inputPdf, 'rb')

    # creating pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, False)

    pages = pdfReader.numPages
    print("number of pages: " + str(pdfReader.numPages))

    # added 4 blank end-pages and some more blanks // not done automatically anymore
    # so the number of pages is the larger nearest multiplication of 8
    # pages = math.ceil((pdfReader.numPages) / 8) * 8
    # print("number of pages after added some blank end-pages: " + str(pages))

    # number of paper needed
    papers = math.ceil((pages / 8))
    print("number of paper used to print: " + str(papers))

    newPages = []
    print("")

    # generating the new order
    isOdd = True
    pdfWriter = PyPDF2.PdfFileWriter()
    for x in range(1, papers * 2 + 1):
        if isOdd:
            print("page of " + str(x) + " top-left " + str(pages + 1 - x))
            print("page of " + str(x) + " top-right " + str(x))
            print("page of " + str(x) + " bottom-left " + str(pages - papers * 2  + 1 - x))
            print("page of " + str(x) + " bottom-right " + str(papers * 2 + x))
            newPages.append(str(pages + 1 - x))
            newPages.append(str(x))
            newPages.append(str(pages - papers * 2  + 1 - x))
            newPages.append(str(papers * 2 + x))

            translated_page = PageObject.createBlankPage(
                None,
                pdfReader.getPage(1).mediaBox.getWidth(),
                pdfReader.getPage(1).mediaBox.getHeight(),
            )

            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(pages - x), 0.5,
                0, int(pdfReader.getPage(1).mediaBox.getHeight()/2)
            )
            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(x - 1), 0.5,
                int(pdfReader.getPage(1).mediaBox.getWidth()/2), int(pdfReader.getPage(1).mediaBox.getHeight()/2)
            )
            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(pages - papers * 2  - x), 0.5,
                0, 0
            )
            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(papers * 2 + x - 1), 0.5,
                int(pdfReader.getPage(1).mediaBox.getWidth()/2), 0
            )

            pdfWriter.addPage(translated_page)

            # pdfWriter.addPage(pdfReader.getPage(pages - x))
            # pdfWriter.addPage(pdfReader.getPage(x - 1))
            # pdfWriter.addPage(pdfReader.getPage(pages - papers * 2  - x))
            # pdfWriter.addPage(pdfReader.getPage(papers * 2 + x - 1))
            isOdd = False
        else:
            print("page of " + str(x) + " top-left " + str(x))
            print("page of " + str(x) + " top-right " + str(pages + 1 - x))
            print("page of " + str(x) + " bottom-left " + str(papers * 2 + x))
            print("page of " + str(x) + " bottom-right " + str(pages - papers * 2  + 1 - x))
            newPages.append(str(x))
            newPages.append(str(pages + 1 - x))
            newPages.append(str(papers * 2 + x))
            newPages.append(str(pages - papers * 2  + 1 - x))
            
            translated_page = PageObject.createBlankPage(
                None,
                pdfReader.getPage(1).mediaBox.getWidth(),
                pdfReader.getPage(1).mediaBox.getHeight(),
            )

            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(x - 1), 0.5,
                0, int(pdfReader.getPage(1).mediaBox.getHeight()/2)
            )
            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(pages - x), 0.5,
                int(pdfReader.getPage(1).mediaBox.getWidth()/2), int(pdfReader.getPage(1).mediaBox.getHeight()/2)
            )
            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(papers * 2 + x - 1), 0.5,
                0, 0
            )
            translated_page.mergeScaledTranslatedPage(
                pdfReader.getPage(pages - papers * 2  - x), 0.5,
                int(pdfReader.getPage(1).mediaBox.getWidth()/2), 0
            )

            pdfWriter.addPage(translated_page)

            # pdfWriter.addPage(pdfReader.getPage(x - 1))
            # pdfWriter.addPage(pdfReader.getPage(pages - x))
            # pdfWriter.addPage(pdfReader.getPage(papers * 2 + x - 1))
            # pdfWriter.addPage(pdfReader.getPage(pages - papers * 2  - x))
            isOdd = True
        print("")

    with open(outputPdf, "wb") as f: 
        pdfWriter.write(f)

    # closing the input pdf file object 
    pdfFileObj.close()

    print(newPages)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
