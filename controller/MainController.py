import mysql.connector
from database.User import User
from database.UserService import UserSservice

class MainController:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="payroll"
        )

        self.createServices()

    def createServices(self):

        self.user = User("a","b","c","d")
        self.userService = UserSservice(self.conn)

    def fetchUsers(self):
        result = self.userService.getById(1)
        print("hello")

