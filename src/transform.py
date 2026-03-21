import pandas as pd
import os

def limpar_pasta_anp(pasta_entrada, pasta_saida):
    # cria pasta de saída
    os.makedirs(pasta_saida, exist_ok=True)

    # lista todos os arquivos da pasta
    arquivos = os.listdir(pasta_entrada)

    for arquivo in arquivos:
        # só pega arquivos Excel
        if arquivo.endswith(".xls") or arquivo.endswith(".xlsx"):
            
            caminho_entrada = os.path.join(pasta_entrada, arquivo)

            try:
                # 1. ler arquivo
                df = pd.read_excel(caminho_entrada, skiprows=9)

                # 2. reset index
                df = df.reset_index(drop=True)

                # 3. remover colunas
                colunas_remover = [
                    "NÚMERO DE POSTOS PESQUISADOS",
                    "UNIDADE DE MEDIDA",
                    "DESVIO PADRÃO REVENDA",
                    "COEF DE VARIAÇÃO REVENDA"
                ]

                df = df.drop(columns=[col for col in colunas_remover if col in df.columns])

                # 4. nome do arquivo de saída
                nome_saida = arquivo.replace(".xlsx", ".csv").replace(".xls", ".csv")
                caminho_saida = os.path.join(pasta_saida, nome_saida)

                # 5. salvar CSV
                df.to_csv(caminho_saida, index=False, encoding="utf-8-sig", sep=";")

                print(f"OK: {nome_saida}")

            except Exception as e:
                print(f"ERRO em {arquivo}: {e}")


limpar_pasta_anp(
    "dados_brutos_2026",
    "dados_tratados_2026"
)