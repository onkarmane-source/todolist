# Project Setup

To initiate the project, you must first start the server using the designated virtual environment.

## On Linux

Execute the following commands after navigating to the project directory:

```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Once the application server has started, you can begin interacting with the API.

## API Endpoints

### API Registration

**ENDPOINT** - [https://onkarmane28.pythonanywhere.com/api/auth/register/](https://onkarmane28.pythonanywhere.com/api/auth/register/)

```json
{
    "username": "",
    "password": ""
}
```

### Login and Authentication

**ENDPOINT** - [https://onkarmane28.pythonanywhere.com/api/auth/login/](https://onkarmane28.pythonanywhere.com/api/auth/login/)

```json
{
    "username": "",
    "password": ""
}
```

After successfully logging in, you can access the following endpoints:

### Retrieve All Tasks

**ENDPOINT** - [https://onkarmane28.pythonanywhere.com/api/main/](https://onkarmane28.pythonanywhere.com/api/main/)

### Create a Task

Make a POST request to the endpoint:

**Note**: Tags should be provided in a comma-separated format.

**ENDPOINT** - [https://onkarmane28.pythonanywhere.com/api/main/create/](https://onkarmane28.pythonanywhere.com/api/main/create/)

### Edit a Task

**Note**: While editing, tags should be provided in a list format.

**ENDPOINT** - [https://onkarmane28.pythonanywhere.com/api/main/{id}/](https://onkarmane28.pythonanywhere.com/api/main/{id}/)

Replace `{id}` with the respective task ID to edit.

### Delete a Task

**ENDPOINT** - [https://onkarmane28.pythonanywhere.com/api/main/delete/{id}](https://onkarmane28.pythonanywhere.com/api/main/delete/{id})

Replace `{id}` with the respective task ID to delete.
