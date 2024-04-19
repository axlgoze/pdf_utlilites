import fitz  # PyMuPDF

def rotar_pdf(input_file, output_file):
    # Abre el archivo PDF
    pdf_document = fitz.open(input_file)

    # Itera sobre cada página y rota 90 grados en sentido antihorario
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page.set_rotation(90)
    
    # Guarda el PDF rotado en un nuevo archivo
    pdf_document.save(output_file)
    pdf_document.close()

# Uso del programa
input_file = "doc1.pdf"
output_file = "rotatedFile.pdf"
rotar_pdf(input_file)

