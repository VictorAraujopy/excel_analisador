# Excel Analisador

Projeto em Python para análise de vendas a partir de um arquivo Excel.

## Descrição

Este script lê um arquivo Excel (`vendas.xlsx`) contendo dados de vendas, calcula o valor total de cada venda (quantidade × preço unitário), agrupa os resultados por produto e gera um arquivo resumo (`resultados.xlsx`).

## Como usar

1. Coloque o arquivo `vendas.xlsx` na pasta do projeto.  
2. Execute o script Python:

```bash
python analisador_vendas.py
O arquivo resultados.xlsx será criado na mesma pasta, contendo o total vendido por produto.

Requisitos
Python 3.x

Bibliotecas Python:

pandas

openpyxl

Instale as dependências com:

bash
Copier
Modifier
pip install pandas openpyxl
Estrutura dos arquivos
vendas.xlsx — arquivo Excel com os dados de entrada.

analisador_vendas.py — script que realiza a análise.

resultados.xlsx — arquivo Excel gerado com o resumo.
