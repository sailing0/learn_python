# 5. 扩展练习(定义函数，返回指定范围内的素数)
# 例如：１－－１００　　

# def get_prime(bengin,end):
#     list_prime = []
#     for number in range(bengin,end+1):
#         if number < 2:
#             pass
#         else:
#             for i in range(2, number):
#                 if number % i == 0:
#                     break  # 如果有结论了,就不需要在和后面的数字比较了
#             else:
#                 list_prime.append(number)
#     return list_prime


def get_prime(bengin, end):
    """
        生成指定范围内的所有素数
    :param bengin: 开始
    :param end: 结束
    :return: 范围内的所有素数
    """
    list_prime = []
    for number in range(bengin, end + 1):
        if is_prime(number):
            list_prime.append(number)
    return list_prime

#10:47
def is_prime(number):
    """
        判断是否为素数
    :param number: 需要判断的数
    :return: 是不是素数
    """
    if number < 2:
        return False # 不是素数
    # 判断能否被中间的数字整除
    for i in range(2, number):
        if number % i == 0:
            return False # 不是素数
    return True # 是素数


primes = get_prime(5, 100)
print(primes)

primes = get_prime(-5, 50)
print(primes)
