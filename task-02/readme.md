# Inventory Management System (IMS)

## Overview
The Inventory Management System (IMS) is a user-friendly application developed using Python's Tkinter library and SQLite for database management. This system helps manage and track inventory items, users, sales, and categories efficiently. 

## Features
- User Management: Add, update, and manage users.
- Product Management: Keep track of products in the inventory.
- Category Management: Organize products into categories.
- Sales Tracking: Record and view sales transactions.
- Inventory Tracking: Monitor inventory levels.
- Reporting: Generate reports based on user activities and inventory status.
- Real-time Updates: Displays current users, products, categories, and sales count.

## Technologies Used
- Python
- Tkinter (GUI)
- SQLite (Database)
- PIL (Pillow) for image handling


## Database :
### Features

- **Creates Tables**: Sets up the following tables in the `inventory.db` database:
  - **Users**: Stores user information including ID, name, date of birth, email, contact details, gender, password, and user type.
  - **Products**: Manages product details such as product ID, category, name, quantity, price, and status.
  - **Tracking**: Keeps records of product tracking with references to the product table, allowing for monitoring of product levels.
  - **Category**: Maintains product categories.



## Users :
### Features

- **User Registration**: Add new users with fields for user ID, name, date of birth, email, contact, gender, password, and user type (Admin/User).
- **User Management**: Update user details or delete users from the database.
- **Search Functionality**: Search users by multiple criteria, including Name, Email, Contact, and User ID.
- **Data Display**: User information is displayed in a structured table format, allowing for easy viewing and management of records.
- **Password Validation**: Ensure that the password and confirm password fields match during user registration and updates.
- **Clear Functionality**: Clear all input fields for a new entry after any operation.



## Products :
### Features

- **Add Products**: Users can add new products with details like category, name, quantity, price, and status.
- **Edit Products**: Modify the details of existing products.
- **Delete Products**: Remove products from the inventory.
- **Search Functionality**: Search for products based on name, category, or price.
- **Data Persistence**: All product information is stored in an SQLite database.



## Category :
### Features

- **Add Category**: Users can enter a new category name and add it to the database.
- **Delete Category**: Users can select a category from the list and delete it if needed.
- **View Categories**: Displays all existing categories in a table format, making it easy to manage and review categories.
- **User Feedback**: Displays success and error messages using message boxes for better user experience.



## Sales :
### Features
- **View Customer Bills**: Users can view customer bills stored in the `bill` directory.
- **Search by Invoice Number**: Users can enter an invoice number to quickly retrieve and display the corresponding bill.
- **Clear Display**: A clear button to reset the displayed bills and refresh the list.



## Billing :
### Features
- **Product Management**: Add, search, and display products.
- **Customer Management**: Input and manage customer details.
- **Billing**: Calculate total amount, discounts, and net payable.
- **Cart Functionality**: Add and remove products from cart.
- **Calculator**: Built-in calculator for quick calculations.
- **Receipt Generation**: Generate, save and print customer bills.



## Tracking :
## Features
- **Add Products**: Log changes in product quantities and details.
- **Search Products**: Search for products by ID or name.
- **Display or Track Inventory**: View a list of all products in the inventory.



## Report Low Stock
## Features
- **Search Products**: Search for products by name, category, or price.
- **Show All Products**: Display a comprehensive list of all products in the inventory.
- **Low Stock Report**: Generate a report of products below a specified stock threshold.
