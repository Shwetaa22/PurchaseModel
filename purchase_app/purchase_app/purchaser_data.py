import random
import time
from datetime import datetime
from statistics import mean
import pymysql

from settings import DATABASES

pymysql.install_as_MySQLdb()
import MySQLdb
# from purchase.models import purchase_app,PurchaseStatusModel


database = MySQLdb.connect(host=DATABASES['default']['HOST'], user=DATABASES['default']['USER'],
                           passwd=DATABASES['default']['PASSWORD'], db=DATABASES['default']['NAME'])

cursor = database.cursor()
purchase_query = """INSERT INTO purchase (purchaser_name, quantity) VALUES ( %s, %s)"""
purchase_status_query = """INSERT INTO purchase_status (purchase_id,status, created_at) VALUES ( %s, %s, %s)"""

name_array = [
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqr',
    'stu',
    'vwx',
    'yz',
    'no123'
]

status = ['open', 'dispatched', 'verified', 'delivered']

start = time.mktime(time.strptime("2019-01-01 17:00:00", "%Y-%m-%d %H:%M:%S"))  # "2019-01-01 17:00:00"
end = time.mktime(time.strptime("2020-03-31 22:00:00", "%Y-%m-%d %H:%M:%S"))  # "2020-03-31 22:00:00"

purchase_data = []
purchase_status_data = []
num = 0
# for i in range(10):
#     name = random.choice(name_array)
#     quant_avg = True
#     qunat_values = []
quant_avg = True
qunat_values = []
while quant_avg and num <= 5000:
    name = random.choice(name_array)
    # quant_avg = True


    quantity = random.randint(1, 10)
    qunat_values.append(quantity)
    # print(name,quantity,qunat_values,mean(qunat_values),mean(qunat_values) > 7,type(mean(qunat_values)))

    if int(mean(qunat_values)) > 7:
        qunat_values.remove(quantity)
        quant_avg = False
    else:
        num += 1
        purchase_data.append({"name": name, "quantity": quantity, "idd": num})
        values = (name, quantity)
        cursor.execute(purchase_query, values)
        id = cursor.lastrowid

        for j in range(0, len(status)):
            dt = random.random() * (end - start) + start
            dt = datetime.fromtimestamp(time.mktime(time.localtime(dt)))
            stat = random.choice(status)
            status_values = (id,stat, dt)
            cursor.execute(purchase_status_query, status_values)
            purchase_status_data.append({"status": stat, "purchase_id": num, "created_at": dt})

print(purchase_data)
print(purchase_status_data)
print(num)
# purchase_app.objets.bulk_create(purchase_data)
# PurchaseStatusModel.objets.bulk_create(purchase_status_data)

cursor.close()
database.commit()
database.close()
