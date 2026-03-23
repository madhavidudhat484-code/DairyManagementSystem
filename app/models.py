import mysql.connector
from config import Config


def get_connection():
    return mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
    )


#  AUTH


def register_user(first_name, last_name, username, mobile, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return False, "Username already exists"

        cursor.execute(
            """
            INSERT INTO users (first_name, last_name, username, mobile, password)
            VALUES (%s, %s, %s, %s, %s)
        """,
            (first_name, last_name, username, mobile, password),
        )
        conn.commit()
        return True, "User registered successfully"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT id, username FROM users
            WHERE username = %s AND password = %s
        """,
            (username, password),
        )
        user = cursor.fetchone()
        if user:
            return True, user
        return False, "Invalid username or password"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


#  CUSTOMERS


def add_customer(code, first_name, last_name, full_name, mobile, milk_type, status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM customers WHERE code = %s", (code,))
        if cursor.fetchone():
            return False, "Customer code already exists"

        cursor.execute(
            """
            INSERT INTO customers (code, first_name, last_name, full_name, mobile, milk_type, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
            (code, first_name, last_name, full_name, mobile, milk_type, status),
        )
        conn.commit()
        return True, "Customer added successfully"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM customers ORDER BY code")
        return True, cursor.fetchall()
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def update_customer(code, first_name, last_name, full_name, mobile, milk_type, status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE customers
            SET first_name=%s, last_name=%s, full_name=%s,
                mobile=%s, milk_type=%s, status=%s
            WHERE code=%s
        """,
            (first_name, last_name, full_name, mobile, milk_type, status, code),
        )
        conn.commit()
        return True, "Customer updated successfully"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def delete_customer(code):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM customers WHERE code = %s", (code,))
        conn.commit()
        return True, "Customer deleted successfully"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


#  COLLECTION


def add_collection(date, time, milk_type, code, liters, fat, snf, rate, total):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO collection (date, time, milk_type, customer_code, liters, fat, snf, rate, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            (date, time, milk_type, code, liters, fat, snf, rate, total),
        )
        conn.commit()
        return True, cursor.lastrowid
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def get_all_collections():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM collection ORDER BY date DESC, time DESC")
        return True, cursor.fetchall()
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def update_collection(id, date, time, milk_type, code, liters, fat, snf, rate, total):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE collection
            SET date=%s, time=%s, milk_type=%s, customer_code=%s,
                liters=%s, fat=%s, snf=%s, rate=%s, total=%s
            WHERE id=%s
        """,
            (date, time, milk_type, code, liters, fat, snf, rate, total, id),
        )
        conn.commit()
        return True, "Collection updated successfully"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def delete_collection(id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM collection WHERE id = %s", (id,))
        conn.commit()
        return True, "Collection deleted successfully"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


#  RATES


def add_rate(milk_type, fat, snf, rate, date):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO rates (milk_type, fat, snf, rate, date)
            VALUES (%s, %s, %s, %s, %s)
        """,
            (milk_type, fat, snf, rate, date),
        )
        conn.commit()
        return True, cursor.lastrowid
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def get_all_rates():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM rates ORDER BY date DESC, milk_type, fat")
        return True, cursor.fetchall()
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()


def update_rate(id, milk_type, fat, snf, rate):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE rates SET milk_type=%s, fat=%s, snf=%s, rate=%s
            WHERE id=%s
        """,
            (milk_type, fat, snf, rate, id),
        )
        conn.commit()
        return True, "Rate updated successfully"
    except Exception as e:
        return False, str(e)
    finally:
        cursor.close()
        conn.close()
