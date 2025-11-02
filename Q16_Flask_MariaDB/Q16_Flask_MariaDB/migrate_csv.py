import pandas as pd
from db import SessionLocal, Course, Base, engine

CSV_FILE = "coursera_courses_ajax.csv"

# -------------------------------
# Helper: convert review strings to integer
# -------------------------------
def parse_reviews(review_str: str) -> int:
    """Convert review strings like '174K reviews' into integers."""
    if not isinstance(review_str, str):
        return 0
    review_str = review_str.lower().replace('reviews', '').strip()
    multiplier = 1
    if 'k' in review_str:
        multiplier = 1000
        review_str = review_str.replace('k', '').strip()
    elif 'm' in review_str:
        multiplier = 1000000
        review_str = review_str.replace('m', '').strip()
    try:
        return int(float(review_str) * multiplier)
    except ValueError:
        return 0

# -------------------------------
# Main migration function
# -------------------------------
def migrate_csv_to_db():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Load CSV
    df = pd.read_csv(CSV_FILE)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Ensure 'course_name' exists
    if "course_name" not in df.columns:
        print("CSV does not have 'course_name' column. Columns found:", df.columns)
        return

    # Drop duplicates
    df = df.drop_duplicates(subset=["course_name"])

    db = SessionLocal()
    for _, row in df.iterrows():
        exists = db.query(Course).filter_by(course_name=row["course_name"]).first()
        if not exists:
            course = Course(
                course_name=row.get("course_name"),
                provider=row.get("provider"),
                skills=row.get("skills"),
                rating=float(row.get("rating", 0)) if not pd.isna(row.get("rating")) else 0,
                total_reviews=parse_reviews(row.get("total_reviews", 0)),
                level=row.get("level"),
                duration=row.get("duration")
            )
            db.add(course)

    db.commit()
    db.close()
    print("✅ Migration completed! CSV data inserted into MariaDB.")


# -------------------------------
# Run migration
# -------------------------------
if __name__ == "__main__":
    migrate_csv_to_db()
