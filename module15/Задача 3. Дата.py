from datetime import datetime

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"

    @classmethod
    def from_string(cls, date_string):
        if cls.is_date_valid(date_string):
            day, month, year = map(int, date_string.split('-'))
            return cls(day, month, year)
        else:
            raise ValueError("Неверный формат даты")

    @staticmethod
    def is_date_valid(date_string):
        try:
            day, month, year = map(int, date_string.split('-'))
            datetime(year, month, day)
            return True
        except ValueError:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))