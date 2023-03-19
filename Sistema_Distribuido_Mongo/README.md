# Sistema Distribuído

Este projeto tem por objetivo simular um Sistema Distribuído para a disciplina de "Sistemas Distribuídos" do Centro Universitário SENAI. O projeto é executado em três terminais com diferentes portas (8000, 80001, 8002) tendo acesso aos mesmos dados inseridos no MongoDB, realizando as requisições a partir de uma rota de inserção de musicas e uma para acessar as musicas cadastradas sendo estas salvas no MongoDB.


## Configuração rápida

1. Este projeto utiliza o [Poetry](https://python-poetry.org/) para gerenciar suas dependências.
    Consulte a [documentação oficial](https://python-poetry.org/docs/#installation) para instalá-lo se ainda não o fez.
    **Este passo só precisa ser executado uma vez.**

1. **A versão utilizada do Python é a 3.10**.

  - Utilizando o [conda](https://docs.conda.io/en/latest/miniconda.html):
  - Crie um novo ambiente virtual:
    ```sh
    conda env create -f environment.yml
    ```
  - Ative o ambiente virtual:
    ```sh
    conda activate projeto-teste
    ```


1. Instale as dependências do backend:

    ```sh
    pip install "fastapi[all]"
    pip install sqlalchemy
    pip install sqlalchemy_utc
    pip install pymysql
    pip install pytest
    pip install factory-boy
    pip install requests
    pip install redis
    pip install pymongo
    ```
2. Instale o MongoDB

    É necessário instalar ou [MongoDB Community Server](https://www.mongodb.com/try/download/community), assim o MongoDB Compass funcionará corretamente.


3.  Pra Rodar o Projeto
    ```sh
    python -m uvicorn backend.main:app --reload --port=8000
    python -m uvicorn backend.main:app --reload --port=8001
    python -m uvicorn backend.main:app --reload --port=8002
    ```
4.  Urls Criadas
    
    ```sh
    Url swagger Porta 8000: http://localhost:8000/api/docs/
    Url swagger Porta 8001: http://localhost:8001/api/docs/
    Url swagger Porta 8002: http://localhost:8002/api/docs/
    ```
