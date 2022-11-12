#  Image Processing Django API
This project was part of a technical interview and I decided to make it part of my portfolio!

## Goal
Create an API connected to a POSTGRESQL database that allows to download images to which to do certain processes like invert colors, change to black and white, etc.

## Instalation

1.  Clone the repository locally  `git clone https://github.com/aike-s/Image-Processing-Django-API.git` 
    
2.  Install the requirements:  `pip install -t requirements.txt`
    
3.  Set the database:  `python3 manage.py makemigrations && python3 manage.py migrate`
    
4.  Run the server:  `python3 manage.py runserver`  Click the link to see the page.
    
5.  Optionally, create superuser credentials to see the admin platform:  `python3 manage.py createsuperuser`

## Components

-   Models: 
	- Job: Download images
	- History: History of each process applied to the images
-   Views and Urls:
    -  Image: Add a new image
    -  History: Add a process to an existing image
