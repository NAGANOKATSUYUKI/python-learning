#オブジェクト指向
class Player:       #設計図1  インスタンス生成
    def display(self):
        print("Name: ", self.name)
        print("Level:", self.level)
"""
p1 = Player()       #インスタンスの生成
p1.name = "Daikon"  #名前の設定
p1.level = 1        #レベル設定
p1.display()        #名前とレベルの表示

p2 = Player()
p2.name = "Ninzin"
p2.level = 2
p2.display()
"""

class Player:       #設計図2　initメソッド
    def __init__(self, name, level):    #引数を受け取り、データ属性を初期化する
        self.name = name
        self.level = level

    def display(self):
        print("Name: ", self.name)
        print("Level:", self.level)
"""
p1 = Player("aho", 100)
p2 = Player("baka", 99)
p1.display()
p2.display()
"""

class Player:       #設計図3　メソッドの追加
    def __init__(self, name, level):    #引数を受け取り、データ属性を初期化する
        self.name = name
        self.level = level

    def display(self):
        print("Name: ", self.name)
        print("Level:", self.level)

    def level_up(self, number):         #メソッドの追加
        self.level += number
'''
p1 = Player("aho", 100)
p2 = Player("baka", 99)
p1.level_up(677)                        #レベルアップの設定
p2.level_up(1)
p1.display()
p2.display()
'''
class Player:       #設計図4　マングリング
    def __init__(self, name, level):   
        self.name = name
        self.level = level

    def display(self):
        print("Name: ", self.name)
        print("Level:", self.level)

    def level_up(self, number):         
        self.level += number
        self.__check_level()            #レベルの確認
    
    def __check_level(self):            #定義
        if self.level > 10:             #レベルが超えていたら    
            self.level = 10             #レベルを10に補正する
"""
p1 = Player("aho", 100)
p2 = Player("baka", 99)
p1.level_up(677)            
p2.level_up(1)
p1.display()
p2.display()
"""

class Player:       #設計図5　クラス属性
    LEBEL_LIMIT = 100                            #クラス属性設定

    def __init__(self, name, level):   
        self.name = name
        self.level = level

    def display(self):
        print("Name: ", self.name)
        print("Level:", self.level)

    def level_up(self, number):         
        self.level += number
        self.__check_level()            
    
    def __check_level(self):            
        if self.level > Player.LEBEL_LIMIT:              
            self.level = Player.LEBEL_LIMIT  
        if self.level < 0:                       #マイナスになるときは１に補正する
            self.level = 1      

"""
p1 = Player("aho", 100)
p2 = Player("baka", 1)
p1.level_up(677)            
p2.level_up(-5)
p1.display()
p2.display()
"""

class Player:       #設計図6　継承
    LEBEL_LIMIT = 15                            

    def __init__(self, name, level):            #以前と同じ
        self.name = name
        self.level = level

    def display(self):
        print("Name: ", self.name)
        print("Level:", self.level)

    def level_up(self, number):         
        self.level += number
        self.__check_level()            
    
    def __check_level(self):            
        if self.level > Player.LEBEL_LIMIT:              
            self.level = Player.LEBEL_LIMIT

class Fighter(Player):                          #クラスの定義
    def __init__(self, name, level, sword):     #オーバーライド
        Player.__init__(self, name, level)      #Playerクラスのinitメソッドを呼び出す
        self.sword = sword                      #データ属性swordの設定

    def display(self):
        Player.display(self)                    #Playerクラスのinitメソッドを呼び出す
        print("Sword:", self.sword)             #swordの表示

    def slash(self):                            #Fighterクラス特有のメソッド
        print("Slashing!")                      

class Wizard(Player):                           #クラスの定義
    def __init__(self, name, level, wand):      #オーバーライド
        Player.__init__(self, name, level)      #Playerクラスのinitメソッドを呼び出す
        self.wand = wand                        #データ属性wandの設定

    def display(self):
        Player.display(self)                    #Playerクラスのinitメソッドを呼び出す
        print("Wand:", self.wand)               #wandの表示

    def magic(self):                            #Wizardクラス特有のメソッド
        print("Casting a magic!")                      

"""
f = Fighter('aho', 1, "kuso")                   #Fighterクラスインスタンス生成
f.display()                                     #呼び出し
f.slash()                                       #呼び出し

w = Wizard("baka", 5, "unko")
w.display()
w.magic()
"""

class Player:       #設計図7　多重継承
    LEBEL_LIMIT = 15                            

    def __init__(self, name, level):            #以前と同じ
        self.name = name
        self.level = level

    def display(self):
        print("Name: ", self.name)
        print("Level:", self.level)

    def level_up(self, number):         
        self.level += number
        self.__check_level()            
    
    def __check_level(self):            
        if self.level > Player.LEBEL_LIMIT:              
            self.level = Player.LEBEL_LIMIT

class Fighter(Player):                               
    def __init__(self, name, level, sword):     #オーバーライド
        Player.__init__(self, name, level)      
        self.sword = sword                      

    def display(self):
        Player.display(self)                    
        print("Sword:", self.sword)             

    def slash(self):                            
        print("Slashing!")                      

class Wizard(Player):                                   
    def __init__(self, name, level, wand):      #オーバーライド
        Player.__init__(self, name, level)      
        self.wand = wand                        

    def display(self):
        Player.display(self)                    
        print("Wand:", self.wand)               

    def magic(self):                            
        print("Casting a magic!")      

class MagicKnight(Fighter, Wizard):
    def __init__(self, name, level, sword, wand):
        Player.__init__(self, name, level )
        self.sword = sword
        self.wand = wand

    def display(self):
        Player.display(self)
        print("Sword:", self.sword)                
        print("Wand:", self.wand)

"""
mk = MagicKnight("tensai", 1, "silver", "glass")
mk.display()
mk.slash()
mk.magic()
"""

import random                       #モジュールのインポート
print(random.random())              #モジュールの関数の呼び出し