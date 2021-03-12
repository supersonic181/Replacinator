import PyPDF2 as pdf

try:
    namePage = open('PDF/Name_Page.pdf','rb')
    source = open('PDF/Source.pdf', 'rb')
    
    pdfReader_Name = pdf.PdfFileReader(namePage)
    pdfReader_Source = pdf.PdfFileReader(source)
    pageCount = pdfReader_Source.getNumPages()
    
    destination = pdf.PdfFileWriter()
    
    name = pdfReader_Name.getPage(0)
    destination.addPage(name)
    
    for i in range(1,pageCount):
        ans = pdfReader_Source.getPage(i)
        destination.addPage(ans)
          
    newFile = open('PDF/G_58_ShubhamShaw.pdf', 'wb')
    destination.write(newFile)

finally:
    namePage.close()
    source.close()
    newFile.close()
