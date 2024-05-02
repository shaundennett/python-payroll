import model.pojos as pojos
import services.MainPanel as main
import view.ApplicationTabs as top
from services.UserService import UserService

class MainController:

    user_service = None
    db = ""
    schema = ""
    def __init__(self):
        self.runtime_params()
        self.main()

    def runtime_params(self):
        self.db = "../payroll.db"
        self.schema = "../schema.txt"

    def main(self):

        application = top.ApplicationTabs(self)
    def getUserServces(self) :
        if self.user_service == None:
            self.user_service = UserService(self.db)
        return self.user_service


