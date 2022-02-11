import logging
import sqlite3

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting app')
    print('App started')

    logging.info('Open DB connection')
    connection = sqlite3.connect('test.db')

    try:
        logging.info('Select data')
        cursor = connection.execute('''SELECT * FROM blog''')
        for row in cursor:
            print(row)
    finally:
        logging.info('Close DB connection')
        connection.close()

if __name__ == '__main__':
    main()
