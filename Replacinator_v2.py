import PyPDF2 as pdf

destination = pdf.PdfFileWriter()

with open('PDF/G_58_ShubhamShaw.pdf', 'wb') as newFile:
    
    with open('PDF/Name_Page.pdf','rb') as namePage:
        pdfReader_Name = pdf.PdfFileReader(namePage)
        name = pdfReader_Name.getPage(0)
        destination.addPage(name)
        destination.write(newFile)
    
    with open('PDF/Source.pdf','rb') as source:
        pdfReader_Source = pdf.PdfFileReader(source)
        pageCount = pdfReader_Source.getNumPages()
        for i in range(1,pageCount):
            ans = pdfReader_Source.getPage(i)
            destination.addPage(ans)
            destination.write(newFile)