
class Person:
    def __init__(self, id, name, addressLine1, townCity, postcode, telephone, taxRef, timestamp):
        self.id = id
        self.name = name
        self.addressLine1 = addressLine1
        self.townCity = townCity
        self.postcode = postcode
        self.telephone = telephone
        self.taxRef = taxRef
        self.timestamp = timestamp

class School:
    def __init__(self, id, name, addressLine1, townCity, postcode, timestamp):
        self.id = id
        self.name = name
        self.addressLine1 = addressLine1
        self.townCity = townCity
        self.postcode = postcode
        self.timestamp = timestamp

class Visit:
    def __init__(self, id, schoolId, date, ampm, hours, state, timestamp):
        self.id = id
        self.schoolId = schoolId
        self.date = date
        self.ampm = ampm
        self.hours = hours
        self.state = state
        self.timestamp = timestamp

class Expense:
    def __init__(self, id, description, value, state, timestamp):
        self.id = id
        self.description = description
        self.value = value
        self.state = state
        self.timestamp = timestamp

class Invoice:
    def __init__(self, id, personId, dateSubmitted, datePaid, total, state, timestamp):
        self.id = id
        self.personId = personId
        self.dateSubmitted = dateSubmitted
        self.datePaid = datePaid
        self.total = total
        self.state = state
        self.timestamp = timestamp
        self.invoice_items = []

    def add_invoice_item(self, invoice_item):
        self.invoice_items.append(invoice_item)

class InvoiceItem:
    def __init__(self, id, invoiceId, type, claimId, state, timestamp):
        self.id = id
        self.invoiceId = invoiceId
        self.type = type
        self.claimId = claimId
        self.state = state
        self.timestamp = timestamp


