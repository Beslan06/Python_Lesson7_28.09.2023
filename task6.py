import os
import random
import string

def create_files_with_extension(directory, extension, min_name_length=6, max_name_length=30,
                                min_file_size=256, max_file_size=4096, num_files=42):
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Ошибка при создании директории: {e}")
        return

    for _ in range(num_files):
        # Генерируем случайное имя файла
        file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(min_name_length, max_name_length)))
        file_name = f"{file_name}.{extension}"
        file_path = os.path.join(directory, file_name)

        # Проверяем, существует ли файл с таким именем
        if os.path.exists(file_path):
            print(f"Файл {file_path} уже существует, пропускаем.")
            continue

        # Генерируем случайный размер файла
        file_size = random.randint(min_file_size, max_file_size)

        # Создаем и записываем в файл случайные байты
        with open(file_path, 'wb') as file:
            file.write(os.urandom(file_size))

        print(f"Создан файл {file_path} размером {file_size} байт")

def create_files_with_extensions(directory, extensions_and_counts, **kwargs):
    for extension, num_files in extensions_and_counts.items():
        create_files_with_extension(directory, extension, num_files=num_files, **kwargs)

# Пример использования
extensions_and_counts = {'.txt': 5, '.jpg': 3, '.docx': 2}
create_files_with_extensions("my_directory", extensions_and_counts, min_name_length=5, max_name_length=15, min_file_size=512, max_file_size=1024)
