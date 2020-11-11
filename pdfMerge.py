
import PyPDF2

def PDFmerge(pdfs, output):
	merger = PyPDF2.PdfFileMerger()

    #Agrega PDFs uno por uno
	for pdf in pdfs:
		with open(pdf, 'rb') as f:
			merger.append(f)

	#Escribe  los pdf combinados
	with open(output, 'wb') as f:
		merger.write(f)

def main():
	# lista de PDFs
	pdfs = ['factura licuadora audifonos.pdf', 'Documento1.pdf']

    #Nombre de la salida
	output = 'nuevo.pdf'

	PDFmerge(pdfs = pdfs, output = output)

if __name__ == "__main__":
	main()
