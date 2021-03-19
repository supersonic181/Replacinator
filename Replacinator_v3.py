try:    
    import PyPDF2
except:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyPDF2'])

def valid_input_checker():
    valid_input = False
    while (valid_input == False):
            input1 = input("Enter the starting and ending page number you want to copy from PDF1: ").split(' ')
            if (len(input1) != 2) or (not input1[0].isnumeric()) or (not input1[1].isnumeric()):
                print("Please enter 2 integers.")
                valid_input = False
            else:
                valid_input = True
    start, end = int(input1[0]),int(input1[1])
    return start,end
    
destination = PyPDF2.PdfFileWriter()

input("Please keep both Pdfs in the same folder where replacinator.py is...\nPress any key to proceed\n")

first_pdf = input("Enter the first pdf name including .pdf: ")
second_pdf = input("Enter the second pdf name including .pdf: ")
final_pdf = input("Enter the final pdf name including .pdf: ")

with open(final_pdf, 'wb') as newFile:
    
    with open(first_pdf,'rb') as namePage:
        pdfReader_Name = PyPDF2.PdfFileReader(namePage)
        start,end = valid_input_checker()
        start = start - 1
        for i in range(start,end):
            name = pdfReader_Name.getPage(i)
            destination.addPage(name)
            destination.write(newFile)
    
    with open(second_pdf,'rb') as source:
        pdfReader_Source = PyPDF2.PdfFileReader(source)
        pageCount = pdfReader_Source.getNumPages()
        start,end = valid_input_checker()
        start = start - 1
        for i in range(start,end):
            ans = pdfReader_Source.getPage(i)
            destination.addPage(ans)
            destination.write(newFile)
            
print(f"File Created Successfully!!!\nFile Name: {final_pdf}")
