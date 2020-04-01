

cook_book = {}

with open('recipes.txt', encoding='utf8') as f:

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


def shop_book(recipe_request, recipe_list):
    shop_list = {}
    for dish in recipe_list:
        if dish in recipe_request:
            shop_list[dish] = recipe_list[dish]
    return shop_list


def calc_shop_list(person_quantity, recipe_list):
    shop_list = {}
    for dish in recipe_list.values():
        for ingredient in dish:
            shop_ingredient = ingredient
            shop_ingredient['quantity'] *= person_quantity
            if shop_ingredient['ingredient_name'] not in shop_list:
                shop_list[shop_ingredient['ingredient_name']] = shop_ingredient
            else:
                shop_list[shop_ingredient['ingredient_name']]['quantity'] += shop_ingredient['quantity']
    return shop_list


def print_shop_list(shop_list):
    print('Нужно купить:')
    for ingredient in shop_list.values():
        print(f"{ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")

test_shop = calc_shop_list(3, shop_book(['Омлет','Запеченный картофель'], cook_book))

print(test_shop)

print_shop_list(test_shop)
