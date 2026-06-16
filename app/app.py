import psycopg2
import os
import datetime

def main():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'testdb'),
        user=os.getenv('DB_USER', 'testuser'),
        password=os.getenv('DB_PASSWORD', 'testpass')
    )
    cur = conn.cursor()
    cur.execute('SELECT version();')
    version = cur.fetchone()[0]
    print(f'Connected to PostgreSQL: {version}')
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()

print(f'Current time: {datetime.datetime.now()}')
