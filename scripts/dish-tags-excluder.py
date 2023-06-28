import os
import json


def extract_tags(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        tags = []
        for category in data['categorys']:
            for menu_item in category['menu-items']:
                tags.extend(menu_item['tags'])
        #Making all tags to be in lowercase
        for i in range(len(tags)):
            tags[i] = tags[i].lower()
        return tags



def split_tags(input_file, output_file, layout):
    with open(input_file, 'r') as f:
        data = json.load(f)

    tags = data['tags']
    new_tags = []

    for tag in tags:
        new_tags.extend(tag.split())

    data['tags'] = new_tags
    data['tags'] = sorted(set(data['tags']))
    print(type(data['tags']))

    # Запись информации о количестве тегов в файл
    with open('FlavorConnect/jsons/dish-tags-spliced-quantity.txt', 'w') as f:
        f.write(f"Number of tags in splitted file: {len(data['tags'])}\n")

    # Удаляем дубликаты, приводим все к нижнему регистру
    new_tags = list(set(tag.lower() for tag in new_tags))



    if layout == "column":
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print (f"The tags was spliced, теги были сохранены в файле: {output_file}")
    elif layout == "row":
        with open(output_file, 'w') as f:
            f.write(json.dumps(data, separators=(',', ':'))) #сериализатор убирает пробелы между тэгами
        print (f"The tags was spliced, теги были сохранены в файле: {output_file}")




def main():
    folder_path = 'FlavorConnect/jsons/restaurants'  
    output_file = 'FlavorConnect/jsons/dish-tags-column.json' 
    output_file_row = 'FlavorConnect/jsons/dish-tags-row.json' 
    splitted_output_file = 'FlavorConnect/jsons/dish-tags-column-splitted.json'
    splitted_output_file_row = 'FlavorConnect/jsons/dish-tags-row-splitted.json'

    tags_set = set()  # Множество для хранения уникальных тегов
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            existing_tags = json.load(file)
            tags_set.update(existing_tags)


    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            json_file = os.path.join(folder_path, filename)
            tags = extract_tags(json_file)
            tags_set |= set(tags)  # Добавляем уникальные теги в множество

    tags_list = sorted(list(tags_set))  # Преобразование множества обратно в список и сортировка в алфавитном порядке
    tags_list2 = tags_list.copy()


    formatted_tags = {'tags': tags_list}  #в столбик
    with open(output_file, 'w') as file:
        json.dump(formatted_tags, file, indent=4)
    print(f"Извлеченные теги были сохранены в файле: {output_file}")
    split_tags(output_file, splitted_output_file, "column")

    formatted_tags = {'tags': (tags_list2)}  #в строчку
    output_file = output_file_row
    with open(output_file, 'w') as file:
        json.dump(formatted_tags, file, indent=None)
    print(f"Извлеченные теги были сохранены в файле: {output_file}")
    split_tags(output_file, splitted_output_file_row, "row")

    # Запись информации о количестве тегов в файл
    with open('FlavorConnect/jsons/dish-tags-quantity.txt', 'w') as f:
        f.write(f"Number of tags in the file: {len(tags_list)}\n")

if __name__ == '__main__':
    main()
