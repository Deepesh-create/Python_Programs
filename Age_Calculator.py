import datetime
def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)

#main
date = int(input("Enter the date of your DOB: "))
month = int(input("Enter the month of your DOB: "))
year = int(input("Enter the year of your DOB: "))
ageCalculator(year, month, date)
