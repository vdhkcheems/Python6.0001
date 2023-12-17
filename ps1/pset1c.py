x = int(input('Enter your annual salary: '))

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25*1000000
current_savings = 0.00

months = 0

low = 0
high = 10000

steps = 0
annual_salary = x
while True:
    guess = (low + high)//2
    while (portion_down_payment - current_savings) > 100.0:
        if months % 6 == 0 and months!=0:
            annual_salary += annual_salary * semi_annual_raise
        
        current_savings += (current_savings*(r/12)) + (annual_salary/12)*(guess/10000)
        months += 1
    if months > 36:
        low = guess
        annual_salary = x
        months = 0
        current_savings = 0
    elif months < 36:
        high = guess
        annual_salary = x
        months = 0
        current_savings = 0
    else:
        optimumRate = guess / 10000
        possible = True
        break
    steps +=1
    if guess == 9999:
        possible = False
        break

if possible:
    print('Best savings rate: ', optimumRate)
    print('Steps in bisection search: ', steps)
else:
    print('At this salary, it is not possible to save the down payment in 36 months.')