"""
    
    Chapter1
    華氏溫度轉攝氏溫度
    20220209
    by Kevin Hsu
"""
temp_f = eval(input())
temp_c = (temp_f - 32 )* 5 / 9
print("Fahrenheit %.2f ----> Celsius %.2f"%(temp_f, temp_c))