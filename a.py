import PyPDF2
import pandas as pd

def extract_table_from_pdf(pdf_path):
    pdf_text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page_num].extract_text()
    return pdf_text

pdf_text = extract_table_from_pdf('Pasta1.pdf')
print(pdf_text)

table_rows = pdf_text.split('\n')

data = []
for row in table_rows:
     row_data = row.split()  
     data.append(row_data)

df = pd.DataFrame(data)
print(df)

excel_path = 'Novo.xlsx'
df.to_excel(excel_path, index=False, header=True) 