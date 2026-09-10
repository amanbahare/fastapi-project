def check_perfect_number(number):
    divisors = []
    if number <= 0:
        return False
    for i in range(1,number):
        if number % i == 0 :
            divisors.append(i)
    if sum(divisors) == number:
        return True
    return False
def check_perfectno_from_list(no_list):
    perfect_num_list = []
    for num in no_list:
        if check_perfect_number(num) == True:
            perfect_num_list.append(num)
    return perfect_num_list
perfectno_list=check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)