from datetime import date
from application.salary import calculate_salary
from application.bd.people import get_employees


if __name__ == "__main__":
    print(f"{date.today():%d-%m-%Y}")
    calculate_salary()
    get_employees()
