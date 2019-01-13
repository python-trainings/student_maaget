import psycopg2

class DB:
    def __init__(self,user = "admin", password = "1234",database = "esdata"):
        try:    
            self.connection = psycopg2.connect(database=database,user=user, password=password)
            self.cursor =  self.connection.cursor()
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

    def fetch(self,query):
        try:
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            return record
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to fetching", error)

    # "SELECT * from student;"
    # for i in range(10):
    #     cmd = "insert into student(name,age, gender, contact_no, course, address, qualification_10, qualification_12) values ('subham', 20, 'M', '999222833%s', 'IT', 'blore', 90, 80);" % i
    #     cursor.execute(cmd)
    # cursor.execute("SELECT * from student;")
    # record = cursor.fetchall()
    # for item in record:
    #   print item
    # connection.commit()
    # # print("You are connected to - ", type(record),"\n")
# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
# finally:
    def close(self):
        #closing database connection.
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")