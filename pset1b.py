salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Part of salary you want to save, in decimal: "))
cost = int(input("Enter cost of your dream home: "))
incr = float(input("Enter every 6 month raise in decimal: "))

down_payment = 0.25 * cost
monthly_salary=salary/12

month = 0
savings = 0.0

while savings < down_payment:
    interest = savings*0.04/12
    savings = savings + interest

    if month%6==0 and month != 0:
        increment = monthly_salary*incr
        monthly_salary = monthly_salary + increment
    
    savings = savings + portion_saved*monthly_salary
    month+=1


print ("months:", month)