import tabula
import pandas as pd

# caminho do pdf
arquivo_pdf = 'tabela2.pdf'

# Extrai todas as tabelas de todas as páginas
tabelas = tabula.read_pdf(arquivo_pdf, pages="all", multiple_tables='False')

# Junta todas as tabelas em um único dataframe
df_final = pd.concat(tabelas, ignore_index=True)

# Salva como excel
df_final.to_excel('tabelas_unificadas22.xlsx', index=False)

# Criar lista com os valores do cabeçalho que devem ser removidos quando repetidos
cabecalho_padrao = [
    "INSCRIÇÃO", "NOME", "PORT", "MAT", "LEG", "CE", "PONTOS", "RESULTADO"
]

# lendo o arquivo excel
df = pd.read_excel('tabelas_unificadas22.xlsx')

# Remover linhas que sejam exatamente o cabeçalho repetido
df_limpo = df[~(
    (df.iloc[:, 0] == cabecalho_padrao[0]) &
    (df.iloc[:, 1] == cabecalho_padrao[1]) &
    (df.iloc[:, 2] == cabecalho_padrao[2]) &
    (df.iloc[:, 3] == cabecalho_padrao[3])
)]

# Redefinir o índice
df_limpo = df_limpo.reset_index(drop=True)

# Definir o cabeçalho como a primeira linha original
df_limpo.columns = cabecalho_padrao

# Salvar Excel limpo
df_limpo.to_excel('tabelas_final22.xlsx', index=False)

