st = "".join(input().split()).lower()
print(st == st[::-1])

# Строка разбивается в список, после собирается обратно в строку без пробелов
# Все буквы становятся маленькими
# Проверяется, равна ли строка той же строке только в срезе с шагом -1
# Выводится True/False

# Палиндромы в виде предложений тут работают как пример: "А роза упала на лапу азора"
