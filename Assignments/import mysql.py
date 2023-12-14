# # import mysql.connector

# # my_db = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="2524@Mahesh",
# #     database="viraj"
# # )

# # cur = my_db.cursor()

# # i = "INSERT INTO VIRU VALUES(2,'SAHIL')"
# # cur.execute(i)
# # my_db.commit()

# # # my_result = cur.fetchall()
# # # for i in my_result:
# # #     print(i)


# # cur.close()
# # my_db.close()

# import mysql.connector

# my_db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="2524@Mahesh",
#     database="viraj"
# )

# cur =my_db.cursor()

# i = "INSERT INTO VIRU VALUES(1,'JORI')"
# u ="UPDATE VIRU SET name='mahesh' where id=2"
# d ="DELETE from viru where id=2"

# cur.execute(i)
# cur.execute(u)
# cur.execute(d)
# my_db.commit()


# records = cur.fetchall()

# for records in records:
#     print(records)

# cur.close()
# my_db.close()

import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2524@Mahesh",
    database="viraj"
)

cur = my_db.cursor()

# INSERT query
i = "INSERT INTO VIRU VALUES(2, 'karan')"
cur.execute(i)
my_db.commit()

# UPDATE query
u = "UPDATE VIRU SET name='mahesh' WHERE id=1"
cur.execute(u)
my_db.commit()

# DELETE query
# d = "DELETE FROM VIRU WHERE id=2"
# cur.execute(d)
# my_db.commit()

# SELECT query to fetch and display records
s = "SELECT * FROM VIRU"
cur.execute(s)

records = cur.fetchall()

for record in records:
    print(record)

cur.close()
my_db.close()
