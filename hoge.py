'''
引数のnameを使い回す為に
self.nameを定義している。
'''


class User:
    def __init__(self, 引数のname, age):
        self.name = 引数のname
        self.age = age


bob = User(引数のname='ボブ・ディラン', age=60)

print(bob.name)
