# curelink-newsletter-api
A REST api written in Django for people who want to get emails about topics they like. users just have to subscribe using their email and select topics they like and they will start recieving fabulous content.
There is also apis to add topics and post contents on those topics , schedule those content at specific time and they will automatically sent to all the users subscribed with given topic.

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs
* [celery](https://docs.celeryq.dev/en/latest/index.html): Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/gargharshit567/curelink_newsletter_app.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd curelink_newsletter_app
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirement.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/auth/
        
    ```
    For api documentation 

    ```
        http://localhost:8000/docs
        http://localhost:8000/playground
        
    ```
* #### For celery
    Fistly make sure your redis server is running
    Run the celery worker using this one simple command:
    ```bash
        $ celery -A curelink worker -l info
    ```
    You can now watch the worker recevieng email requests
