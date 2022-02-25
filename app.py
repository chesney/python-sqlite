import logging
import sqlite3
from contextlib import contextmanager

@contextmanager
def open_database(filename: str):
    logging.info('Open DB connection')
    connection = sqlite3.connect(filename)
    try:
        cursor = connection.cursor()
        yield cursor
    except sqlite3.DatabaseError as err:
        logging.error('Database error: %s', err)
    finally:
        logging.info('Close DB connection')
        connection.commit()
        connection.close()

def db_exec(query: str, args=()):
    with open_database('test.db') as cursor:
        cursor.execute(query, args)
        return cursor.fetchall()

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting app')
    print('App started')

    db_exec("insert into blog (title, content, author) values (?, ?, ?)", ('Test', 'Test content', 'joe'));
    
    # The values of the row BEFORE the update.
    before = db_exec("SELECT id, title, content, author FROM blog where id = ?", [1])
    for row in before:
        print(row)

    # Update the row.
    db_exec("UPDATE blog SET title=?, content=? where id = ?", ["A brand new World!","Learning new things", 1])
    
    # The values of the row AFTER the update.
    after = db_exec("SELECT id, title, content, author FROM blog where id = ?", [1])
    for row in after:
        print(row)

if __name__ == '__main__':
    main()
