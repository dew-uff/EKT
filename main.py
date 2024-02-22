# Este projeto calcula a medida de distancia tau de kendall e a distancia tau de kendall extendida, generalizada para
# listas ordenadas de qualquer tamanho


# O primeiro script: INSERT_RESUME procede a limpeza dos arquivos .txt fornecidos e a conversão destes em estatísticas sumarizadas.
# Depois, converte as estatísticas sumarizadas de cada arquivo em um resumo por linha no excel com as listas
# ordenadas em ordem crescente de frequencia das letras encontradas nos arquivos de texto.

# O terceiro script: FUNCTIONS tem as definições da função tau de kendall e a função tau de kendal expandida.
# Neste scrip também temos a forma optimizada para O(nlog n) da contagem de movimentos do algoritmo bubble sort.

# O quarto scrip: MATRIX faz a leitura do arquivo de resumo para o calculo das distancias tau de kendall e tau de kendall expandida.
# Neste script também há um tratamento para remoção de valores não comuns no cálculo tau de kendall.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# STEP 1
# Using the process_folder function - data clean and primary statistics.


# Assuming ekt and common_elements are defined in FUNCTIONS.py


from FUNCTIONS import *

# STEP 1
# Process folder containing texts, processing data cleaning and calculating statistics in each folder


process_folder('ES')
process_folder('PT')
process_folder('IN')
process_folder('IT')
process_folder('AL')

# STEP 2
# Using the aggregate function (data resume in all listed folders).
# Aggregate statistics present in all folders.
# Table 2 is obtained here.

aggregate('ES', 'PT', 'IN', 'IT', 'AL')

# STEP 3
# Filling Excel matrix for KT and EKT data. Sheet2 is prepared for statistics calculation.
# Table 4 and Table 5 is obtained here.

matrix('overall_summary.xlsx', 'outputekt.xlsx', 'outputkt.xlsx')


# STEP 4
# Calculated Statistics.
# Copy data from outputkt.xlsx and outputekt.xlsx to outputkt_form.xlsx and outputekt_form.xlsx
# Data for Table 6, Table 7 and Table 8 is obtained here.

calculate_statistics('outputkt_form.xlsx', 'StatsKT.xlsx', pairs)
calculate_statistics('outputekt_form.xlsx', 'StatsEKT.xlsx', pairs)


# For generate Table 9, "D Cohen and abs results from StatsEKT and StatsKT.xlsx" was prepared with data
# from "StatsKT.xlsx" and "StatsEKT.xlsx" and Wilcoxon one-tailored test was performed on the data.
