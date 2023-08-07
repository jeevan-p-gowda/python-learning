name = "Jeevan"
age = 27
salary = 100
dic = {'name': 'Jeevan', 'age': 27, 'salary': 100}
pi = 3.14159265
my_list = range(0, 10)

# Approach 1 - Using comma
print("Name is:", name, "Age is:", age, "Salary is:", salary)

# Approach 2 - Using format
# %s - String, %d - Integer, %g - decimal
print("Name is:%s Age is:%d Salary is:%g" % (name, age, salary))

# Approach 3 - Curly Braces
print("Name is:{} Age is:{} Salary is:{}".format(name, age, salary))
# Can pass any data structure
print("Name is:{0[name]} Age is:{0[age]} Salary is:{0[salary]}".format(dic))
# Can pass positional args
print("Name is:{name} Age is:{age} Salary is:{salary}".format(name='Jeevan', age=27, salary=900))
# auto-searches the key in dic and fetches the value accordingly
print("Name is:{name} Age is:{age} Salary is:{salary}".format(**dic))
# control decimal values
print("pi value is {:.2f}".format(pi))
# control 0's
for i in my_list:
    print('The value is {:02}'.format(i))
# control separators like comma, dot etc
print('The value of 1 MegaByte is {:,}'.format(1000 ** 2))
print('The value of 1 MegaByte is {:,.2f}'.format(1000 ** 2))
# handle datetime
import datetime
my_date = datetime.datetime(2023, 7, 31, 2, 24, 00)
print('Current datetime is {:%B %d,%Y}'.format(my_date))
print('{0:%B %d,%Y} fell on a {0:%A} which is {0:%j} day of the year'.format(my_date))
