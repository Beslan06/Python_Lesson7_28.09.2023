import os
import shutil

def sort_files(source_directory, target_directory):
    # Создаем список расширений для каждой категории
    video_extensions = {'.mp4', '.avi', '.mkv'}
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif'}
    text_extensions = {'.txt', '.docx', '.pdf'}
    
    # Получаем список файлов в исходной директории
    files = os.listdir(source_directory)
    
    for file in files:
        # Получаем полный путь к файлу
        file_path = os.path.join(source_directory, file)
        
        # Проверяем, является ли файл видео
        if any(file.lower().endswith(ext) for ext in video_extensions):
            # Перемещаем файл в директорию для видео
            target_path = os.path.join(target_directory, 'Видео', file)
            shutil.move(file_path, target_path)
        
        # Проверяем, является ли файл изображением
        elif any(file.lower().endswith(ext) for ext in image_extensions):
            # Перемещаем файл в директорию для изображений
            target_path = os.path.join(target_directory, 'Изображения', file)
            shutil.move(file_path, target_path)
        
        # Проверяем, является ли файл текстовым документом
        elif any(file.lower().endswith(ext) for ext in text_extensions):
            # Перемещаем файл в директорию для текстовых документов
            target_path = os.path.join(target_directory, 'Текст', file)
            shutil.move(file_path, target_path)
        
        else:
            # Если файл не подходит ни под одну категорию, оставляем его в исходной директории
            print(f"Файл '{file}' не подходит для сортировки и остается в исходной папке.")

if __name__ == "__main__":
    source_directory = "Путь к исходной папке"
    target_directory = "Путь к целевой папке"
    
    sort_files(source_directory, target_directory)
