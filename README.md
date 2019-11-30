[![Build Status](https://travis-ci.org/mohamedmbah2019cistudent/bah_eCommerce.svg?branch=master)](https://travis-ci.org/mohamedmbah2019cistudent/bah_eCommerce)

#  Welcome To Mohamed Marifa Bah!

# Full Stack Framework Milestone Final Project Of Code Institute.


# Project Summary

Project Purpose: In this project, I need to build a full-stack site based around business logic used to control a centrally-owned dataset. I need to set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

I have made a palm oil website where the owner displays thier hand made palm oil.They maintains a blog where they provides users tips and instructions to make Palm Oil productions.Users can also write and share their blogs here.Users can buy palm oil if they like.If they want some sweet palm oil,they can contact the owner with the details of their requirements.


# UX


This platform has been built to be fully responsive so it works perfectly on any device and screen size.

"As a customer, I would like to _______________"

view the site from any device (mobile, tablet, desktop).
get a palm oil website that can be searched by category, similar product and using text search, making it easy to find specific things or enjoy browsing categories that interest me
payment procedure should be easy to handle
have a palm oil website where I can get new food stuff.
have a palm oil website where I can get my frying oil and cooking oil

# Design

Color Scheme

Since the website sells palm oil, I chose bright, vibrant colors.

Framework

Bootstrap 4

jQuery 3.4.1

In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.

Django 1.11.24

Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap. We were taught how to use Django 1.11 in the lessons, despite Django 2.0 being the current version,I used Django 1.11

Icons

Font Awesome 

Typography

Google Fonts were used across the site.

Google images were used accross the site.


# Features

Base template (navbar & footer)

Navbar

Site logo to navigate back to homepage.

Home button to navigate back to homepage.

Login button for existing users to log back in.

Register button for new users to register. Once the user has logged in.

removal of login and register button.

Logout button to end their session.

Explore drop down to enable users to navigate the site from any html page.

Search bar enabling users to search for products via key words.

Footer

Contact form enabling users to submit contact requests.

Social media buttons which currently link homepage of the sites however would link to this websites social.

Index (homepage)

Register button which is hidden if user is already registered.

Icons which link to different parts of the site.

Products

Index page users can see all the products

Users can straight away add a product in the cart

Users can go to detailed view product to check price details and other details of the product. From detailed view page also user can add a product in the cart

Products can be searched by Categories through Navigation bar.
Profile page.

Users can check their login details here.

Contact Page

The contact page contains a form for the user to fill in to send the shop owner an email.


Name, email address, subject and message are all required fields so that the shop owner receives all the information she needs to respond.

When the user clicks "send" the email is processed and sent via emailjs to Owner’s email address and user has been notified via message.

Register Page

A user who is not logged in can create a new account using the register page. The page on this form includes a username (which must be unique), email address, password and password conformation fields.
Information about what characters are accepted by these fields is displayed with the form.
If a user who is already logged in tries to access this page, they are redirected to the home page.
After registration, user will be notified via a message.

Login Page

The login page features a standard login form asking for username and password.
Validation for this form is handled in the back end and relevant feedback is sent to the user when they sign in.
User can reset password if needed from this page.

Log out page

Any user who clicks on "Log out" from the navigation bar is automatically logged out and their session data cleared.


Cart page

The shopping cart page features a summary of all the items the user has added to their cart.
Each list item includes a picture of the item, the item title and price.
A quantity field is displayed with each cart item, giving the user the ability to adjust the quantity in their cart. Any time a quantity is adjusted the subtotal displayed is updated to reflect the change.


Checkout page

Each checkout page features an order summary, which lists all the items in the users cart, title, price and quantity.
User need to populate their details like Name, contact no., delivery address and payment card details and then submit for payment.


Blog Post Page

Since it is a handmade palm oil website, interested users can share their write ups related to palm oil making and other stuffs related to palm oil here in this Blog page.
No of views for each post will be automatically updated.
Users can view others’ blogs too.
Edit/Delete options are there for logged in users

# Features Left to Implement

In the blog post any user can edit/delete other users’ posts. I need to make it user specific so that users can only get the access to edit/delete for their own posts.
Review section for users for each product they buy.
Checkout pages to include a field for customers to enter discount codes or coupons to adjust their final payment cost.
User profile page will show more details like buying history of the user.


# Technologies Used

HTML

CSS

JavaScript

Python 3

SQL

Framework / Libraries

jQuery

Django

Font Awesome

Stripe

Bootstrap

Travis

# Tools:

Git
Databases:

SQLite

PostgreSQL

Testing
A thorough mix of automated and manual testing have gone into building the project. In addition to tests, I have validated all files against online validation sites, and checked compatibilities across various modern browsers and devices.

Automated tests
I used Travis to test my test.py files. Build Status
Validation services
I used This HTML validator to ensure my code was legal.
The only warnings were when the validator failed to recognise the Django template tags.
I used This CSS validator to ensure my CSS was legal.
Valid CSS!

I used This Python validator to ensure my Python was legal.
Stripe payment testing
Please use the below information to test payments.

Card number - 4242424242424242
CVC - Any 3 digit number.
Expiry date - Any date in the future.

# Manual tests
Check logging in and out, views change accordingly
Check registering as new user and logging in and out and in again
Check all links in navbar and footer, confirm opening in new tabs
Click 'Forgot password' and confirm email link
For the posts, no. of views for each post is getting updated
Check switching between pages
Contact Us form is working fine.
Cart is adding the products properly
Checkout function is working fine.
Check display is reasonable with reasonable resizings of browser window
Check that filtering works by confirming in the Python shell
Change things in the admin panel and try to break stuff (e.g. delete a user and then check profile removed by CASCADE)

# Deployment
How to run this project locally
To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:

An IDE such as gitpod C9
The following must be installed on your machine:

PIP 3

Python 3

Git

Instructions
Save a copy of the github repository located at https://github.com/by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
git clone https://github.com/
If possible open a terminal session in the unzip folder or cd to the correct location.

Install all required modules with the command

pip3 -r requirements.txt.
Attempt to run project where you will get an error message displaying your host name.
python3 manage.py runserver 
In your settings.py file add your hostname under 'ALLOWED_HOSTS'.

Create a stripe account and get your API keys.

In your local IDE create a file called env.py.

Inside the env.py file create the below variables.

SECRET_KEY

STRIPE_PUBLISHABLE

STRIPE_SECRET

DEFAULT_FROM_EMAIL

SERVER_EMAIL

EMAIL_HOST

EMAIL_HOST_USER

EMAIL_HOST_PASSWORD

You can now re-run the runserver command to view local project.

python3 manage.py runserver 
Note - If you are having issues viewing static files you may need to collect static with the below command.
python3 manage.py collectstatic
Heroku Deployment
To deploy Creative Jewelry to heroku, take the following steps:

Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

Create a Procfile with the terminal command echo web: python app.py > Procfile.

git add and git commit the new requirements and Procfile and then git push the project to GitHub.

Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

Confirm the linking of the heroku app to the correct GitHub repository.

In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

Set the following config vars:

# Key	Value

SECRET_KEY	<your_secret_key>

STRIPE_PUBLISHABLE	<your_stripe_publishable>

STRIPE_SECRET	<your_stripe_secret>

DEFAULT_FROM_EMAIL	<your_from_email>

SERVER_EMAIL	<your_server_email>

EMAIL_HOST	<your_email_host>

EMAIL_HOST_USER	<your_host_user>

EMAIL_HOST_PASSWORD	<your_host_password>

In the Heroku dashboard, click "Deploy".

In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

The site is now successfully deployed.



# Acknowledgements

The tutors, mentors and support staff at Code Institute

Mini Projects learnt from Code Institute

Django docs

Python docs

My mentor 

Disclaimer

 The content of this Website is for educational purposes only.

# Thanks everyone from Code Institute from staff to students you are the best!