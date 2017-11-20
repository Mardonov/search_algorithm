class Main:

    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    __read_logs_file = '/var/log/auth.log'

    # Открываем файл - logs
    def open_the_log_for_reading(self):
        try:
            read_file = open(self.__read_logs_file, mode='r', encoding='UTF-8')
            return read_file
        except FileNotFoundError as e:
            print('Файл или директория не существует! ', e)
        except UnicodeError as e:
            print('Ошибка, связанная с кодированием / раскодированием unicode в строках. ', e)
        except IsADirectoryError as e:
            print('Ошибка, ожидался файл, но это директория. ', e)
        except Exception as e:
            print('Сведения об исключении:  def open_the_log_for_reading(self) -  ', e)

    # Ищем строку в логе по входным данным и возвращаем номер найденной строки
    def search_numb_line(self):
        try:
            search_number_line = None
            for num, line in enumerate(self.open_the_log_for_reading(), 0):
                if self.ip_addr in line:
                    search_number_line = num
            return search_number_line
        except Exception as e:
            print('Номер строки не найден ', e)

    # Ищем последнюю строку в логе
    def search_last_line(self):
        try:
            last_line = None
            for num, line in enumerate(self.open_the_log_for_reading(), 0):
                last_line = num
            return last_line
        except Exception as e:
            print("Сведения об исключении: def search_last_line(self) -", e)

    # Возвращаем номер строки от - 100 строк от найденного идентификатора.
    def min_num(self, search_num):
        try:
            if search_num - 100 > 0:
                min_num = search_num - 100
            else:
                min_num = 0
            return min_num
        except Exception as e:
            print("Сведения об исключении: def min_num(self, search_num) - ", e)

    # Возвращаем номер строки от + 100 строк от найденного идентификатора.
    def max_num(self, num_line):
        try:
            if num_line + 100 < self.search_last_line():
                min_num = num_line + 100
            else:
                min_num = self.search_last_line()
            return min_num
        except Exception as e:
            print("Сведения об исключении: def max_num(self, num_line) - ", e)

    # Записываем найденные строки в файл, +100 и -100 строк от найденной строки.
    def write_info_to_file(self, min_, max_):
        try:
            for num, line in enumerate(self.open_the_log_for_reading(), 0):
                if (num > min_) and (num < max_):
                    print(line)
            self.open_the_log_for_reading().close()
        except Exception as e:
            print("Сведения об исключении: def write_lines_to_file(self, min_, max_) - ", e)


if __name__ == '__main__':
    ip = input('Введите ip-адрес: ')

    obj = Main(ip)
    print('==============================')

    num_line_ = obj.search_numb_line()
    print("Номер найденной строки - " + str(num_line_))

    min_numb_line = obj.min_num(num_line_)
    print("Минимальний номер строки - " + str(min_numb_line))

    max_numb_line = obj.max_num(num_line_)
    print("Максимальеый номер строки - " + str(max_numb_line))

    obj.write_info_to_file(min_numb_line, max_numb_line)
    print('Записали найденные строки в файл - info_found_in_the_logs.txt')