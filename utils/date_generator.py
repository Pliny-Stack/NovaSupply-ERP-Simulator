from datetime import datetime, timedelta
import random

class DateGenerator:
    """Generates random dates within a specified range."""

    @staticmethod
    def generate_date(start_year: int, end_year: int):
        start = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)

        difference = end - start

        random_days = random.randint(0, difference.days)

        return (start + timedelta(days=random_days)).date()

