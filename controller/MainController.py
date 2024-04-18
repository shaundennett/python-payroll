import mysql.connector

from services.UserService import UserSservice

class MainController:

    db = ""
    schema = ""
    def __init__(self):
        self.runtime_params()
    def runtime_params(self):
        self.db = "../payroll.db"
        self.schema = "../schema.txt"