import psycopg2

conn = psycopg2.connect(
      host="ep-raspy-cake-a4er20z3-pooler.us-east-1.aws.neon.tech",
      database="neondb",
      user='neondb_owner',
      password="npg_Aj9IicxVR6Og"
)

cur = conn.cursor()

cur.execute('''
      CREATE TABLE IF NOT EXISTS page_counter (
            id SERIAL PRIMARY KEY,
            count INTEGER NOT NULL DEFAULT 0
            );
      ''')
cur.execute('INSERT INTO page_counter (count) VALUES (1, 0) ON CONFLICT DO NOTHING;')
conn.commit()
cur.close()
conn.close()