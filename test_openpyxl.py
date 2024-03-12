from openpyxl import load_workbook

wb = load_workbook(filename='planilha.xlsx')
sheet = wb.active

# Acessando uma célula específica
cell_value = sheet['A2'].value

print("\n Printando apenas a célula A1 - Guardada na variável cell_value ")
print(cell_value, "\n")

# Iterando sobre todas as células em uma coluna
print("\n Printando nomes da planilha na tela: ")
for cell in sheet['A']:
    print(cell.value)

print("\n Printando idades da planilha na tela: \n")
for cell in sheet['B']:
    print(cell.value)
    
print("\n Printando pesos da planilha na tela: \n")
for cell in sheet['C']:
    print(cell.value)
