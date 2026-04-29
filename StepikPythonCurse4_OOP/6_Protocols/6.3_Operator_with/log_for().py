def log_for(logfile, data_str):
    with open(logfile, 'r', encoding="UTF-8") as file1:
        with open(f'log_for_{data_str}.txt', 'w', encoding='UTF-8') as file2:
            for line in file1.readlines():
                if data_str in line:
                    new_line = line.replace(data_str, '')
                    file2.write(new_line.lstrip(' '))