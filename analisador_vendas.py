import pandas as pd


#le o arquivo do excel
df = pd.read_excel(r"C:\Users\vicit\Desktop\excel_analisador\vendas.xlsx")

#calcula o valor total de cada venda
df["Total"] = df["Quantidade"] * df["Preço Unitário"]


#agrupa por produto e soma os totais
resumo = df.groupby("Produto")["Total"].sum().reset_index()


#salva o resultado em um novo arquivo
resumo.to_excel(r"C:\Users\vicit\Desktop\excel_analisador\resultados.xlsx", index=False)


print("Análise concluída. Veja o arquivo resultado.xlsx.")