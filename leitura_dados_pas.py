import PyPDF2
import re

# caminho_pdf = input("Caminho do arquivo .pdf: ")

caminho_pdf = "C:\\Users\\GamerDainez\\Desktop\\Projeto Python\\dados asafe-142-419.pdf"
pdf_file = open(caminho_pdf, 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
print(f"Qnt de páginas: {number_of_pages}")

conteudoPDF = [""]

for i in range(0, 2):  # number_of_pages):
    dadosPDF = read_pdf.getPage(i)
    dadosPDF = dadosPDF.extractText()
    dadosPDF = "".join(dadosPDF)
    dadosPDF = re.sub('\n', '', dadosPDF)
    lista = list(dadosPDF.split())
    lista.pop(0)
    conteudoPDF += lista


# num = conteudoPDF.index("DARCY")
# for _ in range(0, num-1):
#     del conteudoPDF[0]

strPDF = " ".join(conteudoPDF)

print(strPDF)
