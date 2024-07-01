from datetime import date, datetime

date_str = input("Введіть дату в форматі 'PPPP-MM-ДД': ")

def get_days_from_today(date):
    today = datetime.today()
    iso_date = datetime.fromisoformat(date)
    days_from_today = (iso_date - today).days
    return days_from_today
try:
    print(f"{get_days_from_today(date_str)} days from today")
except ValueError:
    print("Invalid date")
    print("Try to print your date like this date: 2024-06-24")