import mysql.connector

class UserSservice:
    query_find_all = "SELECT id, firstname, lastname, payroll_id, status FROM User"
    where_id = "WHERE id = %s"


    def __init__(self, connection):
        self.myconnection = connection

    def getAll(self):
        cursor = self.myconnection.cursor()

        cursor.execute(self.query_find_all)

        cursor.close()

    def getById(self, id):
        cursor = self.myconnection.cursor()
        statement = self.query_find_all + " " + self.where_id
        print(statement)
        result = []
        try:
            cursor.execute(statement, (id,))
            # Fetch and print results

            for row in cursor.fetchall():
                print(row)
                result.append(row)
        except ValueError as e:
            print(e)
        finally:
            cursor.close()
            return result


