# Mithra's Kitchen

###Page Issues and Areas for Improvement
* The site logo should redirect the user to the home page.
* The About page is not accessible from the navbar while on the menu page; this needs to be fixed.
* The Menu and About pages are not accessible from the navbar while on the reservation page; this needs to be fixed.
* Overall, the site's CSS can be improved.
* Prices can be added to the dishes.
* A user-specific page can be created where users can change their nickname or email.

## Main Technologies

#### Frontend:
HTML, CSS, JS 
#### Backend: 
Py+Django
Db:PostgreSQL

## About Page
This website showcases the culinary offerings of our restaurant. Here, you can explore detailed descriptions of our dishes to help you make your dining choices. Additionally, the website features an online reservation system to enhance your dining experience. Please note that reservations cannot be made without logging in.
![1](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/ss1.jpg)
![2](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/ss2.jpg)
![3](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/about.jpg)
* Customers' favorite dishes in our restaurant are shown here
![3](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/favorites.jpg)
![4](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/favorites2.jpg)
* Footer 
![5](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/footer.jpg)




All user and reservation data are securely managed and stored in the 'mitraskitchen' database, which is hosted on Heroku.

### Example Demo
To see an example of your art portfolio and understand how it works, you can click on the following link: [Mithra-s-Kitchen Demo](https://swecery.github.io/Mithra-s-Kitchen)



## Features
### Online Reservation
* Hassle-Free Booking: Easily book a table online at any time. Our intuitive booking system allows you to choose the date, time, and number of 
guests.
![6](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/reservations.jpg)
* Manage Reservations: Registered users can view and manage their reservations. Update or cancel your bookings with just a few clicks.
![7](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/reservations2.jpg)
![8](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/reservations3.jpg)

 
### Registration and Login
* Registration: Users can register using their email address. Upon registration, users will create a username and password. Each email and username must be unique to prevent duplicate accounts.
![8](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/registerss1.jpg)
* Login: After registration, users can log in using their username and password. This simplifies the login process while ensuring that each user's identifier is unique.
![9](https://github.com/swecery/Mithra-s-Kitchen/blob/main/images/loginss1.jpg)


### Interactive Menu
* Easy Navigation: Our website's navbar is conveniently divided into four main categories: Vegan Dishes, Chicken Dishes, Meat Dishes, and Fish Dishes. This organization allows you to easily browse and select from the specific types of meals offered at our restaurant.

### Installation Guide

This section details how to set up and configure your Django project in a local environment using PostgreSQL.

To successfully run this project, ensure the following tools are installed on your system:

* Python (version 3.8 or higher recommended)
* pip (Python package manager)
* PostgreSQL (Database server)

#### Using a virtual environment for Python projects helps manage dependencies effectively. To create a virtual environment, run the following commands in your terminal: 
```
bash
python -m venv venv
```
#### To activate the virtual environment:
* For macOS and Linux: 
```
bash
source venv/bin/activate
```
* For Windows:
```
bash
source venv/bin/activate
```
#### Installing Required Python Packages:
```
bash
pip install -r requirements.txt
```
Firstly, to use a PostgreSQL database in your project, you need to install the psycopg2 package. psycopg2 is an adapter written in Python for interacting with PostgreSQL databases. You can manage your database operations in your Django project using this adapter.

#### Installing Psycopg2: 
```
bash
pip install psycopg2
```
If you prefer a lighter installation, you can use the psycopg2-binary package:
```
bash
pip install psycopg2-binary
```

#### Install PostgreSQL (macOS)
If you have Homebrew installed, you can easily install PostgreSQL by opening a terminal and running:
```
bash
brew install postgresql
```
#### Starting PostgreSQL:
After installation, you can start PostgreSQL using:
```
bash
brew services start postgresql
```
###Validator
nput validation is missing on all pages.

## License

[MIT](https://choosealicense.com/licenses/mit/)
