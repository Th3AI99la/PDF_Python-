import fpdf

pdf = fpdf.FPDF()


# Adiciona uma página
pdf.add_page()

# Define a fonte como Arial em negrito tamanho 14
pdf.set_font("Arial", "B", 14)

# Define a cor de fundo da célula
pdf.set_fill_color(255, 255, 0)  # Define a cor de preenchimento como amarelo
pdf.cell(0, 10, "Célula com fundo amarelo", 1, 1, 'C', 1)



# Personaliza o alinhamento da célula
pdf.cell(0, 10, "Texto centralizado", ln=True, align='C')
pdf.cell(0, 10, "Texto alinhado à direita", ln=True, align='R')
pdf.cell(0, 10, "Texto alinhado à esquerda", ln=True, align='L')


# Adiciona um bloco de texto na célula
pdf.cell(100, 10, "Olá, mundo")



# Salva o documento em um arquivo PDF
pdf.output("document.pdf")
