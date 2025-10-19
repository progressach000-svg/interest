from nepali_datetime import date
#fn for input:
def take_bs():
    year = int(input("year: "))
    month = int(input("MOnth: "))
    day = int(input("Days: "))
    return date(year,month,day)
#input dates in BS:
print("Give past BS date: ")
bs1 = take_bs()
print("Give present BS date: ")
bs2 = take_bs()
#bs2ad conversion:
#ad1 = bs1.to_datetime_date()
#ad2 = bs2.to_datetime_date()
#Taking amount_value:
P = float(input("Enter the principal amount: "))
#days finding:
days_diff = (bs2-bs1).days
print("Total days of Interest:",days_diff)
#days2year conversion:
T = days_diff/365
R = 0.13
#calc of due year, month and days:
def due(days):
    year = days//365
    month = (days%365)//30
    rem_days = (days%365)%30
    return year,month,rem_days
print("Due year, month and days: %d-%d-%d"%(due(days_diff)))
print("time in year: ",T)
#calc of interest (13%):
interest = P*T*R
print("Interest: ",interest)
ch = input("enter any key to end: ")

