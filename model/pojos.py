
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
    def __str__(self):
        return f"Person(id={self.id}, name='{self.name}', addressLine1='{self.addressLine1}', townCity='{self.townCity}', postcode='{self.postcode}', telephone='{self.telephone}', taxRef='{self.taxRef}', timestamp='{self.timestamp}')"
    def get_data(self) -> ():

        data = (self.id,self.name,self.addressLine1, self.townCity, self.postcode, self.telephone, self.taxRef, self.timestamp)
        return data

class School:
    def __init__(self, id, name, addressLine1, townCity, postcode, timestamp):
        self.id = id
        self.name = name
        self.addressLine1 = addressLine1
        self.townCity = townCity
        self.postcode = postcode
        self.timestamp = timestamp
    def __str__(self):
        return f"School(id={self.id}, name='{self.name}', addressLine1='{self.addressLine1}', townCity='{self.townCity}', postcode='{self.postcode}', timestamp='{self.timestamp}')"

class Visit:
    def __init__(self, id, schoolId, date, ampm, hours, state, timestamp):
        self.id = id
        self.schoolId = schoolId
        self.date = date
        self.ampm = ampm
        self.hours = hours
        self.state = state
        self.timestamp = timestamp
    def __str__(self):
        return f"Visit(id={self.id}, schoolId={self.schoolId}, date='{self.date}', ampm='{self.ampm}', hours={self.hours}, state='{self.state}', timestamp='{self.timestamp}')"

class Expense:
    def __init__(self, id, description, value, state, timestamp):
        self.id = id
        self.description = description
        self.value = value
        self.state = state
        self.timestamp = timestamp
    def __str__(self):
        return f"Expense(id={self.id}, description='{self.description}', value={self.value}, state='{self.state}', timestamp='{self.timestamp}')"

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
    def __str__(self):
        return f"Invoice(id={self.id}, personId={self.personId}, dateSubmitted='{self.dateSubmitted}', datePaid='{self.datePaid}', total={self.total}, state='{self.state}', timestamp='{self.timestamp}', invoiceItems={self.invoice_items})"
class InvoiceItem:
    def __init__(self, id, invoiceId, type, claimId, state, timestamp):
        self.id = id
        self.invoiceId = invoiceId
        self.type = type
        self.claimId = claimId
        self.state = state
        self.timestamp = timestamp
    def __str__(self):
        return f"InvoiceItem(id={self.id}, invoiceId={self.invoiceId}, type='{self.type}', claimId={self.claimId}, state='{self.state}', timestamp='{self.timestamp}')"


