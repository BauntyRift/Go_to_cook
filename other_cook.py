import os
from pprint import pprint


def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]: 
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такое блюдо не найдено!"\n')
    return ingr_list




def end_file():
    file_directory = 'sorted'
    output_file = "output_file.txt"

    file_data = []

    os.chdir(file_directory)
    files = os.listdir()

    for file_name in files:
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append({
                'name': file_name,
                'line_count': len(lines),
                'lines': lines
            })

    file_data = sorted(file_data, key=lambda x: x['line_count'])

    with open(output_file, 'w', encoding='utf-8') as output:
        for file in file_data:
            output.write(file['name'] + '\n')
            output.write(str(file['line_count']) + '\n')
            output.writelines(file['lines'])
            output.write('\n')




if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cookbook()
    print('------Задание 1 - Проверка словаря------')

    print(cook_book)
    print('------Задание 2 - Ингредиенты для блюд на количество людей------')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))


    print('------Задание 3 -Надеюсь, я понял что вы имеете ввиду. Я постарался переделать свой код, и вроде, тперь работает как надо. Вызов функции ниже создаст выходной файл в папке "sorted"------')
    end_file()


