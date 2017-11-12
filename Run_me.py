from Main import Main

ip = input('Введите ip-адрес: ')
mask = input('Введите маску названия лога: ')
num = input('Введите числовой идентификатор: ')

obj = Main(ip, mask, num)
print('==============================')

num_line_ = obj.search_numb_line()
print("Номер найденной строки - " + str(num_line_))

min_numb_line = obj.min_num(num_line_)
print("Минимальний номер строки - " + str(min_numb_line))

max_numb_line = obj.max_num(num_line_)
print("Максимальеый номер строки - " + str(max_numb_line))

obj.write_info_to_file(min_numb_line, max_numb_line)
print('Записали найденные строки в файл - info_found_in_the_logs.txt')
