import os

def rename_files(directory, new_name, num_digits, source_ext, target_ext, name_range=None):
    # Получаем список файлов в указанной директории
    files = [f for f in os.listdir(directory) if f.endswith(source_ext)]
    
    if not files:
        print(f"В директории '{directory}' нет файлов с расширением '{source_ext}'.")
        return
    
    for i, filename in enumerate(files, start=1):
        # Извлекаем диапазон символов из оригинального имени файла
        if name_range:
            original_name_part = filename[name_range[0] - 1:name_range[1]]
        else:
            original_name_part = ""
        
        # Собираем новое имя файла
        new_filename = f"{new_name}{i:0{num_digits}d}.{target_ext}"
        
        # Полный путь к оригинальному файлу
        src_path = os.path.join(directory, filename)
        
        # Полный путь к целевому файлу
        dest_path = os.path.join(directory, new_filename)
        
        # Переименовываем файл
        os.rename(src_path, dest_path)
        
        print(f"Переименован файл '{filename}' в '{new_filename}'.")

if __name__ == "__main__":
    source_directory = "Путь к директории"
    new_file_name = "Новое имя файла"
    num_digits = 3  # Количество цифр в порядковом номере
    source_extension = ".jpg"  # Расширение исходных файлов
    target_extension = "png"  # Расширение конечных файлов
    name_range = (3, 6)  # Диапазон символов из оригинального имени файла
    
    rename_files(source_directory, new_file_name, num_digits, source_extension, target_extension, name_range)
