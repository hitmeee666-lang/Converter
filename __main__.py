import docx_to_pdf 
import pdf_to_docx


print("\nDocument Converter")
print("[1] PDF to DOCX")
print("[2] DOCX to PDF")
print("[3] Close")

choice = input("Choose an option:")

if choice == "1":
    pdf = input("Enter PDF file path:")
    docs = input("Enter output Docx file path:")
    result = pdf_to_docx.pdf_to_docx(pdf, docs)
    print(f"Conversion Complete:  {result}")
    
elif choice == "2":
    docx = input("Enter Docx file path:")
    pdf = input("Enter output PDF file path:")
    result = docx_to_pdf.docx_to_pdf(docx, pdf)
    print(f"Conversion Complete: {result}:")

elif choice == "3":
    print("Closing program...")

else:
    print("Invalid option, try again.")
