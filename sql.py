import sqlite3
import csv
import pandas as pd
import hashlib
conn = sqlite3.connect('./NittanyMarket.db')
print("open database success")
c = conn.cursor()

c.execute("drop table Users")
c.execute('''CREATE TABLE Users (
  email         CHAR(40)     ,
  Password      CHAR(128)     
);''')
"""
c.execute("drop table Buyers")
c.execute('''CREATE TABLE Buyers (
  email         CHAR(40)     NOT NULL,
  first_name      CHAR(32)     NOT NULL,
  last_name      CHAR(32)     NOT NULL,
  gender      CHAR(32)     NOT NULL,
  age       CHAR(32)    NOT NULL,
  home_address_id      CHAR(32)     NOT NULL
);''')

c.execute("drop table Credit_Cards")
c.execute('''CREATE TABLE Credit_Cards (
  credit_card_num         CHAR(40)     NOT NULL,
  card_code      CHAR(32)     NOT NULL,
  expire_month      CHAR(32)     NOT NULL,
  expire_year      CHAR(32)     NOT NULL,
  card_type      CHAR(32)     NOT NULL,
  Owner_email   CHAR(32)      NOT NULL
);''')

c.execute("drop table Address")
c.execute('''CREATE TABLE Address (
  address_id         CHAR(40)     NOT NULL,
  zipcode      CHAR(32)     NOT NULL,
  street_num      CHAR(32)     NOT NULL,
  street_name      CHAR(32)     NOT NULL
);''')

c.execute("drop table Zipcode_Info")
c.execute('''CREATE TABLE Zipcode_Info (
  zipcode         CHAR(40)     NOT NULL,
  city      CHAR(32)     NOT NULL,
  state_id      CHAR(32)    NOT NULL,
  population      CHAR(32)     NOT NULL,
  density      CHAR(32)     NOT NULL,
  county_name      CHAR(32)     NOT NULL,
  timezone      CHAR(32)     NOT NULL,
);''')

c.execute("drop table Sellers")
c.execute('''CREATE TABLE Sellers (
  email         CHAR(40)     NOT NULL,
  routing_number      CHAR(32)     NOT NULL,
  account_number      CHAR(32)     NOT NULL,
  balance      CHAR(32)     NOT NULL
);''')

c.execute("drop table Local_Vendors")
c.execute('''CREATE TABLE Local_Vendors (
  email         CHAR(40)     NOT NULL,
  Business_Name      CHAR(32)     NOT NULL,
  Business_Address_ID      CHAR(32)     NOT NULL,
  Customer_Service_Number      CHAR(32)     NOT NULL
);''')

c.execute("drop table Categories")
c.execute('''CREATE TABLE Categories (
  parent_category         CHAR(40)     NOT NULL,
  category_name      CHAR(32)     NOT NULL
);''')

c.execute("drop table Product_Listings")
c.execute('''CREATE TABLE Product_Listings (
  Seller_Email         CHAR(40)     NOT NULL,
  Listing_ID      CHAR(32)     NOT NULL
);''')

c.execute('''CREATE TABLE Orders (
  Transaction_ID         CHAR(40)     NOT NULL,
  Seller_Email      CHAR(32)     NOT NULL,
  Buyer_Email      CHAR(32)     NOT NULL,
  Quantity      CHAR(32)     NOT NULL,
  Payment      CHAR(32)     NOT NULL
);''')

c.execute('''CREATE TABLE Reviews (
  Buyer_Email         CHAR(40)     NOT NULL,
  Seller_Email      CHAR(32)     NOT NULL,
  Listing_ID      CHAR(32)     NOT NULL,
  Review_Desc      CHAR(32)     NOT NULL
);''')

c.execute('''CREATE TABLE Rating (
  Buyer_Email         CHAR(40)     NOT NULL,
  Seller_Email      CHAR(32)     NOT NULL,
  Rating      CHAR(32)     NOT NULL,
  Rating_Desc      CHAR(32)     NOT NULL
);''')
"""


f = csv.reader(open("./Users.csv"))
"""
for i in f:
    print(i)
    sql = "INSERT INTO user(email,Password) VALUES ('%s','%s')" % (
        i[0], i[1])
    c.execute(sql)
"""
for i in f:
    password = i[1]
    email = i[0]
    h1 = hashlib.md5()
    h1.update(password.encode('utf-8'))
    md5password = h1.hexdigest()
    sql = "INSERT INTO users(Email, Password) VALUES ('%s', '%s')" % (
          email, md5password)
    c.execute(sql)

conn.commit()

