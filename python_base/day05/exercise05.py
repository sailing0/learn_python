#练习２：在控制台中录入一个字符串
#       打印这个字符串中的字符以及出现的次数．
#       abcdbcdb
#       a字符1次
#       b　　3
#       c   2
#       d   2

str_input = "abcdbcdb"
# key: 字符   value:次数
result = {}
# (1)逐一判断字符，出现的次数．
for item in str_input:
    # (2)如果没有统计过该字符串
    if item not in  result:
        result[item] = 1
    else:
        # (3)否则,次数增加
        # result[item] = result[item] + 1
        result[item] += 1

print(result)


