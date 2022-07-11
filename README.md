# MYSQL-concept_impl

MYSQL database container is running on Docker host. Program connects to database via
mysql.connector.connect, with corresponding parameters initialized on another file because of security. 
This program contains the following tables:
Grade | Student | Class | Bookshelf | Personal | Link | Address.
1. Grade table acts as a look up table, consisting of 5 different values: FAILED(1), VERY BAD(2), BAD(3), GOOD(4), EXCELLENT(5), assigned on each student. Benefit of using look up table, compared to adding a column on Student table is if we want to change for ex. FAILED into FAILURE we only change it to Grade table, instead of changing N number of times in Student table, where N is the number of students that have FAILED. 
2. Student address is an attribute to the Student, but following 1NF(First Normal Form), country/city/street/number must be seperated into different columns. But because they are attributes to the address, proper way is to store them in seperate table named Address table(3NF), with Foreign key reference to Student PRIMARY KEY.
3. There are 3 types of db relationships: one to one, one to many and many-to-many 
4. One-to-one relationship is made between Student table and Personal table. Personal table contains unique Student identity number. In other words, each Student can have only one unique identity number, and one unique identity number can be owned by only one Student.
5. One-to-many relationship is made between Student table and Bookshelf table. Here, one Student can occupy multiple bookshelfs, whereas one bookshelf can be occupied by only one Student.
6. Many-to-many relationship is made between Student table and Class table. In other words, each Student can be enrolled in multiple classes, and each Class can be followed by multiple Students. This relationship is done using Intermediate table named Link. In each row of Link table, there are 2 columns(STUDENT PRIMARY KEY | CLASS PRIMARY KEY). So, many-to-many relationship, can be split into 2 one-to-many relationships, i.e. Student-Link and Class-Link. 
7. Final goal is to combine all information from all tables per Student, using INNER JOIN(without duplicating data). Joining can be done with OUTER JOIN.
8. ![Difference-between-Inner-and-Outer-Join-in-SQL](https://user-images.githubusercontent.com/75247159/178321897-82813375-39f2-40d4-8b80-9f548957750b.jpg)
