import PyPDF2
import openpyxl

def extract_tables_from_pdf(pdf_path):
    tables = []
    pdf_text = ""
    
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page_num].extract_text()
    
    # Assume que cada linha está separada por uma quebra de linha
    lines = pdf_text.split('\n')
    
    for line in lines:
        table_row = line.split()  # Dividir a linha em colunas
        tables.append(table_row)
    
    return tables

def export_to_excel(tables, excel_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    for table_row in tables:
        sheet.append(table_row)  # Adicionar cada linha como uma nova linha na planilha
        
    workbook.save(excel_path)

if __name__ == '__main__':
    pdf_path = 'lista.pdf'  # Substitua pelo caminho do seu arquivo PDF
    excel_path = 'tabela.xlsx'    # Substitua pelo caminho desejado para o arquivo Excel
    
    extracted_tables = extract_tables_from_pdf(pdf_path)
    export_to_excel(extracted_tables, excel_path)
