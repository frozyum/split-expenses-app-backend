### Split Expenses App Backend
App for splitting expenses

### How to run the project for development on ubuntu:
1. Update packages: `sudo apt-get update`
2. Install `libpq-dev`: `sudo apt-get install libpq-dev`
3. Install dependencies: `pip install -r requirements.txt`
4. Start server: `python manage.py runserver`

### How to run the project for development in Docker:
1. Install Docker
2. Build image: `docker build -t splitexpenses .`
3. Start database and server: `docker-compose up
4. Start only database: `docker-compose -f docker-compose-database.yml up`

### Technologies used:
* Python 3
* Django
* Docker/Docker-Compose
* Travis CI/CD

### Authors:
* Sandro Mamukelashvili smamu13@freeuni.edu.ge
* Konstantine Dvalishvili cdval13@freeuni.edu.ge 