# baykar-project
## This project made to job apply of Baykar Technology


## Technologies I used while designing the project:


- Django
- Docker
- PostgreSQL
- Django Rest Framework
- Django Rest Framework Permissions
- Django Class Based Views
- Django Model Form
- Django Pagination


## You can:


- Create a new user
- Login with user you created
- Create a new UAV
- Update, Delete and List UAVs
- Search for UAV you want
- Visit some endpoint

    - /api/user-list/     ==> to see all users
    - /api/user/id/       ==> to see user you want
    - /api/user-create/   ==> to create a new user
    - /api/product-list/  ==> to see all UAVs
    - /api/product/id/    ==> to see UAV you want


## Download the project

First, create a folder and run
```
git clone https://github.com/bedirhansahin/baykar-project.git
cd baykar-project
```
:warning: **Don't forget install Docker desktop and create an account**:

After, run the following commands from CMD:
```
docker build .
docker-compose build .
docker-compose run --rm app sh -c "python manage.py wait_for_db"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
docker-compose up
```

and you can go to [http://127.0.0.1:8090/](http://127.0.0.1:8090/) on your own browser.

:point_up: **create a superuser with command (docker-compose run --rm app sh -c "python manage.py createsuperuser")**
:point_up: **create new types like 'İnsansız Hava Aracı', 'Silahlı İnsansız Hava Aracı' on [http://127.0.0.1:8090/admin](http://127.0.0.1:8090/admin) after logging in**