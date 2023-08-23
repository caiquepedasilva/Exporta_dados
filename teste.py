import tabula
import pandas as pd

def extract_table_from_pdf(pdf_path, pages):
    tables = tabula.read_pdf(pdf_path, pages=pages, multiple_tables=True, lattice=True)
    return tables

pdf_path = "lista.pdf"
pages_to_extract = "1"  # Páginas que contêm a tabela

tables = extract_table_from_pdf(pdf_path, pages_to_extract)

if len(tables) > 0:
    df = tables[0]  # Supondo que a tabela esteja na primeira posição da lista de tabelas

    # Ajustar as colunas manualmente
    df.columns = ["nome", "idade", "peso", "altura", "zé ruela?", "ocupação"]

    # Preencher os dados vazios na coluna "nome" com os valores corretos
    nome_index = df.columns.get_loc("nome")
    last_name = ""
    for index, row in df.iterrows():
        if pd.notna(row["nome"]) and row["nome"].strip() == "":
            df.at[index, "nome"] = last_name
        else:
            last_name = row["nome"]

    # Salvar o DataFrame em um arquivo Excel
    excel_path = "tabela_extraida.xlsx"
    df.to_excel(excel_path, index=False)

    print("Tabela extraída e salva em", excel_path)
else:
    print("Nenhuma tabela encontrada nas páginas especificadas.")
