# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:46:03 2019

@author: denni
"""

import cx_Oracle

import threading
from datetime import datetime
import Logger
import matplotlib.pyplot as plt
import csv

thread_amount = 15
thread_list_index = 0
thread_list = [None] * thread_amount
lista = []
log_folder = 'C:\\Users\\Aluno\\Desktop\\garcia'
log = Logger.init('main', log_folder)

def set_log(thread_index):
  now = datetime.now()
  log.info(now.strftime('%H:%M:%S'))
  lista.append(now)

def update_cust_credit(thread_list_index):
  i = 0
  while (i < 1000):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'ORCLFATEC')
    conn = cx_Oracle.connect(user=r'system', password='fatec', dsn=dsn_tns)
    cur = conn.cursor()
    #tnc = 'SET TRANSACTION ISOLATION LEVEL SERIALIZABLE'
    tnc = 'SET TRANSACTION ISOLATION LEVEL  READ COMMITTED '
    cur.execute(tnc)
    stt = 'update sh.customers set cust_credit_limit = cust_credit_limit - :1 where customers.cust_id between :2 and :3 and cust_credit_limit > 100'
    cur.execute(stt, (9990, 250, 500))
    conn.commit()
    cur.close()
    conn.close()
    set_log(thread_list_index)
    i=i+1

for i in range(thread_amount):
  thread_list[thread_list_index] = threading.Thread(target=update_cust_credit,args=(thread_list_index,))
  thread_list[thread_list_index].start()
  log.info('THREAD '+str(thread_list_index)+' is running.\n')
  thread_list_index = thread_list_index + 1


x = []
y = []

# with open('C:\\Users\\Aluno\\Desktop\\garcia\\teste.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=';')
#     for row in plots:
#         x.append(float(row[0]))
#         y.append(float(row[1]))

# plt.plot(x,y, label='Performance do algoritmo executando ' + str(thread_amount) + ' threads por segundo')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Quantidade de commits por segundo\n X = Quantidade / Y = Segundo')
# plt.legend()
# plt.show()