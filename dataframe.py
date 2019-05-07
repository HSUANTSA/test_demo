import pandas as pd
import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    db = "techyesdb"
)

c = connection.cursor()
sql = "select * from contact_us;"
c.execute(sql)
data = c.fetchall()
username=[]
email=[]
phone=[]

for i in data:
    username.append(i[1])
    email.append(i[3])
    phone.append(i[2])

number= (1,2)

users = {
    "Username" : username,
    "Email" : email,
    "Phone" : phone
}

user_details = pd.DataFrame(users,index=number)
print(user_details)

json_file = user_details.to_json(r"E:\PandaDemo\user_detail.json")