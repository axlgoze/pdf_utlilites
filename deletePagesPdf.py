import fitz  # PyMuPDF

def eliminar_paginas(input_files, output_file, paginas_a_eliminar):
    for input_file in input_files:
        # Abre el archivo PDF
        pdf_document = fitz.open(input_file)

        # Elimina las páginas especificadas
        for pagina in sorted(paginas_a_eliminar, reverse=True):
            pdf_document.delete_page(pagina - 1)  # Las páginas se numeran desde 0, así que restamos 1

        # Guarda el PDF actualizado en un nuevo archivo
        pdf_document.save(output_file)
        pdf_document.close()

# Uso del programa
input_files = ["documento1.pdf", "documento2.pdf"]
output_file = "documento_sin_paginas.pdf"
paginas_a_eliminar = [2, 5]  # Por ejemplo, elimina la página 2 y la página 5
eliminar_paginas(input_files, output_file, paginas_a_eliminar)

