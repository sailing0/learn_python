# 4. 定义函数，判断字符串中存在的中文字符数量．
#     中文编码范围：0x4E00   ord(字符)    0x9FA5


def get_chinese_char_count(str_target):
    count = 0
    for item in str_target:
        if 0x4E00 <= ord(item) <= 0x9FA5:
            count += 1
    return count


count = get_chinese_char_count("a你sid你f好ln")
print(count)
