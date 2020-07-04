"""
データ型宣言: Username
   属性:
     実際のユーザー名
   ルール:
    ・ユーザー名は4文字以上20文字以下である
    できること =>メソッド
    ・ユーザー名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) < 20):
            raise ValueError(f'{name}は文字数のルール違反やで！')

        self.name = name

    def screen_name(self):
        return self.name.upper()


# Usernameクラスのインスタンス化をしている
hibiki = UserName(name='hibiki')

print(hibiki.screen_name())

# print(hibiki)
# print type(hibiki)
# print(hibiki.name) # 'hibiki'

# sho = UserName('sho')
# print(sho.name)
