import fitz  # PyMuPDF
import os

def rotar_pdf(input_files):
    for input_file in input_files:
        # Abre el archivo PDF
        pdf_document = fitz.open(input_file)

        # Itera sobre cada página y rota 90 grados en sentido antihorario
        for page in pdf_document:
            page.set_rotation(90)

        # Genera un nombre de archivo de salida basado en el nombre del archivo de entrada
        output_file = os.path.splitext(input_file)[0] + "_rotado.pdf"

        # Guarda el PDF rotado en un nuevo archivo
        pdf_document.save(output_file)
        pdf_document.close()

# Uso del programa
input_files = ["muestra1.pdf", "muestra3.pdf", "muestra5.pdf", "muestra2.pdf", "muestra4.pdf", "muestra6.pdf"]
rotar_pdf(input_files)

