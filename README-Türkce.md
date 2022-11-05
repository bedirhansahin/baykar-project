# baykar-project
## Bu proje Baykar Teknoloji iş başvurusu için yapılmıştır


## Projede kullandığım teknolojiler:


- Django
- Docker
- Github Action
- PostgreSQL
- Django Rest Framework
- Django Rest Framework Permissions
- Django Class Based Views
- Django Model Form
- Django Pagination
- Bootstrap


## Yapabileceğiniz şeyler:


- Yeni bir kullanıcı oluşturmak
- Oluşturduğunuz kullanıcı ile giriş yapmak
- Yeni bir IHA kaydetmek
- IHAları düzenlemek, silmek ve listelemek
- Model ismine göre IHAları aramak
- Rest API sayfası için gidebileceğiniz endpointler:

    - /api/user-list/     ==> to see all users
    - /api/user/id/       ==> to see user you want
    - /api/user-create/   ==> to create a new user
    - /api/product-list/  ==> to see all UAVs
    - /api/product/id/    ==> to see UAV you want


## Projeyi Çalıştırmak İçin

Öncelikle bir klasör oluşturun ve klasör içinde bash açın.
```
git clone https://github.com/bedirhansahin/baykar-project.git
cd baykar-project
```
:warning: **Docker uygulamasını bilgisayarınıza yükleyip giriş yapmayı unutmayın:)**:

Ardından aşağıdaki komutları sırasıyla çalıştırın
```
docker build .
docker-compose build .
docker-compose run --rm app sh -c "python manage.py wait_for_db"
docker-compose run --rm app sh -c "python manage.py makemigrations core"
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
docker-compose up
```

[http://127.0.0.1:8090/](http://127.0.0.1:8090/) linkine giderek proje sayfasına ulaşabilirsiniz.

:point_up: **Admin kullanıcı oluşturmak için bu komutu kullanabilirsiniz. (docker-compose run --rm app sh -c "python manage.py createsuperuser")**
:point_up: **'İnsansız Hava Aracı', 'Silahlı İnsansız Hava Aracı' gibi IHA türleri oluşturmak için [http://127.0.0.1:8090/admin](http://127.0.0.1:8090/admin) sayfasına giriş yapın**