import pdftables_api

conversion = pdftables_api.Client("lista.pdf")

conversion.xlsx("pasta1.pdf", "teste3.xlsx")