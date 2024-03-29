import mysql.connector as mysql
from mysql.connector import Error
import os
from penc import check_password
from penc import hash_password
from datetime import datetime
import shutil

#covert pic to binary file
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file: #open file and read in binary
        binaryData = file.read()
    return binaryData

#writing read file in binary
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

#inserting data to student table
def insertStudent(rollno, name, pic, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        queryclass = "SELECT * FROM student WHERE rollno = %s AND class = %s"
        para = (rollno, cls,)

        cursor.execute(queryclass, para)
        record = cursor.fetchall()  # fetches all record

        if len(record) == 0:
            query = """INSERT INTO student(rollno, name, pic, class) VALUES (%s,%s,%s,%s)"""
            stdPicture = pic #coverted pic in binary
            insertTuple = (rollno, name, stdPicture, cls) #insert parameters
            result = cursor.execute(query, insertTuple) #execute query with parameters
            con.commit()
            return True
        else:
            return False

    except mysql.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("MySQL connection is closed")

#reading pic file
def readStudent(cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()
        querypic = "SELECT * FROM student WHERE class = %s"
        para = (cls,)

        cursor.execute(querypic, para)
        record = cursor.fetchall()#fetches all record
        if len(record) != 0:
            myList = record
            return myList
        else:
            return ""


    except mysql.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("MySQL connection is closed")

#reading all students based on class
def readAllStudent(cls, values):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()
        query = "SELECT * FROM student WHERE class = %s ORDER BY rollno"
        para = (cls,)

        cursor.execute(query, para)
        record = cursor.fetchall()#fetches all record
        for row in record:
            dic = {}
            dic['roll'] = row[0]
            dic['name'] = row[1]
            values.append(dic)
        return values


    except mysql.Error as error:
        print("Failed to read data from MySQL table {}".format(error))

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("MySQL connection is closed")

#updating data to student table
def updateStudent(prollno, pcls, rollno, name, pic, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()
        record = []
        if prollno != rollno:
            queryclass = "SELECT * FROM student WHERE rollno = %s AND class = %s"
            para = (rollno, cls,)

            cursor.execute(queryclass, para)
            record = cursor.fetchall()  # fetches all record

        if len(record) == 0:
            if pic != "":
                query = """UPDATE student SET rollno=%s, name=%s, pic=%s, class=%s WHERE rollno=%s AND class=%s"""
                stdPicture = pic  # coverted pic in binary
                updateTuple = (rollno, name, stdPicture, cls, prollno, pcls,)  # update parameters
                result = cursor.execute(query, updateTuple)  # execute query with parameters
            else:
                query = """UPDATE student SET rollno=%s, name=%s, class=%s WHERE rollno=%s AND class=%s"""
                updateTuple = (rollno, name, cls, prollno, pcls,)  # update parameters
                result = cursor.execute(query, updateTuple)  # execute query with parameters

            con.commit()
            return True
        else:
            return False

    except mysql.Error as error:
        print("Failed updating data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("MySQL connection is closed")

#deleting a student
def deleteStudent(rollno, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        query = "DELETE FROM student WHERE rollno = %s AND class = %s"
        para = (rollno, cls,)
        cursor.execute(query, para)
        con.commit()
        return True

    except mysql.Error as error:
        print("Failed deleting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("MySQL connection is closed")

#inserting class
def insertClass(name):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        queryclass = "SELECT * FROM classtbl WHERE class = %s"
        para = (name,)

        cursor.execute(queryclass, para)
        record = cursor.fetchall()  # fetches all record
        if len(record) == 0:
            query = """INSERT INTO classtbl(class) VALUES (%s)"""
            insertTuple = (name,) #insert parameters
            result = cursor.execute(query, insertTuple) #execute query with parameters
            con.commit()
            return True

    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

#updating class
def updateClass(pname, name):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        queryclass = "SELECT * FROM classtbl WHERE class = %s"
        para = (name,)
        cursor.execute(queryclass, para)
        record = cursor.fetchall()  # fetches all record

        if len(record) == 0:
            cquery = """UPDATE classtbl SET class=%s WHERE class=%s"""
            cTuple = (name, pname,) #update parameters
            cursor.execute(cquery, cTuple) #execute query with parameters

            squery = """UPDATE subjecttbl SET class=%s WHERE class=%s"""
            sTuple = (name, pname,)  # update parameters
            cursor.execute(squery, sTuple)  # execute query with parameters

            stquery = """UPDATE student SET class=%s WHERE class=%s"""
            stTuple = (name, pname,)  # update parameters
            cursor.execute(stquery, stTuple)  # execute query with parameters

            con.commit()
            return True
        else:
            return False

    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

#read all class-- values is an array
def readAllClass(values):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        queryclass = "SELECT class FROM classtbl"

        cursor.execute(queryclass)
        record = cursor.fetchall()  # fetches all record
        for row in record:
            values.append(row[0])
        return values

    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

#deleting a class
def deleteClass(cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        clsquery = "DELETE FROM classtbl WHERE class = %s"
        clspara = (cls,)
        cursor.execute(clsquery, clspara,)

        stquery = "DELETE FROM student WHERE class = %s"
        stpara = (cls,)
        cursor.execute(stquery, stpara,)

        subquery = "DELETE FROM subjecttbl WHERE class = %s"
        subpara = (cls,)
        cursor.execute(subquery, subpara,)
        con.commit()
        return True

    except mysql.Error as error:
        print("Failed deleting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("MySQL connection is closed")

#insert subject
def insertSubject(name, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        querysub = "SELECT * FROM subjecttbl WHERE subject = %s AND class = %s"
        para = (name,cls,)

        cursor.execute(querysub, para)
        record = cursor.fetchall()  # fetches all record
        if len(record) == 0:
            query = """INSERT INTO subjecttbl(subject,class) VALUES (%s,%s)"""
            insertTuple = (name,cls,) #insert parameters
            result = cursor.execute(query, insertTuple) #execute query with parameters
            con.commit()
            return True
        else:
            return False

    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

#update subject
def updateSubject(pname, pcls, name, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        querysub = "SELECT * FROM subjecttbl WHERE subject = %s AND class = %s"
        para = (name,cls,)
        cursor.execute(querysub, para)
        record = cursor.fetchall()  # fetches all record

        if len(record) == 0:
            query = """UPDATE subjecttbl SET subject=%s, class=%s WHERE subject=%s AND class=%s"""
            updateTuple = (name,cls,pname,pcls,) #update parameters
            result = cursor.execute(query, updateTuple) #execute query with parameters
            con.commit()
            return True
        else:
            return False

    except mysql.Error as error:
        print("Failed updating data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

#read all class-- values is an array
def readSubject(cls, values):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        querysub = "SELECT subject FROM subjecttbl where class = %s"
        para = (cls,)
        cursor.execute(querysub, para)

        record = cursor.fetchall()  # fetches all record
        for row in record:
            values.append(row[0])
        return values

    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

#deleting a subject
def deleteSubject(sub, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        query = "DELETE FROM subjecttbl WHERE subject = %s AND class = %s"
        para = (sub, cls,)
        cursor.execute(query, para)
        con.commit()
        return True

    except mysql.Error as error:
        print("Failed deleting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print("MySQL connection is closed")

def insertLec(cls, name, sub, t, lf, ty, d):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        cursor = con.cursor()
        queryatt = "SELECT * FROM attendancetbl WHERE class = %s AND rollno = %s AND lframe = %s AND ldate = %s"
        iname = int(name)
        para = (cls, iname, lf, d,)

        cursor.execute(queryatt, para)
        record = cursor.fetchall()  # fetches all record
        if len(record) == 0:
            query = """INSERT INTO attendancetbl(class,rollno,subject,teacher,lframe,type,ldate) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            insertTuple = (cls,iname,sub,t,lf,ty,d)  # insert parameters
            result = cursor.execute(query, insertTuple)  # execute query with parameters
            con.commit()
            return True


    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def insertAccount(user, p):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()
        query = """INSERT INTO account(username,pwd) VALUES (%s,%s)"""
        insertTuple = (user,p,) #insert parameters
        result = cursor.execute(query, insertTuple) #execute query with parameters
        con.commit()
        return True

    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def readAccount(user):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()
        querylog = "SELECT pwd FROM account WHERE username = %s"
        para = (user,)

        cursor.execute(querylog, para)
        record = cursor.fetchall()
        if len(record) != 0:
            for row in record:
                pwd = row[0]
                return pwd
        else:
            return ""

    except mysql.Error as error:
        print("Failed reading data into MySQL table {}".format(error))

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def changePassword(p, new_p):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()
        querych = "SELECT pwd FROM account"

        cursor.execute(querych)
        record = cursor.fetchall()
        ch = False
        ohpd = ""
        for row in record:
            pwd = row[0]
            if check_password(pwd, p):
                ch = True
                ohpd = pwd
                break

        if ch == True:
            sql = "UPDATE account SET pwd = %s WHERE pwd = %s"
            n = hash_password(new_p)
            para = (n, ohpd,)
            cursor.execute(sql, para)
            con.commit()
            return True
        else:
            return False


    except mysql.Error as error:
        print("Failed reading data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def readlframes(cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
            port=3308,
            user="root",
            password="",
            database="attenddb"
        )

        cursor = con.cursor()
        queryatt = "SELECT * FROM attendancetbl WHERE class = %s AND ldate = %s"
        now = datetime.now()
        d = now.strftime('%d-%m-%Y')
        para = (cls, d,)

        cursor.execute(queryatt, para)
        record = cursor.fetchall()  # fetches all record
        return record

    except mysql.Error as error:
        print("Failed reading data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

# pwd = hash_password("master1234")
# insertAccount("admin", pwd)