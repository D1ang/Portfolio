# Portfolio

[![Build Status](https://app.travis-ci.com/D1ang/Portfolio.svg?branch=master)](https://app.travis-ci.com/D1ang/Portfolio)

![Design](https://github.com/D1ang/Portfolio/blob/master/mockups/presentation.png)

In order to have a place on the net to promote my projects this portfolio is created.
The main goal of this portfolio is to promote my skills as a full stack developer.
For the visitors I would like to provide an easy to understand and clear overview of projects.

In short:

- A system for myself to maintain the portfolio site with the least effort.
- An easy to navigate site for visitors.

## Demo

A live demo version can be found **[here](https://heydjang.com/)**

## Table of Contents

- [Portfolio](#portfolio)
  - [Demo](#demo)
  - [Table of Contents](#table-of-contents)
  - [UX](#ux)
  - [User stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Surface](#surface)
    - [Skeleton](#skeleton)
  - [Technologies](#technologies)
    - [JavaScript Libraries](#javascript-libraries)
    - [Python & Django Libraries](#python--django-libraries)
  - [Features](#features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Testing](#testing)
  - [Bugs](#bugs)
    - [CSS](#css)
    - [JavaScript](#javascript)
  - [Deployment](#deployment)
    - [Deploy requirements](#deploy-requirements)
    - [Local deployment](#local-deployment)
    - [Heroku deployment](#heroku-deployment)
    - [Content](#content)

## UX

To make the portfolio as clear as possible to the end-user, a basic but very clean design has been chosen.
Options are minimalistic and the end-user will not be overloaded with options to choose from.

## User stories

With years of experience, I have built a well-known form and work ethic in creating designs.
For my presonal preference a sample has been build with the following points:

- As a visitor, I want to easily fill in the form to contact the site owner
- As a visitor, I do not want to be overloaded with info
- As a visitor, I want a overview of all the build projects by this dude
- As a visitor, I want to know who build these projects
- As an admin, I want to have an easy to manage portfolio page
- As an admin, I want to update page info with ease
- As an admin, I want a nice looking dashboard to manage the portfolio
- As an admin, I would like to easily extend this portfolio

### Strategy

The goal of the system is to make it as easy as possible to access, short and informative,
while striving for a minimalist and user-friendly design.

### Scope

For visitors, I wanted to provide them with an easy to understand (first-view-use) portfolio.

### Structure

The system is structured to get the right information as quickly as possible.
The order of the options provided are placed in a logic workflow while the design provided will use a messages bar
that should be easy to understand and gives the visitor a straight away no-nonsense feedback.

### Surface

The colours chosen are darkish and spacey as space is the theme for this portfolio.
A very clean and abstract design has been chosen to force the attention to the systems functionality.
Users will not be afraid to use the system by this easy to understand design.

### Skeleton

For this project there is no skeleton available, as I build it on the go right from the brain.

## Technologies

- HTML - *To create the basics*
- CSS - *To improve placements and design*
- JavaScript - *The engine to create user interaction*
- Python - *Programming language*
- Postgres - *Opensource database to save the transactions, profile, and orders*
- Django - *Web framework in python*
- Bootstrap - *To make the design responsive*
- Font Awesome - *Easy icon access for the icons*

### JavaScript Libraries

- jQuery - *To improve input field feedback*
- Slick - *the last carousel you'll ever need*
- Normalize.css - *A modern, HTML5-ready alternative to CSS resets*

### Python & Django Libraries

- pillow - *Python Imaging Library*
- django-crispy-forms - *Controls the rendering behaviour of Django forms*
- django-jazzmin - *Bootstrap 4 django admin interface*
- whitenoise - *Radically simplified static file serving for Python web apps*

## Features

This webapp is an portfolio based website with a simplistic but easy to understand build-up.
Providing the user with 2 call-to-action buttons, a choice can be made in seconds.
Some YouTube videos are shown as linked images and can be pressed.
Projects are shown with an additional text, an image and 2 buttons.
A contact is provided at the bottom of the page.

### Features Left to Implement

In later releases I would like to connect the page to the GitHub & YouTube api to automate some processes.
I would like to build A cleaner and more animated layout with Tailwind or React. On top of that some
blog functionality would be nice...

## Testing

This system was tested across multiple screen sizes on Chrome, Brave & Safari
To ensure compatibility and responsiveness it is also tested on an android based mobile device (OnePlus5)
The system has been field-tested by friends, colleagues and family.
Some basic unit testing has been done with Travis and own written testcodes on the home app.
Unit testing does not go as deep as the field tests, but does show that the bare basic functions are working correctly.

The following tests have been used to ensure proper site functionality:

- [GTmetrix](https://gtmetrix.com/): To test on website loading times.
- [W3C HTML Validator](https://validator.w3.org/): This validator checks the mark-up validity of Web documents in HTML.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): This validator checks the mark-up validity of Web documents in CSS.
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB): Inspecting on overflow errors.
- [Autoprefixer CSS online](https://autoprefixer.github.io/): Autoprefixer is a PostCSS plugin which parses your CSS and adds vendor prefixes.
- [JSHint](https://jshint.com/): A static code analysis tool for JavaScript.
- [ES6 Syntax Check](https://www.piliapp.com/syntax-check/es6/): An online ECMAScript 6 Checker.
- [Visual Studio Code](https://code.visualstudio.com/): Using the built-in tools to test on proper code, like flake8 linter.
- [Travis](https://travis-ci.org/): Used halfway the project to test the code.

## Bugs

### CSS

CSS written code is tested with the W3C CSS Validator.
As it does not give any problems, the deployed version of the site does gives a couple of warnings and errors coming
from Bootstrap.

### JavaScript

All 3 JavaScript’s in this system passed the test, only a couple of warnings came up through JSHint, for example: using "let", "const" but none of them are bug worthy.
By using "ES6 Syntax Check" all the Syntax checks passed.

## Deployment

The code of this system is hosted by using Heroku, this code is deployed to GitHub directly from the master branch.
The deployed site will update automatically upon new commits to the master branch.
This code can be run locally or deployed to a live environment. Directions are based on deployment locally and to Heroku.

### Deploy requirements

- [VScode](https://code.visualstudio.com/) *A tool/IDE to develop software*
- [python 3](https://www.python.org/) *A programming language*
- [PIP](https://pip.pypa.io/en/stable/installing/) *To get python installation packages*
- [Git](https://github.com/) *Version control for code source*

### Local deployment

1. Download a copy of the GitHub repository by clicking the "Code" button at the top right of the
   GitHub page and in the submenu select "Download ZIP". Extract the zip file to a folder of choice on your system. If Git is installed on your system,
   you can clone the repository with the following command:

   ```bash
   git clone https://github.com/D1ang/Portfolio.git
   ```

1. Open the unzipped folder in your preferred IDE (in this example we are using VScode)
   Open up a terminal session and set up a virtual environment with these commands in the terminal session:

   ```bash
   pip install virtualenv
   ```

   >If you already have virtualenv installed from a different project, then this step is not needed. The pip command may differ per system this can be pip or pip3.

   ```bash
   virtualenv env
   ```

   >Your command may differ to the IDE you are using, such as ```python -m .venv venv ...``` or ```py manage.py ...```
  
   Activate the .env with the command:

   ```bash
   env\Scripts\activate
   ```

   >This command may differ depending on your operating system, please check the Python documentation on creating an ENV.

1. Install all required django modules with the command:

   ```bash
   pip install -r requirements.txt
   ```

1. Create a new file at the base directory level called env.py and copy the following into the created env.py file:

   ```bash
   import os

   os.environ.setdefault('DEVELOPMENT', 'True')
   os.environ.setdefault('SECRET_KEY', 'your_value')
   os.environ.setdefault('RECAPTCHA_PUBLIC_KEY', 'True')
   os.environ.setdefault('RECAPTCHA_PRIVATE_KEY', 'True')
   ```

   Replace <your_value> with the values from your own created accounts:
   - [SECRET_KEY](https://djecrety.ir/) *Required from an online key generator*

1. Set up the databases by running the following management command in your terminal:

   ```python
   python manage.py migrate
   ```

1. Create a superuser so you can have access to the django admin by running the following command in your terminal:

   ```python
   python manage.py createsuperuser
   ```

1. Now that the server is running, we need to add the required data into the database in the following order:

   ```python
   python manage.py loaddata groups.json
   python manage.py loaddata customers.json
   python manage.py loaddata itemtags.json
   python manage.py loaddata items.json
   ```

1. Finally start your server by running the following management command in the terminal:

   ```bash
   python manage.py runserver
   ```

   If everything went correctly the terminal will provide a message telling that the development server is running
   at a provided URL mostly:  `http://127.0.0.1:8000/`

### Heroku deployment

To run this application in a cloud-based environment, you can deploy the code to Heroku. This section assumes you have succeeded at running the application in your local environment first, as described above.

1. Login to Heroku and set up a new app with an unique name NOTE: heydjang is already taken :smile:
1. On the Resources tab, in the Add-ons field type Heroku Postgres select the Hobby Dev then click the Provision button.
1. After setting the Postgress database go back to the Settings tab and click Reveal Config Vars. Copy the values from your env.py file into Heroku. Make sure you load the following:

    |:          Key           |:     Value     |
    |:------------------------|:---------------|
    | DATABASE_URL            |  <your_value>  |
    | SECRET_KEY              |  <your_value>  |
    | RECAPTCHA_PUBLIC_KEY    |  True          |
    | RECAPTCHA_PRIVATE_KEY   |  True          |
    | DEVELOPMENT             |  False         |

    Grab the DATABASE_URL link from Heroku's Config Vars as we gonna need it later to migrate
    to the Heroku Postgres database.

1. Now that the database on Heroku is created the following rule needs to be added to the env.py file

   ```bash
   os.environ.setdefault('DATABASE_URL', '<your postgres url grabbed from Heroku>')
   ```

   >Be assured to not share this URL with anybody.

1. Because this is a new database connection, the migrate command must be executed with the following command in your terminal:

   ```bash
   python manage.py migrate
   ```

   >Do not forget to reactivate your virtual environment if the system or IDE is rebooted.

1. Create the superuser for the postgres database so you can have access to the django admin.

   ```bash
   python manage.py createsuperuser
   ```

1. Now we need to add the required data into the database in the following order:

   ```python
   python manage.py loaddata projects.json
   python manage.py loaddata videos.json
   ```

1. With everything set push the code to a GitHub account of yourself:

   ```bash
   git init
   git commit -m 'getting ready to deploy to Heroku'
   git push -u origin
   ```

1. From the Heroku dashboard of your newly created application, click on the "Deploy" tab, then scroll down to the "Deployment method" section and select GitHub.

1. Use the GitHub link and type in the name of the repository and click the search button. Then connect the Heroku app to the desired GitHub repository.

1. On the Deployment Tab, scroll a bit further down to the "Manual Deploy" section, select the master branch then click "Deploy Branch".

1. Once your application is running, you may want to update the Deployment method from Manual to Automatic.

1. From the Heroku dashboard select the Open app button on the top right.

### Content

All text content for this system were written by me.
