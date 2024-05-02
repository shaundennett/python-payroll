from model.pojos import Person, School, Visit, Expense, Invoice, InvoiceItem


import model.database as database


class UserService:

    def __init__(self, db):
        self.db = db

    def get_all_person(self):

        result = []
        rows = database.read_persons(self.db)
        for item in rows:
            result.append(Person(*item))

        return result

