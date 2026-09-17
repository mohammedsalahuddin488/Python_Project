3from PyPDF2 import PdfWriter

merger = PdfWriter()

pdf = []

n = int(input("Enter the number of PDF files you want to merge: "))

for i in range(n):
    name1 = input(f"Enter PDF {i + 1} name: ")
    pdf.append(name1)

for pdf_file in pdf:
    merger.append(pdf_file)

merger.write("merged-pdf.pdf")

merger.close()

print("PDFs merged successfully!")