# CodeLeap API

This is the README for the **CodeLeap API** project. Here you will find information about the available routes and instructions to start the project using `docker-compose.yaml`.

## API Routes

### **Posts**

- **POST** `/`  
    Creates a new post.  
    **Body:**  

    ```json
    {
        "username": "string",
        "title": "string",
        "content": "string"
    }
    ```

- **GET** `/`  
    Lists all posts.

- **DELETE** `/{id}/`  
    Deletes a post.

- **PATCH** `/{id}/`  
    Updates a post's data.  
    **Body:**  

    ```json
    {
        "title": "string",
        "content": "string"
    }
    ```

## Instructions to Start the Project

### Cloning the Project

1. Clone the project repository:

    ```bash
    git clone https://github.com/your-username/codeleap_api.git
    ```

### Creating a Virtual Environment with venv

1. Navigate to the project directory:

     ```bash
     cd /codeleap_api
     ```

2. **Create the Virtual Environment**

     Use the command `python -m venv <environment_name>` to create a virtual environment with the desired name. Replace `<environment_name>` with the name you choose for the virtual environment.

    ```bash
    python -m venv my_virtual_env
    ```

3. **Activate the Virtual Environment**

    Depending on your operating system, the command to activate the virtual environment varies:

    3.1. On Windows:

    ```bash
    my_virtual_env\Scripts\activate
    ```

    3.2. On macOS and Linux:

    ```bash
    source my_virtual_env/bin/activate
    ```

You will see the name of the current virtual environment in the terminal prompt, indicating that the environment has been successfully activated.

### Docker

1. Ensure that Docker and Docker Compose are installed on your machine.

2. Start the services defined in the `infra/compose.yaml` file:

     ```bash
     docker compose -f infra/compose.yaml up -d
     ```

### Initializing the Database

1. Start the migration process with the command:

    ```bash
    python manage.py migrate
    ```

### Starting the API Server

1. Start the API by running the command:

    ```bash
    python manage.py runserver
    ```

2. Access the API at `http://localhost:8000/`.

## Environment Variables

There is a `.env.example` file that serves as a template for the `.env` file to be used in production or development. For example:

```env
POSTGRES_HOST= // Database host.
POSTGRES_PORT= // Database port.
POSTGRES_DB= // Database name.
POSTGRES_USER= // Database user.
POSTGRES_PASSWORD= // Database password.
```
