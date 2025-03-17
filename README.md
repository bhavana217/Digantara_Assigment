# Digantara Backend Developer Assignment

## Overview

This project implements three fundamental algorithms: Binary Search, Quick Sort, and Breadth-First Search (BFS). The APIs are designed to demonstrate the understanding of data structures and algorithms (DSA). Each API call is logged with the algorithm name, input data, and output data, allowing for revisiting the results of previous queries.

## Design Decisions

1. **Modular Code Structure**: The project is organized into separate modules for algorithms, views, models, and serializers to ensure clean and maintainable code.
2. **Error Handling**: Each algorithm implementation includes error handling to manage invalid inputs gracefully.
3. **Logging**: API calls are logged in a database to maintain a record of inputs and outputs for each algorithm execution.
4. **Dockerization**: The application is dockerized to ensure consistency across different environments and simplify deployment.


## Project Structure
digantara/
├── algorithms/
│   ├── __init__.py
│   ├── algorithms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
├── digantara/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── README.md
└── algorithm_calls.log

## How to Build/Run the Solution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bhavana217/Digantara_Assigment.git
   cd digantara
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Apply migrations:

python manage.py makemigrations
python manage.py migrate
Run the server:

python manage.py runserver
