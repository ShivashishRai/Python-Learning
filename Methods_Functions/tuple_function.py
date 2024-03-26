
def max_work_hours(emp_data):
    max_price = 0
    best_par = ''

    for emp , data in emp_data:
        if data > max_price:
            max_price = data
            best_par = emp
    print(f"The best Emp for the month is {best_par} with work hour {max_price}")

emp_data = (["Shiva", 500], ["Ishu", 507] , ["Appu", 119], ["Kaju", 503])
max_work_hours(emp_data)