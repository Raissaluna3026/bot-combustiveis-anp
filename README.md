# Bot de Alerta de Gasolina - ANP

🚀 Projeto em Python que automatiza o envio de alertas de preços de combustíveis via WhatsApp, usando dados da ANP.

O bot extrai os dados de planilhas da ANP, trata os dados para identificar o menor preço e envia uma mensagem com as informações do posto e localização no grupo do WhatsApp.

---

## Funcionalidades

- ✅ Extrai dados semanais de gasolina da ANP (planilhas Excel)  
- ✅ Converte e trata os dados em CSV, removendo colunas desnecessárias e normalizando nomes  
- ✅ Identifica automaticamente o menor preço de combustível por município  
- ✅ Gera mensagem com informações do posto e link do Google Maps  
- ✅ Envia a mensagem diretamente para um grupo do WhatsApp via `pyautogui`  

---

## Estrutura do Projeto

```text
bot-combustivel-anp/
├── data/
│   ├── dados_brutos_2026/          # Planilhas baixadas da ANP
│   └── dados_tratados_2026/        # CSVs tratados pelo bot
├── src/
│   ├── transform.py                 # Script de tratamento de dados
│   └── send.py                      # Script de envio da mensagem
├── README.md


