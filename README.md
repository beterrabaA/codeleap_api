# CodeLeap API

Este é o README para o projeto **CodeLeap API**. Aqui você encontrará informações sobre as rotas disponíveis e instruções para iniciar o projeto utilizando o `docker-compose.yaml`.

## Rotas da API

### **Posts**

- **POST** `/`  
    Cria um novo post.  
    **Body:**  

    ```json
    {
        "username": "string",
        "title": "string",
        "content": "string"
    }
    ```

- **GET** `/`  
    Lista todos os posts.

- **DELETE** `/{id}/`  
    Remove um post.

- **PATCH** `/{id}/`  
    Atualiza os dados de um post.  
    **Body:**  

    ```json
    {
        "title": "string",
        "content": "string"
    }
    ```

## Instruções para iniciar o projeto

### Clonando o projeto

1. Clone o repositório do projeto:

    ```bash
    git clone https://github.com/seu-usuario/codeleap_api.git
    ```

### Criando um Ambiente Virtual com o venv

1. Navegue até o diretório do projeto:

     ```bash
     cd /codeleap_api
     ```

2. **Crie o Ambiente Virtual**

     Use o comando python -m venv nome_do_ambiente para criar um ambiente virtual com o nome desejado. Substitua nome_do_ambiente pelo nome que você escolher para o ambiente virtual.

    ```bash
    python -m venv meu_ambiente_virtual
    ```

3. **Ative o Ambiente Virtual**

    Dependendo do seu sistema operacional, o comando para ativar o ambiente virtual varia:

    3.1. No Windows:

    ```bash
    meu_ambiente_virtual\Scripts\activate
    ```

    3.2. No macOS e Linux:

    ```bash
    python -m venv meu_ambiente_virtual
    ```

Você verá o nome do ambiente virtual atual no prompt do terminal, indicando que o ambiente foi ativado com sucesso.

### Docker

1. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

2. Inicie os serviços definidos no arquivo `infra/compose.yaml`:

     ```bash
     docker compose -f infra/compose.yaml up -d
     ```

### Inicializando o banco de dados

1. Inicie o processo de migração com o comando:

    ```bash
    python manage.py migrate
    ```

### Inicializando o servidor da API

1. Inicie a API rodando o comando:

    ```bash
    python manage.py runserver
    ```

2. Acesse a API em `http://localhost:8000`.

## Variáveis de Ambiente

Existe um arquivo `.env.example` que serve como um modelo para o arquivo `.env` que será usado em produção ou desenvolvimento. Por exemplo:

```env
POSTGRES_HOST= // Host do banco de dados.
POSTGRES_PORT= // Porta do banco de dados.
POSTGRES_DB= // Nome do banco de dados.
POSTGRES_USER= // Usuário do banco de dados.
POSTGRES_PASSWORD= // Senha do banco de dados.
```
