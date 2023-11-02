from custom_lib import password_generator as pg
import sqlite3

# db connect
connection = sqlite3.connect('pass_db.db')
cursor = connection.cursor()
# creating new tab
cursor.execute("""CREATE TABLE IF NOT EXISTS Password_control (
name TEXT VARCHAR,
value TEXT NOT NULL
)""")
# commit
connection.commit()


def deleter():
    while True:
        print("""       delete""")
        outputer()
        delete = input('Write name of password which you would like to delete: ')
        cursor.execute("DELETE FROM Password_control WHERE name = ?",
                       (delete,))
        connection.commit()
        return


def refactorer():
    while True:
        print("""       refactor
1. Refactor name
2. Refactor password""")
        refactor = int(input('Write what type of refactor you would like to do: '))
        if refactor == 1:
            outputer()
            passvalue = input('Write please key of password: ')
            new_name = input('Write please new name of password: ')
            cursor.execute("UPDATE Password_control SET name = ? WHERE value = ?",
                           (new_name, passvalue))
            connection.commit()
        elif refactor == 2:
            outputer()
            passname = input('Write please name of password: ')
            x = int(input('Write a lenght of password(min 10 recomended): '))
            new_value = pg.passgen(x)
            cursor.execute("UPDATE Password_control SET value = ? WHERE name = ?",
                           (new_value, passname))
            connection.commit()
            return


def outputer():
    while True:
        # output
        cursor.execute("SELECT * FROM Password_control")
        output = cursor.fetchall()
        print(output)
        return


def adder():
    while True:
        # calling values
        db_name = input('Write please the name of password: ')
        x = int(input('Write a lenght of password(min 10 recomended): '))
        db_value = pg.passgen(x)
        # add values into db
        cursor.execute("INSERT INTO Password_control (name, value) VALUES(?, ?)",
                       (db_name, db_value))
        # commit
        connection.commit()
        return


def menu():
    while True:
        print("""       menu
1. Add new password
2. Refactor password
3. Delete password
4. Output""")
        command = int(input('What would you like to do(exit=0): '))
        if command == 1:
            adder()
        elif command == 2:
            refactorer()
        elif command == 3:
            deleter()
        elif command == 4:
            outputer()
        elif command == 0:
            exit()


menu()
connection.close()
