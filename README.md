# 🐍 PythonAI
[🇧🇷 Versão em Português](./README.md) | [🇺🇸 English Version](./README_EN.md)

Aplicação de exemplo da utilização do **Python** para consumir a **API do Google Gemini** e
responder perguntas em linguagem natural.\
O projeto segue boas práticas de **POO** e utiliza **variáveis de
ambiente** para proteger a chave da API.

------------------------------------------------------------------------

## 🚀 Requisitos

-   Python **3.10+**
-   Ambiente virtual configurado (recomendado)\
-   Dependências instaladas via **pip**

------------------------------------------------------------------------

## 📦 Instalação

Clone este repositório:

``` bash
git clone https://github.com/diegonegretto/python_ai.git
cd python_ai
```

Crie e ative um ambiente virtual:

``` bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Instale as dependências:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔑 Configuração da chave da API

Crie um arquivo `.env` na raiz do projeto baseado no modelo
`.env.example`:

``` bash
cp .env.example .env
```

Abra o `.env` e insira sua chave da API:

``` env
API_KEY=sua_chave_aqui
```

------------------------------------------------------------------------

## ▶️ Execução

Para rodar a aplicação:

``` bash
python main.py
```

Você verá um menu no terminal com as opções para interagir com a IA.

------------------------------------------------------------------------

## 📂 Estrutura do projeto

    python_ai/
    │── ai_client.py      # Classe PythonAI que se conecta à API
    │── main.py           # Classe Aplicacao com o menu principal
    │── .env              # Contém sua chave da API (NÃO versionar)
    │── .env.example      # Modelo para variáveis de ambiente
    │── .gitignore        # Ignora arquivos sensíveis
    │── requirements.txt  # Dependências do projeto

------------------------------------------------------------------------
