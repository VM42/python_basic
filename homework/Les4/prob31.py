# tried to create file with all my functions but screwed up somewhere so used old way

from sys import argv
# from some_func_for_les4.py import paycheck

script_name, work_hrs, pay_hrs, extra_pay = argv

try:
    paycheck = work_hrs * pay_hrs + extra_pay
    print(f'Your salary is: {paycheck} CAD')
except ValueError:
    print('Not a number')

