import time
import multiprocessing

def read_info(name):
    all_data = []  # Локальный список для хранения данных
    with open(name, 'r') as file:
        while True:
            line = file.readline()  # Чтение строки из файла
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы
    return all_data

if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейный вызов: {linear_duration:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    processes = [] # Список процессов

    for filename in filenames:
        process = multiprocessing.Process(target=read_info, args=(filename,)) # Создаём процесс
        processes.append(process)  # Добавляем процесс
        process.start()  # Запускаем процесс

    for process in processes:
        process.join()  # Ожидаем завершения всех процессов
    multiprocessing_duration = time.time() - start_time
    print(f"Многопроцессный вызов: {multiprocessing_duration:.6f} секунд")