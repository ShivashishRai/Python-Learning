

# import cx_Oracle
#
# try:
#     connect = cx_Oracle.connect()
#     curs = connect.cursor()
#
#     #Command to execute/fire Query
#     curs.execuate('Select * from Employee')
#
#     #command to commit the DML Command and make changes to the db
#     curs.commit()
#
#     # below commands to fetch queries from the db
#     # row = curs.fetchone()
#     # rows = curs.fetchmany(3)
#     # all_rows = curs.fetchall()
#
#
# except cx_Oracle.DatabaseError as dberror:
#     print("Error enountered while connecting Database", dberror)
#
# finally:
#     if curs:
#         curs.close()
