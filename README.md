# ATM_System

For this project, I developed a database management system using the Python programming language and MySQL as the relational database management system. The goal of this project was to create a system that allows users to easily perform various transactions on the data stored in the database.

One of the key features of this system is its ability to automatically create the database if it does not already exist. This ensures that users can start using the system without having to manually set up the database beforehand. The system also provides an intuitive interface for users to perform common transactions such as creating, updating, deleting, and querying data.

To achieve this functionality, I used the MySQL Connector/Python module to establish a connection between the Python code and the MySQL server. This module provides a simple and consistent API for interacting with the MySQL database from within Python code.

## Features
1. **Automatic Database Creation:** The system can create the necessary database automatically, streamlining the setup process for users.
2. **Intuitive User Interface:** Users can easily perform common transactions, including creating, updating, deleting, and querying data, through a user-friendly interface.
3. **MySQL Connector/Python:** Utilizing this module to establish a secure and efficient connection between the Python code and the MySQL server.
4. **User Authentication:** Secure login using a PIN for account access.
5. **Balance Inquiry:** Check the account balance in real-time.
6. **Cash Withdrawal:** Withdraw funds from the account.
7. **Deposit Functionality:** Add funds to the account conveniently.
8. **Transaction History:** View a record of recent transactions.
9. **Account Management:** Change the PIN for enhanced security.


## Data Manipulation
- **Insertion:** Users can create new records in the database through the system's interface. The system generates the appropriate SQL statements for seamless data insertion.
- **Updating Records:** Users can update existing records in the database by providing new values for one or more fields. The system generates the necessary SQL statements for efficient data updating.
- **Deletion:** The system allows users to delete records from the database by specifying which records to remove. It generates the appropriate SQL statements for effective data deletion.

## Querying Capabilities
- **Powerful Searches:** Users can specify complex search criteria to retrieve data from the database. The system generates SQL statements for executing these queries, providing flexible and powerful querying capabilities.

## Overview
The ATM System is a Python-based application utilizing Tkinter for the front end, MySQL for the backend database, and object-oriented programming (OOP) concepts for a modular design. This system emulates the functionality of an Automated Teller Machine (ATM), allowing users to perform various banking transactions.

## Technologies Used
### Tkinter
- **GUI Framework:** Tkinter is employed for building the graphical user interface, providing a user-friendly experience for ATM interactions.

### MySQL
- **Database Management:** MySQL serves as the backend database to store and manage user account details and transaction records securely.

### Object-Oriented Programming (OOP) Concepts
- **Modular Design:** The application is structured using OOP principles for easy maintenance, scalability, and code reusability.

## How to Run
1. **Clone the Repository:** `git clone https://github.com/your-username/atm_system.git`
2. **Install Dependencies:** Ensure Python is installed, and install the required MySQL connector via `pip install mysql-connector-python`.
3. **Setup MySQL Database:** Execute the SQL script provided (`atm_system.sql`) to create the necessary tables and populate sample data.
4. **Run the Application:** Execute `python main.py` to launch the ATM System.
5. **Login Credentials:** Use the provided sample account or create new accounts to explore the functionalities.

## Future Enhancements
1. **Card-Based Authentication:** Implement a card-based system for user authentication.
2. **Multiple Account Support:** Enable users to link multiple accounts to a single ATM card.
3. **Transaction Categories:** Categorize transactions for better tracking (e.g., withdrawals, deposits, transfers).
4. **Enhanced Security Measures:** Integrate additional security features such as biometric authentication.

Enjoy the seamless and secure banking experience with the ATM System!
Overall, this project demonstrates how Python and MySQL can be used together to create a powerful and user-friendly database management system. By providing an intuitive interface for performing common transactions on data stored in a MySQL database, this system makes it easy for users to manage their data effectively.
