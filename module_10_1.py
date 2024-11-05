import threading
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    """Записывает заданное количество слов в файл с задержкой."""
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Задержка 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

if __name__ == "__main__":
    # Время начала записи функций
    start_time = datetime.now()

    # Запуск функций с аргументами из задачи
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    # Время окончания записи функций
    end_time = datetime.now()
    print(f"Время выполнения функций: {end_time - start_time}")

    # Время начала работы потоков
    start_time_threads = datetime.now()

    # Создание потоков
    threads = []
    thread_args = [
        (10, 'example5.txt'),
        (30, 'example6.txt'),
        (200, 'example7.txt'),
        (100, 'example8.txt')
    ]

    for args in thread_args:
        thread = threading.Thread(target=write_words, args=args)
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Время окончания работы потоков
    end_time_threads = datetime.now()
    print(f"Работа потоков: {end_time_threads - start_time_threads}")