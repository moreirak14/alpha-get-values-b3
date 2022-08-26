# Alpha Vantage Invest
O objetivo do sistema é auxiliar um investidor nas suas decisões de comprar/vender ativos.
O investidor será capaz de realizar o cadastro e ter visibilidade dos seus ativos!

## Pré-requisitos

- Python 3.10+: `https://www.python.org/downloads/`
- Docker: `https://www.docker.com/`
- Poetry: `https://python-poetry.org/docs/#installation`

## Necessário

- Criar novo arquivo `.secrets.toml` e `.env`, você pode copiar o arquivo `.example.secret.toml` para `.secrets.toml` e `.env`.
  - O `secret.toml` é utilizado para aplicação;
  - O `.env` é utilizado para o docker.

- As variaveis de ambiente são: SECRET_KEY, API_KEY, EMAIL, PASSWORD.
  - SECRET_KEY (chave de autenticação projeto django);
  - API_KEY (chave de autenticação de requisição da API "https://www.alphavantage.co", a chave encontra-se aqui: "https://www.alphavantage.co/support/#api-key");
  - EMAIL (e-mail qualquer, sendo g-mail);
  - PASSWORD (processo de geração da senha na conta g-mail para apps: Gerenciamento de conta > Segurança > Senhas de app > Gerar senha).

- Será necessário clonar o repositorio "https://github.com/moreirak14/alpha-get-values-b3-web" da pagina web (frontend) e seguir o procedimento de execução.

## Utilização em desenvolvimento local
O arquivo `Makefile` que existe na raiz do projeto, tem todos os comandos mapeados, desde a construção até os testes.

- Para instalar todos os pacotes necessários e criar um ambiente virtual:
`$ poetry shell` ou `$ poetry install` ou `$ make setup`

- Para subir as migrações de database:
`$ python manage.py migrate` ou `$ make migrate`

- Para gerar uma nova migração de database:
`$ python manage.py makemigrations` ou `$ make makemigrations`

- Para executar a aplicação:
`$ python manage.py runserver` ou `$ make run`
