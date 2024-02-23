
# Flask API with MySQL Database

This repository contains a Flask API implementation with MySQL database integration. This API serves as a foundation for building web applications that require a backend server to handle HTTP requests and interact with a MySQL database and jwt(json web token  ).


## Getting Started

To get started with this Flask API, follow these steps:

+ First Install Flask  Framework

```bash
  pip install flask
```
+ Flask is a lightweight, Python framework for web applications.
        
    + A built-in development server
    + A fast debugger
    + Lightweight
    + An out-of-the-box framework, meaning that you can jump straight into it

+ You can read best user guid Flask Documantaion

     - [Flask Documantaion ](https://flask.palletsprojects.com/en/3.0.x/)


+ Second Database Setup:
    
    - Create a MySQL database.
    - I am use Gui softwear workbench
    - [You can downloads MySQL with workbench using this link ](https://dev.mysql.com/downloads/windows/installer/8.0.html)
    - Update the config.py file with your database credentials.
    - [You can read Mysql documentation ](https://dev.mysql.com/doc/)
    - [You can also read Mysql conection with our model ](https://www.geeksforgeeks.org/python-mysql/)

## Dependencies
 
  + Flask: Web framework for building APIs in Python.
  + Flask-MySQLdb: MySQL database integration for Flask.

## Our API Endpoints

The following endpoints are available:

  + GET  - "/user/getall" --> Get all data in our database.
  + POST - "/user/getone" --> Add data in our database.
  + POST - "/user/addmultiple" --> Add multiple dataset.
  + PUT  - "/user/update" -->Update dataset.
  + DELETE - "/user/delete/<id>" --> Delete dataset using id number.
  + PATCH  - "/user/patch/<id>" --> update particular column using id number
  + GET  - "/user/getall/limit/<limit>/page/<page>" --> This is pagination endpoint
  + PUT - /user/avatar/<uid>/upload" --> Upload Image file in database.

  + POST - "/user/login" --> user login and Create jwt(json web token) token.

## Use jwt (json web token)

  + The header: This contains information about the type of token and the signing algorithm.

  + The payload: This contains the claims about the user, such as their username and email address.

  + The signature: This is used to verify the integrity of the token.

  + JWTs are a powerful tool for securely transmitting information between two parties. They are often used for authentication and authorization, but they can also be used to transmit other types of information.

  + I am generate token inside user_model.py in user_login_model function and set expired time. and I am Create Second file Auth_model.py inside user authentication you can check code and get idea.

  + [Learn more about jwt](\https://jwt.io/introduction)

## Test the API:
 
  + Once the application is running, you can test the API endpoints using tools like Postman .

  - [Download postman](https://www.postman.com/downloads/)
