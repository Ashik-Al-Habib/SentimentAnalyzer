import csv
import os
from django.conf import settings
from SentimentAnalyzer.models import ProductReview


def load_csv_data(csv_file_path):

    csv_file_path = '/Users/ashikalhabib/Desktop/test/merger_v2.csv'
    if os.path.exists(csv_file_path):
        print("File exists")
    else:
        print("File does not exist")
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ProductReview.objects.create(
                score=row['score'],
                product_id=row['P_ID'],
                label=row['Label'],
                review=row['Review']
            )

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SentimentAnalyzer.settings')
    import django
    django.setup()

    csv_file_path = r'/Users/ashikalhabib/Desktop/test/merger_v2.csv'
    load_csv_data(csv_file_path)
