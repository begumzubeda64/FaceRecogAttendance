import mysql.connector as mysql
from mysql.connector import Error
import os
from penc import check_password
from penc import hash_password
from datetime import datetime

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
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()

        queryclass = "SELECT * FROM student WHERE rollno = %s"
        para = (rollno,)

        cursor.execute(queryclass, para)
        record = cursor.fetchall()  # fetches all record

        if len(record) == 0:
            query = """INSERT INTO student(rollno, name, pic, class) VALUES (%s,%s,%s,%s)"""
            #path = "C:/"
            #ppath = os.path.join(path, f"xampp/htdocs/AttendanceFace/Images/{cls}")
            ppath = f'Images/{cls}'
            if os.path.exists(ppath):
                pass
            else:
                os.mkdir(ppath)
            pp = os.path.basename(pic)#filename
            ext = os.path.splitext(pp)[1]#file extension
            stdPicture = convertToBinaryData(pic) #covert pic in binary
            insertTuple = (rollno, name, stdPicture, cls) #insert parameters
            result = cursor.execute(query, insertTuple) #execute query with parameters
            r = str(rollno)
            #picPath = os.path.join(path, f"xampp/htdocs/AttendanceFace/Images/{cls}/{r}{ext}")
            picPath = f'Images/{cls}/{r}{ext}'
            write_file(stdPicture, picPath)  # writing image read from table and storing it with new name
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
            user="root",
            password="",
            database="attenddb"
        )

        # print(db,"Connected")
        cursor = con.cursor()
        # query = """SELECT * from student where rollno = %s and class = %s"""
        querypic = "SELECT * FROM student WHERE class = %s"
        para = (cls,)

        cursor.execute(querypic, para)
        record = cursor.fetchall()#fetches all record
        if len(record) != 0:
            ppath = f'Images/{cls}'
            if os.path.exists(ppath):
                myList = os.listdir(ppath)  # stores list of images in the path 'Images'
                return myList
            else:
                os.mkdir(ppath)
                for row in record:
                    picpath = f'Images/{cls}/{row[0]}.jpg'
                    write_file(row[2], picpath)
                myList = os.listdir(ppath)
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

#deleting a student
def deleteStudent(rollno, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
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
        ppath1 = f'Images/{cls}/{rollno}.jpg'
        ppath2 = f'Images/{cls}/{rollno}.png'
        if os.path.exists(ppath1):
            os.remove(ppath1)
        else:
            os.remove(ppath2)
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

#read all class-- values is an array
def readAllClass(values):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
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

#insert subject
def insertSubject(name, cls):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
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

    except mysql.Error as error:
        print("Failed inserting data into MySQL table {}".format(error))
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

def insertLec(cls, name, sub, t, lf, ty, d):
    try:
        # connecting to database
        con = mysql.connect(
            host="localhost",
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
            user="root",
            password="",
            database="attenddb"
        )
        l = []
        cursor = con.cursor()
        queryatt = "SELECT lframe FROM attendancetbl WHERE class = %s AND ldate = %s"
        now = datetime.now()
        d = now.strftime('%d-%m-%Y')
        para = (cls, d,)

        cursor.execute(queryatt, para)
        record = cursor.fetchall()  # fetches all record
        for row in record:
            l.append(row[0])
        return l

    except mysql.Error as error:
        print("Failed reading data into MySQL table {}".format(error))
        return False

    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()