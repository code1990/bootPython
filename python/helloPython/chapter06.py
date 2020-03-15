# 第6章　字典　　81
# 6.1　一个简单的字典　　81
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 每个键 都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典
# 键—值 对是两个相关联的值。
alien_0 = {'color': 'green'}
print(alien_0['color'])
# 6.2　使用字典　　82
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
del alien_0['points']
print(alien_0)
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
# 6.3　遍历字典　　87
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())
# 可使用函数sorted() 来获得按特定顺序排列的键列表的副本
for name in sorted(favorite_languages.keys()):
    print(name.title())
# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())

# 6.4　嵌套　　93
# 将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 在字典中存储列表
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
for topping in pizza['toppings']:
    print("\t" + topping)
# 在字典中存储字典
users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton', },

         'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', }}
for username, user_info in users.items():
    print("\nUsername: " + username)
