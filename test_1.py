
"""
The program is trying to determin which payment option is better (more money).
First option is 100 dollers per day for 10 days; Second option is 
for 1 doller a day with it being doubled each day for 10 days. There
will be two functions to calculate, the pay rate.
function1 will calculate the amount for the first option, function2
will calculate for the second option

function1 will output $100 x 10 days.
funchtion2 will loop 10 times, with each time doubling the amount and add the amount to the total

if the amount is equal, we output to the user "Option 1 and Option 2 pays the same"
if the Option1 is better, we output to the user "Option1 is better"
if the Option2 is better, we output to the user "Option2 is better"
"""

"""
# option1
    return 100 * 10
# option2
    amount = 1
    list1 = []
    loop 10 times
        add amount to list
        amount *= 2
    sum = sum of all items in loop
    return amount
# main
var1 = option1
var2 = option2

if var1 = var2
    "Option 1 and Option 2 pays the same"
if var1 > var2
    "Option 1 is better"
else
    "Option 2 is better"

main
"""

def option1():
    return 100 * 10

def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    # print("list1", list1) = is verrification of list working
    total = sum(list1)
    return total

def main():
    answer = ""
    var1 = option1()  # 100 * 10 = 1000
    var2 = option2()  # addition of list1 = 1023
    # print("from main: car1", var1, "var2", var2) = testing
    if var1 == var2:
        answer = "Option 1 and Option 2 pay the same!"
    elif var1 > var2:
        answer = "Option 1 is better!"
    else:
        answer = "Option 2 is better!"
    print(answer)

# var1 = option1() = testing
# var2 = option2()
# print(var1)
# print(var2)


main()