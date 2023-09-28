import os
import random
import string

def create_files_with_extension(extension, min_name_length=6, max_name_length=30,
                                min_file_size=256, max_file_size=4096, num_files=42):
    for _ in range(num_files):
        # Генерируем случайное имя файла
        file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(min_name_length, max_name_length)))
        file_name = f"{file_name}.{extension}"
        
        # Генерируем случайный размер файла
        file_size = random.randint(min_file_size, max_file_size)

        # Создаем и записываем в файл случайные байты
        with open(file_name, 'wb') as file:
            file.write(os.urandom(file_size))

        print(f"Создан файл {file_name} размером {file_size} байт")

# Пример использования
create_files_with_extension('txt', min_name_length=5, max_name_length=15, min_file_size=512, max_file_size=1024, num_files=10)
