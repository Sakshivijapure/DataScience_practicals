import sys
import os
import django
import pandas as pd
from datetime import datetime

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject3.settings')
django.setup()

from streaming.models import NetflixShow

# Correct path to CSV file at project root
csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'netflix_titles.csv')

def parse_date(date_str):
    if pd.isna(date_str):
        return None
    try:
        return datetime.strptime(date_str, "%B %d, %Y").date()
    except ValueError:
        return None

def import_netflix_csv(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    print("Importing Netflix data...")

    for index, row in df.iterrows():
        try:
            obj, created = NetflixShow.objects.update_or_create(
                show_id=row['show_id'],
                defaults={
                    'show_type': row['type'],
                    'title': row['title'],
                    'director': row.get('director', ''),
                    'cast': row.get('cast', ''),
                    'country': row.get('country', ''),
                    'date_added': parse_date(row.get('date_added')),
                    'release_year': int(row['release_year']) if not pd.isna(row['release_year']) else None,
                    'rating': row.get('rating', ''),
                    'duration': row.get('duration', ''),
                    'listed_in': row.get('listed_in', ''),
                    'description': row.get('description', '')
                }
            )
            print(f"{'Created' if created else 'Updated'}: {obj.title}")
        except Exception as e:
            print(f"Error processing row {index}: {e}")

# Run the import
import_netflix_csv(csv_file)

