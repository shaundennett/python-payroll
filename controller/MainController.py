import model.pojos as pojos
from view.ApplicationTabs import ApplicationTabs
from services.UserService import UserService
from services.DB_ManagementService import DB_ManagementService

class MainController:

    user_service = None
    db = ""
    schema = ""
    def __init__(self, db, schema):
        self.runtime_params(db, schema)
        self.user_service = UserService(self.db)
        self.db_utils = DB_ManagementService(self.db, self.schema)

        self.main()

    def runtime_params(self, db,schema):

        self.db = db
        self.schema = schema

    def initialize_database(self):
        print("initialize the database...")
        self.db_utils.create_database(self.db, self.schema)
    def main(self):
        #application = ApplicationTabs(self)
        print("hello world")


if __name__ == "__main__":
    db = "../payroll-test.db"
    schema = "../schema.txt"
    controllser = MainController(db,schema)

