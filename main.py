

def assemble_cook_book(file_name):
    with open(file_name, encoding='utf8') as f:
        cook_book = {}
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            num_ingr = int(f.readline().strip())
            cook_book[dish_name] = []
            while num_ingr != 0:
                dish_ingr = f.readline().split(sep='|')
                dish_ingr = [x.strip() for x in dish_ingr]
                dish_ingr_dic = {'ingredient_name': dish_ingr[0], 'quantity': int(dish_ingr[1]), 'measure': dish_ingr[2]}
                cook_book[dish_name].append(dish_ingr_dic)
                num_ingr -= 1
            f.readline()
    return cook_book


def calc_shop_list(num_pers, dish_request, recipe_list):
    shop_list = {}
    for dish in dish_request:
        if dish in recipe_list.keys():
            for ingr in recipe_list[dish]:
                name = ingr['ingredient_name']
                if name in shop_list:
                    shop_list[name]['quantity'] += ingr['quantity'] * num_pers
                else:
                    shop_list[ingr['ingredient_name']] = {'quantity': ingr['quantity'] * num_pers, 'measure': ingr['measure']}
    print(shop_list)

calc_shop_list(4, ['Омлет', 'Омлет', 'Омлет', 'Запеченный картофель'], assemble_cook_book('recipes.txt'))

