import sqlite3

with sqlite3.connect('sales.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE sales")
    c.execute("CREATE TABLE sales(Company_name TEXT , Engagement_type TEXT , Current_Stage TEXT , Sales_Person_Name TEXT , Closing_Date TEXT)")
    c.execute('INSERT INTO sales VALUES("Heroku" , "Staffing" , "Deal Closed" , "Chris" , "November 30")')
