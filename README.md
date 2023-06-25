# FT9JA Stock Trading Application
This repository contains the source code for FT9JA Task.
The project is built using Django, MongoDB, Celery and Django Channels.

## Features
* User Management
  * Registration
  * Login
* Stock Trading Simulation
  * Celery: For profit/loss generation
  * Real time communication using Websocket and Django Channels
* Stock & User Management by Admin

## Project SetUp

Clone the project and navigate into the project directory.
```bash
git clone https://github.com/SirDamis/stock-trade-ft9ja.git

cd Django-Ewallet
```
If you don't have the virtual environment installed, enter this command in your command line
```bash
pip install virtualenv
virtualenv venv
```

Activate the virtual environment
```bash
source venv/bin/activate
```


Install the dependencies.

```bash
pip install -r requirements.txt
```

Migrate the database using the command

```bash
python manage.py migrate
```
Create your copy of the env file from the.env.example file and fill the credentials
```
cp .env.example .env
```


Start the server and run the local development application using the command
```bash
python manage.py runserver
```

The development server will be open at http://127.0.0.1:8000/

## Live URL
Click this [link](/schema/swagger-ui/) to access the project link.
