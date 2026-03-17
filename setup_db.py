import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

print("🐄 Dairy Management System - Database Setup")
print("=" * 45)

# Step 1: Connect WITHOUT database
try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "DatabaseUser"),
        password=os.getenv("DB_PASSWORD", "DatabasePassword"),
    )
    cursor = conn.cursor()
    print("✅ MySQL Connected Successfully!")
except Exception as e:
    print(f"❌ MySQL Connection Failed: {e}")
    print("\n👉 Check your .env file - DB_USER and DB_PASSWORD is it correct?")
    exit()

# Step 2: Create Database
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS dairy_management")
    cursor.execute("USE dairy_management")
    print("✅ Database 'dairy_management' Ready!")
except Exception as e:
    print(f"❌ Database creation failed: {e}")
    exit()

# Step 3: Create Tables
tables = {
    "users": """
        CREATE TABLE IF NOT EXISTS users (
            id         INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50)  NOT NULL,
            last_name  VARCHAR(50)  NOT NULL,
            username   VARCHAR(50)  NOT NULL UNIQUE,
            mobile     VARCHAR(15)  NOT NULL,
            password   VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "customers": """
        CREATE TABLE IF NOT EXISTS customers (
            id         INT AUTO_INCREMENT PRIMARY KEY,
            code       VARCHAR(20)  NOT NULL UNIQUE,
            first_name VARCHAR(50)  NOT NULL,
            last_name  VARCHAR(50)  NOT NULL,
            full_name  VARCHAR(100) NOT NULL,
            mobile     VARCHAR(15),
            milk_type  ENUM('Cow', 'Buffalo') NOT NULL,
            status     ENUM('ON', 'OFF') DEFAULT 'ON',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "collection": """
        CREATE TABLE IF NOT EXISTS collection (
            id            INT AUTO_INCREMENT PRIMARY KEY,
            date          DATE        NOT NULL,
            time          ENUM('Morning', 'Evening') NOT NULL,
            milk_type     ENUM('Cow', 'Buffalo') NOT NULL,
            customer_code VARCHAR(20) NOT NULL,
            liters        DECIMAL(8,2) NOT NULL,
            fat           DECIMAL(5,2) DEFAULT 0,
            snf           DECIMAL(5,2) DEFAULT 0,
            rate          DECIMAL(8,2) NOT NULL,
            total         DECIMAL(10,2) NOT NULL,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
    "rates": """
        CREATE TABLE IF NOT EXISTS rates (
            id         INT AUTO_INCREMENT PRIMARY KEY,
            milk_type  ENUM('Cow', 'Buffalo') NOT NULL,
            fat        DECIMAL(5,2) NOT NULL,
            snf        DECIMAL(5,2) NOT NULL,
            rate       DECIMAL(8,2) NOT NULL,
            date       DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """,
}

for table_name, query in tables.items():
    try:
        cursor.execute(query)
        print(f"✅ Table '{table_name}' Ready!")
    except Exception as e:
        print(f"❌ Table '{table_name}' failed: {e}")

# Step 4: Insert Sample Data
print("\n📦 Sample data inserting...")

# Admin user
try:
    cursor.execute("SELECT id FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute(
            """
            INSERT INTO users (first_name, last_name, username,mobile,password)
            VALUES ('Admin', 'User', 'admin', '9999999999', 'admin123')
        """
        )
        print("✅ Admin user created! (username: admin / password: admin123)")
    else:
        print("ℹ️  Admin user already exists")
except Exception as e:
    print(f"❌ Admin insert failed: {e}")

# Sample Customers
customers = [
    ("10", "Ramesh", "Mane", "Ramesh P. Mane", "4323594288", "Buffalo", "ON"),
    ("20", "Dinesh", "Kale", "Dinesh R. Kale", "4952778098", "Buffalo", "ON"),
    ("30", "Atul", "Mile", "Atul S. Mile", "7709424098", "Cow", "ON"),
    ("40", "Pradip", "Pise", "Pradip H. Pise", "4098772211", "Cow", "OFF"),
    ("50", "Rohan", "Patil", "Rohan Y. Patil", "5518191480", "Cow", "ON"),
]
try:
    cursor.execute("SELECT COUNT(*) FROM customers")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany(
            """
            INSERT INTO customers (code, first_name, last_name, full_name, mobile, milk_type, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
            customers,
        )
        print(f"✅ {len(customers)} Sample customers added!")
    else:
        print("ℹ️  Customers already exist")
except Exception as e:
    print(f"❌ Customers insert failed: {e}")

# Sample Rates
rates = [
    ("Cow", 3.5, 8.0, 28.00),
    ("Cow", 4.0, 8.5, 30.00),
    ("Buffalo", 6.0, 9.0, 38.00),
    ("Buffalo", 6.5, 9.5, 41.00),
]
try:
    cursor.execute("SELECT COUNT(*) FROM rates")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany(
            """
            INSERT INTO rates (milk_type, fat, snf, rate, date)
            VALUES (%s, %s, %s, %s)
        """,
            rates,
        )
        print(f"✅ {len(rates)} Sample rates added!")
    else:
        print("ℹ️  Rates already exist")
except Exception as e:
    print(f"❌ Rates insert failed: {e}")

conn.commit()
cursor.close()
conn.close()

print("\n" + "=" * 45)
print("🎉 Database Setup Complete!")
print("=" * 45)
print("\n▶  Now You Can Start The Server :")
print("   python main.py")
print("\n🌐 Open In Browser :")
print("   http://127.0.0.1:5000")
print("\n🔑  Login:")
print("   Username : admin")
print("   Password : admin123")
print("=" * 45)
