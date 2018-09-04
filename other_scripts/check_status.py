# -*- coding: utf-8 -*-
__author__ = 'ivanov'

import pymysql
# соединяемся с базой данных
connection = pymysql.connect(host="localhost", user="root", passwd="1112223334", db="testdb", charset='utf8', cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        #create new record
#        sql = "INSERT INTO CHECK_STATUS (ID, LOAD_DATE, NONUNIQ_COUNT, ROW_COUNT, IDNULL_COUNT, IVNULL_COUNT, FVNULL_COUNT, CVNULL_COUNT, DVNULL_COUNT, IDZERO_COUNT, IVZERO_COUNT, FVZERO_COUNT, AV_INT_VALUE, AV_FLOAT_VALUE) VALUES (NULL, CURDATE(), (select count(*) from CHECK_OBJECT WHERE CONCAT(ID,INT_VALUE) IN (select * from (SELECT CONCAT(ID,INT_VALUE) AS CC FROM CHECK_OBJECT GROUP BY CC HAVING COUNT(*) > 1) subquary WHERE CC is not null) AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where ID is NULL AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where INT_VALUE is NULL AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where FLOAT_VALUE is NULL AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where CHAR_VALUE is NULL AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where DATE_VALUE is NULL AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where ID = 0 AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where INT_VALUE = 0 AND LOAD_DATE = CURDATE()), (select count(*) from CHECK_OBJECT where FLOAT_VALUE = 0 AND LOAD_DATE = CURDATE()), (select AVG(INT_VALUE) from CHECK_OBJECT where LOAD_DATE = CURDATE()), (select AVG(FLOAT_VALUE) from CHECK_OBJECT where LOAD_DATE = CURDATE()))"

        sql = "INSERT INTO CHECK_STATUS " \
              "(ID, LOAD_DATE, NONUNIQ_COUNT, ROW_COUNT, IDNULL_COUNT, IVNULL_COUNT, FVNULL_COUNT, CVNULL_COUNT, DVNULL_COUNT, IDZERO_COUNT, IVZERO_COUNT, FVZERO_COUNT, AV_INT_VALUE, AV_FLOAT_VALUE)" \
              " VALUES (" \
              "NULL," \
              "CURDATE()," \
              "(select count(*) from CHECK_OBJECT WHERE CONCAT(ID,INT_VALUE) IN " \
              "(select * from (SELECT CONCAT(ID,INT_VALUE) AS CC FROM CHECK_OBJECT GROUP BY CC HAVING COUNT(*) > 1) subquary" \
              " WHERE CC is not null) AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where ID is NULL AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where INT_VALUE is NULL AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where FLOAT_VALUE is NULL AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where CHAR_VALUE is NULL AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where DATE_VALUE is NULL AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where ID = 0 AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where INT_VALUE = 0 AND LOAD_DATE = CURDATE())," \
              "(select count(*) from CHECK_OBJECT where FLOAT_VALUE = 0 AND LOAD_DATE = CURDATE())," \
              "(select AVG(INT_VALUE) from CHECK_OBJECT where LOAD_DATE = CURDATE())," \
              "(select AVG(FLOAT_VALUE) from CHECK_OBJECT where LOAD_DATE = CURDATE()))"

        cursor.execute(sql)

    connection.commit()

# закрываем соединение с БД
finally:
    connection.close()