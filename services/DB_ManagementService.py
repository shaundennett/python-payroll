from model.pojos import Person, School, Visit, Expense, Invoice, InvoiceItem
import model.database as database


class DB_ManagementService:

    def __init__(self, db, schema):
        self.db = db
        self.schema = schema
        self.create_database()
    def create_database(self):

        database.create_tables(self.db, self.schema)


if __name__ == "__main__":
    db = "../payroll-test.db"
    schema = "../schema.txt"
    servie = DB_ManagementService(db,schema)