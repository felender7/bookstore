
# Bookstore Manager - Desktop APP
A program that store book information

User can :
* View all records
* Search entry
* Add entry
* Update entry
* Delete

![Imgur](https://i.imgur.com/IRhO5bY.png?1)

## Getting Started
Bookstore App Manager Build with Python, Tkinter and sqlite3


#### Requirements

You'll need the following installed to run the application successfully:
* Python 3
* TKinter
* sqlite3

To use postgres, download it from the official website [https://www.postgresql.org/download/]
* psycopg2 - `pip install psycopg2`

Change `self.conn = sqlite3.connect(db)` to  `self.conn = psycopg2.connect(db)`

#### Generate executable file

* pyinstaller - `pip install pyinstaller`
* Run - `pyinstaller --onefile[optional] --windowed[optional] front_end.py `
* For more information visit the link `https://pyinstaller.readthedocs.io/en/stable/`
