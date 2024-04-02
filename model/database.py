import sqlite3
import datetime
from model.pojos import Person, School, Visit, Expense, Invoice, InvoiceItem
def current_sqlite_timestamp():
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format it as a SQLite timestamp (YYYY-MM-DD HH:MM:SS)
    sqlite_timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')

    return sqlite_timestamp


def create_tables(db_file, sql_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    with open(sql_file, 'r') as f:
        sql_commands = f.read()
        cursor.executescript(sql_commands)
    conn.commit()
    conn.close()


def create_person(db_file, person):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO PERSON (name, addressLine1, townCity, postcode, telephone, taxRef, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (person.name, person.addressLine1, person.townCity, person.postcode, person.telephone, person.taxRef,
          current_sqlite_timestamp()))
    conn.commit()
    conn.close()


def create_school(db_file, school):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO SCHOOL (name, addressLine1, townCity, postcode, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (school.name, school.addressLine1, school.townCity, school.postcode, school.timestamp))
    conn.commit()
    conn.close()


def create_visit(db_file, visit):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO VISIT (schoolId, date, ampm, hours, state, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (visit.schoolId, visit.date, visit.ampm, visit.hours, visit.state, visit.timestamp))
    conn.commit()
    conn.close()


def create_expense(db_file, expense):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO EXPENSE (description, value, state, timestamp)
        VALUES (?, ?, ?, ?)
    """, (expense.description, expense.value, expense.state, expense.timestamp))
    conn.commit()
    conn.close()


def create_invoice(db_file, invoice):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO INVOICE (personId, dateSubmitted, datePaid, total, state, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (invoice.personId, invoice.dateSubmitted, invoice.datePaid, invoice.total, invoice.state, invoice.timestamp))
    invoice_id = cursor.lastrowid
    conn.commit()

    # Insert invoice items
    for item in invoice.invoice_items:
        cursor.execute("""
            INSERT INTO INVOICE_ITEM (invoiceId, type, claimId, state, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (invoice_id, item.type, item.claimId, item.state, item.timestamp))

    conn.commit()
    conn.close()


def read_persons(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PERSON")
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_schools(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SCHOOL")
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_visits(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VISIT")
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_expenses(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EXPENSE")
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_invoices(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM INVOICE")
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_complete_invoice(db_file, id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT id,personId,dateSubmitted,datePaid,total,state,timestamp FROM INVOICE")
    rows = cursor.fetchall()
    results = []
    for item in rows:
        results.append(Invoice(item[0],item[1],item[2],item[3],item[4],item[5],item[6]))
    conn.close()
    return results


def update_person(db_file, person):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE PERSON
        SET name=?, addressLine1=?, townCity=?, postcode=?, telephone=?, taxRef=?, timestamp=?
        WHERE id=?
    """, (person.name, person.addressLine1, person.townCity, person.postcode, person.telephone, person.taxRef,
          person.timestamp, person.id))
    conn.commit()
    conn.close()


def update_school(db_file, school):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE SCHOOL
        SET name=?, addressLine1=?, townCity=?, postcode=?, timestamp=?
        WHERE id=?
    """, (school.name, school.addressLine1, school.townCity, school.postcode, school.timestamp, school.id))
    conn.commit()
    conn.close()


def update_visit(db_file, visit):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE VISIT
        SET schoolId=?, date=?, ampm=?, hours=?, state=?, timestamp=?
        WHERE id=?
    """, (visit.schoolId, visit.date, visit.ampm, visit.hours, visit.state, visit.timestamp, visit.id))
    conn.commit()
    conn.close()


def update_expense(db_file, expense):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE EXPENSE
        SET description=?, value=?, state=?, timestamp=?
        WHERE id=?
    """, (expense.description, expense.value, expense.state, expense.timestamp, expense.id))
    conn.commit()
    conn.close()


def update_invoice(db_file, invoice):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE INVOICE
        SET personId=?, dateSubmitted=?, datePaid=?, total=?, state=?, timestamp=?
        WHERE id=?
    """, (invoice.personId, invoice.dateSubmitted, invoice.datePaid, invoice.total, invoice.state, invoice.timestamp,
          invoice.id))

    # Delete existing invoice items
    cursor.execute("DELETE FROM INVOICE_ITEM WHERE invoiceId=?", (invoice.id,))

    # Insert new invoice items
    for item in invoice.invoice_items:
        cursor.execute("""
            INSERT INTO INVOICE_ITEM (invoiceId, type, claimId, state, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (invoice.id, item.type, item.claimId, item.state, item.timestamp))

    conn.commit()
    conn.close()


def delete_person(db_file, person_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PERSON WHERE id=?", (person_id,))
    conn.commit()
    conn.close()


def delete_school(db_file, school_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SCHOOL WHERE id=?", (school_id,))
    conn.commit()
    conn.close()


def delete_visit(db_file, visit_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM VISIT WHERE id=?", (visit_id,))
    conn.commit()
    conn.close()


def delete_expense(db_file, expense_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM EXPENSE WHERE id=?", (expense_id,))
    conn.commit()
    conn.close()


def delete_invoice(db_file, invoice_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM INVOICE WHERE id=?", (invoice_id,))
    conn.commit()
    conn.close()
