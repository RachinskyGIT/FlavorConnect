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
    folder_path = '../jsons/restaurants'  # Укажите путь к папке с JSON файлами
    output_file = 'dish-tags.json'  # Имя выходного JSON файла

    tags_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            json_file = os.path.join(folder_path, filename)
            tags = extract_tags(json_file)
            tags_list.extend(tags)

    with open(output_file, 'w') as file:
        json.dump(tags_list, file)

    print(f"Извлеченные теги были сохранены в файл: {output_file}")

if __name__ == '__main__':
    main()
