import sqlite3

DATABASE_FILE = "data/finance.db"


def get_connection():
    return sqlite3.connect(DATABASE_FILE)
    
def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def insert_transaction(transaction_data: dict):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO transactions
        (type, amount, category)
        VALUES (?, ?, ?)
        """,
        (
            transaction_data["type"],
            transaction_data["amount"],
            transaction_data["category"]
        )
    )

    connection.commit()

    transaction_id = cursor.lastrowid

    connection.close()

    return transaction_id

def get_transaction_by_id_from_db(transaction_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, type, amount, category
        FROM transactions
        WHERE id = ?
        """,
        (transaction_id,)
    )

    row = cursor.fetchone()

    connection.close()

    return row

def delete_transaction_by_id_from_db(transaction_id: int):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM transactions
        WHERE id = ?
        """,
        (transaction_id,)
    )

    connection.commit()

    connection.close()

def update_transaction_by_id_from_db(
    transaction_id: int,
    updated_data: dict
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE transactions
        SET type = ?, amount = ?, category = ?
        WHERE id = ?
        """,
        (
            updated_data["type"],
            updated_data["amount"],
            updated_data["category"],
            transaction_id
        )
    )

    connection.commit()

    connection.close()


def get_total_amount_by_type(transaction_type: str):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT SUM(amount)
        FROM transactions
        WHERE type = ?
        """,
        (transaction_type,)
    )

    result = cursor.fetchone()

    connection.close()

    return result[0] or 0


def get_filtered_transactions_from_db(transaction_type=None, category=None, sort = None):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT id, type, amount, category
        FROM transactions
    """

    conditions = []
    params = []

    if transaction_type is not None:
        conditions.append("type = ?")
        params.append(transaction_type)

    if category is not None:
        conditions.append("category = ?")
        params.append(category)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    if sort == "amount_asc":
        query += " ORDER BY amount ASC"
    elif sort == "amount_desc":
        query += " ORDER BY amount DESC"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    connection.close()

    return rows

def get_statistics_by_category_from_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT category, SUM(amount)
        FROM transactions
        GROUP BY category
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows

def get_transaction_count_from_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) FROM transactions
        """
    )

    result = cursor.fetchone()

    connection.close()

    return result[0]