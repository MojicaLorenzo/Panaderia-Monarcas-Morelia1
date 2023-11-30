
Panaderia Monarcas Morelia

Panaderia Monarcas Morelia is your go-to destination for a delightful online bakery experience. Browse through an assortment of freshly baked goods, create an account to unlock personalized features, and enjoy the convenience of managing your cart. My full-stack project integrates the charm of traditional baking with modern technology, offering a seamless journey from exploration to account management. The project is built using React for the frontend and a Python-based Flask server for the backend. The application utilizes a database to store user information, bakery item details, and more.

Key Features:

Browse Bread Options: Customers can view a diverse range of bakery items, each displaying essential details such as price, ingredients, and more.

User Authentication: Users can create an account, log in, and enjoy a personalized experience. Authentication ensures a secure environment for managing their preferences and orders.

Account Management:

Edit Profile: Users can update their account information, such as name, username, and email.

Delete Account: For users who wish to discontinue their account, a feature is available to delete their profile.

Shopping Cart: When logged in, users are assigned a shopping cart, allowing them to add and remove items. Although order placement is not fully implemented yet, it is a future goal.

Dark Mode Toggle: The website provides a visually comfortable experience with a Dark Mode toggle, giving users control over their preferred theme.



Technologies Used
Frontend: React.js
Backend: Flask (Python)
Database: SQL
Project Structure
The project is organized into different components, each serving a specific purpose. Here's a brief overview:

Frontend: The src folder contains React components, pages, and stylesheets. Key components include:

HomePage: Displays bakery items.
LoginForm and SignUpForm: Handle user authentication.
AccountForm: Manages user profile information.
Cart: Allows users to add and remove items from the shopping cart.
Backend: The app.py file contains the Flask application, which handles routes, user authentication, and interactions with the database.

Database: The database schema and models are defined to store essential information such as user details, bakery items, and shopping carts.

Installation
Clone the repository:

git clone https://github.com/your-username/panaderia-monarcas-morelia.git
Install frontend dependencies:


cd panaderia-monarcas-morelia
npm install
Install backend dependencies:


cd backend
pip install -r requirements.txt
Set up the database:

Start the frontend and backend:

# Frontend
npm start

# Backend
python app.py
Open your browser and navigate to http://localhost:3000 to view the website.

Usage
Visit the website and explore the delightful bakery options.
Create an account or log in to access personalized features.
Edit your profile information or delete your account if needed.
Use the shopping cart to add and remove items (order placement feature coming soon).
Enjoy a visually comfortable experience with the Dark Mode toggle.
Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes with descriptive commit messages.
Push your changes to your fork.
Open a pull request.