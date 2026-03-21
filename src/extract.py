import requests
from bs4 import BeautifulSoup
import os

def baixar_mais_recente(url, pasta_destino):
    os.makedirs(pasta_destino, exist_ok=True)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links_validos = []

    # pega todos os links
    for link in soup.find_all("a", href=True):
        href = link["href"]

        #  filtro REAL que funciona
        if "resumo_semanal_lpc" in href and "2026" in href:
            
            if not href.startswith("http"):
                href = "https://www.gov.br" + href

            links_validos.append(href)

    # debug (pra você ver se achou algo)
    print("Links encontrados:", len(links_validos))

    if not links_validos:
        print(" Nenhum link encontrado")
        return

    # ordena (mais recente por último)
    links_validos.sort()

    ultimo_link = links_validos[-1]
    nome_arquivo = ultimo_link.split("/")[-1]

    caminho = os.path.join(pasta_destino, nome_arquivo)

    if os.path.exists(caminho):
        print("Arquivo já existe:", nome_arquivo)
    else:
        print("Baixando:", nome_arquivo)

        arquivo = requests.get(ultimo_link)
        with open(caminho, "wb") as f:
            f.write(arquivo.content)

        print(" Download concluído")


# USO
url = "https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia/precos/levantamento-de-precos-de-combustiveis-ultimas-semanas-pesquisadas"

baixar_mais_recente(url, "dados_brutos_2026")