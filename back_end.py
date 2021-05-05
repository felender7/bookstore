import sqlite3
class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Books(id  INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")


    # View All Data from database
    def view_all(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    # Search record from the database
    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    # Add Data to the table bookstore
    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()


    # Update records from the database
    def update(self,id,title, author, year,isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?,isbn=? WHERE id=?", (title, author,year,isbn,id,))
        self.conn.commit()


    # Delete records from te database
    def delete(self,id):
        self.cur.execute("DELETE FROM books WHERE id=?",(id,))
        self.conn.commit()


    # Close database connection
    def __delete__(self):
        self.conn.close()
