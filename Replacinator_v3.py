try:    
    import PyPDF2
except:
    import sys
    import subprocess

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyPDF2'])

destination = PyPDF2.PdfFileWriter()

input("Please keep both Pdfs in the same folder where replacinator.py is...\nPress any key to proceed\n")

first_pdf = input("Enter the first pdf name including .pdf: ")
second_pdf = input("Enter the second pdf name including .pdf: ")

with open('Replacinator.pdf', 'wb') as newFile:
    
    with open(first_pdf,'rb') as namePage:
        pdfReader_Name = PyPDF2.PdfFileReader(namePage)
        start,end = map(int, input("Enter the starting and ending page number you want to copy from PDF1: ").split(' '))
        start = start - 1
        for i in range(start,end):
            name = pdfReader_Name.getPage(i)
            destination.addPage(name)
            destination.write(newFile)
    
    with open(second_pdf,'rb') as source:
        pdfReader_Source = PyPDF2.PdfFileReader(source)
        pageCount = pdfReader_Source.getNumPages()
        start,end = map(int, input("Enter the starting and ending page number you want to copy from PDF2: ").split(' '))
        start = start - 1
        for i in range(start,end):
            ans = pdfReader_Source.getPage(i)
            destination.addPage(ans)
            destination.write(newFile)
            
print("File Created Successfully!!!\nFile Name: Replacinator.pdf")