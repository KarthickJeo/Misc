import sqlite3

with sqlite3.connect("emails.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE email_addresses")
    c.execute("CREATE TABLE email_addresses(title TEXT )")
    c.execute('INSERT INTO email_addresses VALUES("email")')
