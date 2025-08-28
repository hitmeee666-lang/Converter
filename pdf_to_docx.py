from pdf2docx import Converter

def pdf_to_docx(pdf_file, docx_file):
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        return f"[+] Converted  {pdf_file} -> {docx_file}"
    except Exception as e:
        return f"[!] Error: {str(e)}"