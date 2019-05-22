# 3. 英文单词反转
#   how are you -->you are how
str_01 = "how are you"
list_result = str_01.split(" ")
list_result = list_result[::-1]
str_result = " ".join(list_result)
print(str_result)



