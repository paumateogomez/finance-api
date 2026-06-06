# Finance API

A REST API for personal finance management built with **Python**, **FastAPI** and **SQLite**.

This project was developed to learn backend development concepts such as REST APIs, database management, SQL queries, project architecture and professional Git workflows.

## Features

* Create transactions
* List transactions
* Get transaction by ID
* Update transactions
* Delete transactions
* Filter transactions by type
* Filter transactions by category
* Combine multiple filters
* Sort transactions by amount
* Calculate balance
* Generate statistics by category
* Count total transactions
* Dashboard statistics endpoint
* SQLite database persistence
* Automatic API documentation with Swagger UI

---

## Technologies

* Python
* FastAPI
* Pydantic
* SQLite
* Uvicorn
* Git
* GitHub

---

## Project Structure

```txt
finance-api/
├── data/
│   └── finance.db
├── src/
│   ├── database.py
│   ├── models/
│   │   └── transaction.py
│   └── services/
│       └── transaction_service.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## API Endpoints

### General

```http
GET /
```

Returns the API status.

---

### Transactions

```http
GET /transactions
POST /transactions
GET /transactions/{transaction_id}
PUT /transactions/{transaction_id}
DELETE /transactions/{transaction_id}
```

---

### Filtering and Sorting

```http
GET /transactions?type=expense
GET /transactions?category=food
GET /transactions?type=expense&category=food

GET /transactions?sort=amount_asc
GET /transactions?sort=amount_desc

GET /transactions?type=expense&category=food&sort=amount_desc
```

---

### Balance and Statistics

```http
GET /balance
GET /statistics/categories
GET /statistics/count
GET /statistics
```

---

## Example Transaction

```json
{
  "type": "expense",
  "amount": 50,
  "category": "food"
}
```

---

## Example Dashboard Response

```json
{
  "total_transactions": 12,
  "income": 3500,
  "expenses": 1200,
  "balance": 2300,
  "categories": [
    {
      "category": "food",
      "total": 350
    },
    {
      "category": "transport",
      "total": 120
    }
  ]
}
```

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the server

```bash
python -m uvicorn main:app --reload
```

### Open Swagger Documentation

```txt
http://127.0.0.1:8000/docs
```

---

## SQL Concepts Used

This project includes practical usage of:

* SELECT
* INSERT
* UPDATE
* DELETE
* WHERE
* ORDER BY
* SUM
* COUNT
* GROUP BY

---

## Learning Objectives

The goal of this project is to learn and practice:

* REST API development
* FastAPI fundamentals
* SQLite database management
* SQL query design
* Backend architecture
* Service layer separation
* Data persistence
* Professional Git and GitHub workflow

---

## Future Improvements

* User authentication
* Transaction dates
* Monthly statistics
* Export to CSV
* Frontend dashboard
* Docker deployment
* Cloud deployment

```
```
