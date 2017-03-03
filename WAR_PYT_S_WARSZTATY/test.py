from models.user import User
from mysql.connector import connect



user = 'root'
password = 'coderslab'
host = 'localhost'
database = 'workshop_db'

def testCreateUser():

    cnx = connect(user=user, password=password, host=host, database=database)
    print("Connected")
    cursor = cnx.cursor()

    new_user = User()
    print("id nowego usera to {}".format(new_user.id))
    new_user.name = "Ada"
    new_user.email = "ada@gmail.com"
    new_user.set_password("dupa123")

    success = new_user.save_to_db(cursor, cnx)
    new_id = new_user.id
    print("Udalo sie: {}  nowe id to {}".format(success, new_id))


def testLoadUser():

    cnx = connect(user=user, password=password, host=host, database=database)
    print("Connected")
    cursor = cnx.cursor()

    loaded_user = User.load_user_by_id(cursor, 5)
    loaded_user.printInfo()
   
   
def testLoadAll():

    cnx = connect(user=user, password=password, host=host, database=database)
    print("Connected")
    cursor = cnx.cursor()

    loaded_users = User.load_all(cursor)
    for loaded_user in loaded_users:
        loaded_user.printInfo()
   
if __name__ == "__main__":
    testLoadAll()
