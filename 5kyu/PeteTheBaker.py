'''Пит любит печь торты. У него есть несколько рецептов и ингредиентов. К сожалению, он не силен в математике. 
Можете ли вы помочь ему выяснить, сколько тортов он мог бы испечь, учитывая его рецепты?
Напишите функцию cakes(), которая принимает рецепт (объект) и доступные ингредиенты (тоже объект) и 
возвращает максимальное количество тортов, которые может испечь Пит (целое число). Для простоты здесь нет единиц 
измерения количества (например, 1 фунт муки или 200 г сахара равны просто 1 или 200). 
Ингредиенты, которых нет в объектах, могут рассматриваться как 0.'''
def cakes(recipe, available):
    return min([available[i] // recipe[i] if i in available else 0 for i in recipe])