import mysql.connector
from keys import host, user, password, database
import json

mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)


cursor = mydb.cursor()

#Deleting already created tables
cursor.execute("DROP TABLE IF EXISTS Personal")
cursor.execute("DROP TABLE IF EXISTS Link")
cursor.execute("DROP TABLE IF EXISTS Address")
cursor.execute("DROP TABLE IF EXISTS Bookshelf")
cursor.execute("DROP TABLE IF EXISTS Student")
cursor.execute("DROP TABLE IF EXISTS Grade")
cursor.execute("DROP TABLE IF EXISTS Class")
cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")


#Creating new tables
cursor.execute("CREATE TABLE Grade(grade_id INT PRIMARY KEY AUTO_INCREMENT, grade VARCHAR(255) );")
cursor.execute("CREATE TABLE Student(student_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(255), last_name VARCHAR(255), old int, Grade_id INT, FOREIGN KEY(Grade_id) REFERENCES Grade(grade_id));")
cursor.execute("CREATE TABLE Class(class_id INT PRIMARY KEY AUTO_INCREMENT, class_name VARCHAR(255));")
cursor.execute("CREATE TABLE Bookshelf(bookshelf_id INT PRIMARY KEY AUTO_INCREMENT, shelf_no INT, Student_id INT, FOREIGN KEY(Student_id) REFERENCES Student(student_id) );")
cursor.execute("CREATE TABLE Personal(personal_id INT PRIMARY KEY AUTO_INCREMENT, person_id INT, Student_id INT, FOREIGN KEY(Student_id) REFERENCES Student(student_id));")
cursor.execute("CREATE TABLE Link(student_id INT NOT NULL, class_id INT NOT NULL, PRIMARY KEY (student_id,class_id),class_name VARCHAR(255), FOREIGN KEY(student_id) REFERENCES Student(student_id), FOREIGN KEY(class_id) REFERENCES Class(class_id));")
cursor.execute("CREATE TABLE Address(address_id INT PRIMARY KEY AUTO_INCREMENT, country VARCHAR(255), city VARCHAR(255), street VARCHAR(255), number int, Student_id INT, FOREIGN KEY(Student_id) REFERENCES Student(student_id));")


#Inserting values into tables
cursor.execute("INSERT INTO Class(class_name) VALUES ('Mathematics');")
class_1 = cursor.lastrowid
cursor.execute("INSERT INTO Class(class_name) VALUES ('Physics');")
class_2 = cursor.lastrowid
cursor.execute("INSERT INTO Class(class_name) VALUES ('Algebra');")
class_3 = cursor.lastrowid
cursor.execute("INSERT INTO Class(class_name) VALUES ('Mechanics');")
class_4 = cursor.lastrowid 
cursor.execute("INSERT INTO Grade(grade) VALUES ('FAILED');")
cursor.execute("INSERT INTO Grade(grade) VALUES ('VERY BAD');")
cursor.execute("INSERT INTO Grade(grade) VALUES ('BAD');")
cursor.execute("INSERT INTO Grade(grade) VALUES ('GOOD');")
cursor.execute("INSERT INTO Grade(grade) VALUES ('EXCELLENT');")
cursor.execute("INSERT INTO Student(first_name, last_name, old, grade_id) VALUES ('Johny','Nicke',24, 5);")
student_id = cursor.lastrowid
cursor.execute("INSERT INTO Link(student_id, class_id)  VALUES (%s, %s)", (student_id, class_1))
cursor.execute("INSERT INTO Link(student_id, class_id)  VALUES (%s, %s)", (student_id, class_4))
cursor.execute("INSERT INTO Personal(person_id, Student_id) VALUES (%s, %s)", (6200457, student_id))
cursor.execute("INSERT INTO Address(country, city, street, number, Student_id) VALUES ('New York', 'New York City', 'Broadway', '10', 1);")
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (200, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (205, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (210, student_id))
# print(student_id)

cursor.execute("INSERT INTO Student(first_name, last_name, old, grade_id) VALUES ('Michael','Helothin',18,2);")
student_id = cursor.lastrowid
cursor.execute("INSERT INTO Address(country, city, street, number, Student_id) VALUES ('Alabama', 'Montgomery', ' Antioch Lane', '9', 2);")
cursor.execute("INSERT INTO Link(student_id, class_id)  VALUES (%s, %s)", (student_id, class_1))
cursor.execute("INSERT INTO Link(student_id, class_id)  VALUES (%s, %s)", (student_id, class_2))
cursor.execute("INSERT INTO Personal(person_id, Student_id) VALUES (%s, %s)", (6200458, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (201, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (204, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (207, student_id))

# print(student_id)

cursor.execute("INSERT INTO Student(first_name, last_name, old, grade_id) VALUES ('Gregor','McTycoon',49, 5);")
student_id = cursor.lastrowid
cursor.execute("INSERT INTO Address(country, city, street, number, Student_id) VALUES ('Alabama', 'Montgomery', 'Dexter Avenue', '24', 3);")
cursor.execute("INSERT INTO Link(student_id, class_id)  VALUES (%s, %s)", (student_id, class_2))
cursor.execute("INSERT INTO Link(student_id, class_id)  VALUES (%s, %s)", (student_id, class_3))
cursor.execute("INSERT INTO Personal(person_id, Student_id) VALUES (%s, %s)", (6200459, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (202, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (206, student_id))
cursor.execute("INSERT INTO Bookshelf(shelf_no, Student_id)  VALUES (%s, %s)", (209, student_id))

# print(student_id)
mydb.commit()

sql = "SELECT  \
  Student.first_name AS name, \
  Student.last_name AS lname, \
  Student.old AS old, \
  Address.country AS country, \
  Address.city AS city, \
  Address.street AS street, \
  Address.number AS number, \
  Personal.person_id AS ID, \
  GROUP_CONCAT(DISTINCT Bookshelf.shelf_no separator ', ' ) AS shelf_no, \
  GROUP_CONCAT(DISTINCT Class.class_name separator ', ' ) AS class, \
  Grade.grade AS grade \
  FROM Address \
  INNER JOIN Student ON Address.Student_id = Student.student_id \
  INNER JOIN Personal ON Personal.Student_id = Student.student_id \
  INNER JOIN Grade ON Grade.grade_id = Student.Grade_id \
  INNER JOIN Link ON Student.student_id = Link.student_id  \
  INNER JOIN Class ON Link.class_id = Class.class_id \
  INNER JOIN Bookshelf ON Bookshelf.Student_id = Student.student_id \
  GROUP BY Student.student_id "
   
cursor.execute(sql)
myresult = cursor.fetchall()
payload = []
content = {}
for x in myresult:
  content = {'First name': x[0], 'Last name': x[1], 'Years': x[2], 'Country': x[3], 'City': x[4], 'Street': x[5], 'Street number': x[6], 'Unique identity number': x[7], 'Occupied Bookshelf(s)': x[8], 'Classes': x[9], 'Grade': x[10]}
  payload.append(content)
  content = {}

print(json.dumps(payload))











