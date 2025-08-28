from docx2pdf import convert

def docx_to_pdf(docx_file, pdf_file):
    try:
        convert(docx_file, pdf_file)
        return f"[+] Converted {docx_file} -> {pdf_file}"
    
    except Exception as e:
        return f"[!] Error: {str(e)}"
