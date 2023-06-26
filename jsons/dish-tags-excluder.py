import os
import json

def extract_tags(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        tags = []
        for category in data['categorys']:
            for menu_item in category['menu-items']:
                tags.extend(menu_item['tags'])
        return tags

def main():
    folder_path = './jsons/restaurants'  # Укажите путь к папке с JSON файлами
    output_file = 'dish-tags.json'  # Имя выходного JSON файла

    tags_set = set()  # Множество для хранения уникальных тегов
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            existing_tags = json.load(file)
            tags_set.update(existing_tags)

    format_option = 1  # Выбор опции формата записи тегов (1 - в столбик, 2 - в строчку)

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            json_file = os.path.join(folder_path, filename)
            tags = extract_tags(json_file)
            tags_set |= set(tags)  # Добавляем уникальные теги в множество

    tags_list = sorted(list(tags_set))  # Преобразование множества обратно в список и сортировка в алфавитном порядке

    if format_option == 1:
        formatted_tags = {'tags': tags_list}  # Записываем каждый тег в отдельный элемент списка
    elif format_option == 2:
        formatted_tags = {'tags': ','.join(tags_list)}  # Записываем все теги в виде строки, разделенной запятой

    with open(output_file, 'w') as file:
        json.dump(formatted_tags, file, indent=4)

    print(f"Извлеченные теги были сохранены в файле: {output_file}")

if __name__ == '__main__':
    main()
