# importing required modules
import PyPDF2

def PDFmerge(pdfs, output):
	merger = PyPDF2.PdfFileMerger()

	# appending pdfs one by one
	for pdf in pdfs:
		with open(pdf, 'rb') as f:
			merger.append(f)

	# writing combined pdf to output pdf file
	with open(output, 'wb') as f:
		merger.write(f)

def main():
	# pdf files to merge
	pdfs = ['8vo.pdf', '10BACO.pdf']

	# output pdf file name
	output = 'combinado.pdf'

	# calling pdf merge function
	PDFmerge(pdfs = pdfs, output = output)

if __name__ == "__main__":
	# calling the main function
	main()
