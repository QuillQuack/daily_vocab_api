from sqlalchemy import create_engine

# ใช้ DATABASE_URL เดียวกับใน FastAPI
DATABASE_URL = "mysql+pymysql://vocabuser:vocabpass123@mysql:3306/vocabulary_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("Database connection successful:", result.fetchall())
except Exception as e:
    print("Database connection failed:", e)
