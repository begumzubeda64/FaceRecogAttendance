import mysql.connector as mysql
from mysql.connector import Error
import os


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
        query = """INSERT INTO student(rollno, name, pic, class) VALUES (%s,%s,%s,%s)"""
        path = "C:/"
        ppath = os.path.join(path, f"xampp/htdocs/AttendanceFace/Images/{cls}")
        if os.path.exists(ppath):
            pass
        else:
            os.mkdir(ppath)
        stdPicture = convertToBinaryData(pic) #covert pic in binary
        insertTuple = (rollno, name, stdPicture, cls) #insert parameters
        result = cursor.execute(query, insertTuple) #execute query with parameters
        con.commit()
        return True

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
        for row in record:
            name = row[1]
            image = row[2]
            clss = row[3]

            path = "C:/"
            ppath = os.path.join(path, f"xampp/htdocs/AttendanceFace/Images/{clss}")
            if os.path.exists(ppath):
                pass
            else:
                os.mkdir(ppath)
            picPath = os.path.join(path, f"xampp/htdocs/AttendanceFace/Images/{clss}/{name}.jpg")
            write_file(image, picPath) #writing image read from table and storing it with new name

        myList = os.listdir(f'Images/{cls}')  # stores list of images in the path 'Images'
        return myList


    except mysql.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

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

# path = "C:/"
# rollno = int(input("Enter roll no: "))
# name = input("Enter name: ")
# pic = input("Enter name of the pic ending with .jpg/.png/.svg: ")
# picPath = os.path.join(path, f"xampp/htdocs/AttendanceFace/Images/{pic}")
# cls = input("Enter class: ")
#
# insertStudent(rollno, name, picPath, cls)

# ml = readStudent('FYBSCCS')
# print(ml)
