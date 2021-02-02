# Sipmle Django project
## Requirements
Create a basic Django project as follows:

- one single "hello_world" app

- app model based on the following database tables:

--> table_1, with fields:

----> table_1_id (int)

----> field_1 (text)

----> table_2_id (int) (one to many foreign key with table_2)


--> table_2, with fields:

----> table_2_id (int)

----> field_2 (text)


- single view with url "hello-world"
-- pull single entry from table_1 with related entries from table_2, pass to "hello_world.html" template
-- hello_world.html template to render simple text with field_1 as a header and all field_2's as a unordered list

- unit test for the single view
-- unit test needs to use the low level django db connection and a raw sql query

## Installation
> `git clone https://github.com/MITATED/simple-django.git`

> `cd simple-django`

*For python3.8 with virtualenv*
> `python3.8 -m venv venv && source venv/bin/activate`

> `pip install -r requirements.txt`

## Preparing the database

> `python manage.py migrate`

## Run
> `python manage.py runserver`

## Tests
> `python manage.py test`