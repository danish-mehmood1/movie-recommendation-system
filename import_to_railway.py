import pandas as pd
from database.connection import get_connection

conn = get_connection()
cursor = conn.cursor()

files = [
    ("movies", "data/movies.csv"),
    ("ratings", "data/ratings.csv"),
    ("links", "data/links.csv"),
    ("tags", "data/tags.csv"),
]

BATCH_SIZE = 1000

for table, file in files:
    print(f"\nImporting {table}...")

    # CSV read
    df = pd.read_csv(file)

    # NaN ko MySQL NULL me convert karo
    df = df.astype(object).where(pd.notnull(df), None)

    # Table clean karo
    cursor.execute(f"DELETE FROM {table}")
    conn.commit()

    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))

    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    data = df.values.tolist()

    # Batch import
    for i in range(0, len(data), BATCH_SIZE):
        batch = data[i:i + BATCH_SIZE]

        cursor.executemany(sql, batch)
        conn.commit()

        print(f"{table}: {min(i+BATCH_SIZE, len(data))}/{len(data)}")

    print(f"✅ {len(df)} rows imported into {table}")


cursor.close()
conn.close()

print("\n🎉 All data imported successfully!")