from database.connection import get_connection

try:
    conn = get_connection()

    print("✅ Database connected successfully")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM movies")
    print("Movies:", cursor.fetchone()[0])

    cursor.execute("SELECT COUNT(*) FROM ratings")
    print("Ratings:", cursor.fetchone()[0])

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)