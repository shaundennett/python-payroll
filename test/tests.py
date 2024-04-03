
from model.pojos import Person, School, Visit, Expense, Invoice, InvoiceItem
import model.database as database

def test_create_and_read_person(db):
    person = Person(None, 'John Doe', '123 Main St', 'Anytown', '12345', '555-1234', '123-456-789', '2022-02-16')
    database.create_person(db, person)
    persons = database.read_persons(db)
    print("Persons:")
    for person in persons:
        print(person)

def test_create_and_read_school(db):
    school = School(None, 'XYZ School', '456 Elm St', 'Othertown', '54321', '2022-02-16')
    database.create_school(db, school)
    schools = database.read_schools(db)
    print("Schools:")
    for school in schools:
        print(school)

def test_create_and_read_visit(db):
    visit = Visit(None, 1, '2022-02-16', 'AM', 2, 'Scheduled', '2022-02-16')
    database.create_visit(db, visit)
    visits = database.read_visits(db)
    print("Visits:")
    for visit in visits:
        print(visit)

def test_create_and_read_expense(db):
    expense = Expense(None, 'Office supplies', 50.00, 'Pending', '2022-02-16')
    database.create_expense(db, expense)
    expenses = database.read_expenses(db)
    print("Expenses:")
    for expense in expenses:
        print(expense)

def test_create_and_read_invoice(db):
    invoice = Invoice(None, 1, '2022-02-16', None, 100.00, 'Pending', '2022-02-16')
    invoice_item = InvoiceItem(None, 1, 'Product', 1, 'Pending', '2022-02-16')
    invoice.add_invoice_item(invoice_item)
    database.create_invoice(db, invoice)

    invoices = database.read_complete_invoice(db,4)
    print("Invoices:")
    for invoice in invoices:
        print(invoice)

def main(db):
    database.create_tables(db, "../schema.txt")
    test_create_and_read_person(db)
    test_create_and_read_school(db)
    test_create_and_read_visit(db)
    test_create_and_read_expense(db)
    test_create_and_read_invoice(db)

if __name__ == "__main__":
    main("../payroll.db")
