from model.pojos import Person, School, Visit, Expense, Invoice, InvoiceItem
import model.database as database


class UserService:

    def __init__(self, db):
        self.db = db

    def get_all_person(self):

        database.list_tables(self.db)

        result = []
        rows = database.read_persons(self.db)
        for item in rows:
            result.append(Person(*item))

        return result

if __name__ == "__main__":
    serviec = UserService("../payroll.db")

    result = serviec.get_all_person()
    print(result[0].get_data())
