:us:

## About the project

This project is part of the larger **Inteli.gente** initiative of the **Brazilian Ministry of Science and Tech (MCTI)** and of **IARA Data Science** research project, supported by the **São Paulo State Research foundation (FAPESP)**, and aims to **provide a backend for the interactive dashboard with the Inteli.gente plataform data**.


## How to locally run the project

To run the project, you need to install PostgreSQL, create a database, and execute the commands contained in the file _moc_data/moc.sql_. You should also create a _.env_ file in the root directory and provide the database access details, following the template below:

```
DB_USER = "<username>"
DB_PASSWORD = "<user-password>"
DB_NAME = "<database-name>"
DB_PORT = "<postgres-port>"
```
Once that’s done, follow the steps below to run the project.

1) Clone the repository:
```bash
git clone https://github.com/projeto-inteli-gente/backend.git
```

2) Enter the cloned project repository:
```bash
cd backend
```

3) Create a virtual environment:
```bash
python3 -m venv venv
```

4) Activate the virtual environment:
```bash
source venv/bin/activate
```

5) Install the dependencies:
```bash
pip install -r requirements.txt
```

6) Run the project:
```bash
uvicorn app:app --reload
```

:brazil:

## Sobre o projeto

Esse projeto é parte da iniciativa **Inteli.gente** do **Ministério de Ciência, Tecnologia e Inovação (MCTI)** e do **IARA Data Science**, com apoio da **FAPESP**, e visa **desenvolver o backend para o dashboard interativo com os dados da plataforma** Inteli.gente.

## Como executar o projeto localmente

Para executar o projeto, deve-se instalar o PostgreSQL, criar uma base de dados e executar os comandos contidos no arquivo _moc_data/moc.sql_. Crie também um arquivo _.env_ no diretório raíz e informe os detalhes para acesso ao banco de dados, seguindo o modelo abaixo:

```
DB_USER = "<nome-usuario>"
DB_PASSWORD = "<senha-usuario>"
DB_NAME = "<nome-basedados>"
DB_PORT = "<porta-postgres>"
```

Feito isso, siga os passos abaixo para executar o projeto.

1) Clone o repositório:
```bash
git clone https://github.com/projeto-inteli-gente/backend.git
```

2) Entre no repositório clonado:
```bash
cd backend
```

3) Crie um ambiente virtual:
```bash
python3 -m venv venv
```

4) Ative o ambiente virtual:
```bash
source venv/bin/activate
```

5) Instale as dependências:
```bash
pip install -r requirements.txt
```

6) Execute o projeto:
```bash
uvicorn app:app --reload
```