# Event Registration -
#### Designing and building a REST API for Event Registration


### Technology Stack :
Django Rest Framework



### Install the dependencies 

Create a new Virtual Environment and activate it
Then install the required libraries

```sh
$ pip3 install requirements.txt
```




### Run the Project

```sh
$ python3 manage.py makemigrations events
$ python3 manage.py migrate
$ python3 manage.py runserver
```

#### This project covers the following task : 
Users can create events
Users can limit the number of attendees
Users can delete an event
Users can view public events


#### URL

Project URL : 

```sh
{
    "events": "http://127.0.0.1:8000/events/",
    "users": "http://127.0.0.1:8000/users/"
}
```
