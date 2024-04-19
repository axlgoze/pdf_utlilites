import PyPDF2

def unir_pdf(pdf_files, output_file):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open(output_file, 'wb') as output:
        pdf_writer.write(output)

# Uso del programa
pdf_files = ["doc1.pdf", "doc2.pdf"]
output_file = "mergedFile.pdf"
unir_pdf(pdf_files, output_file)

