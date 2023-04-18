from item import Item


class Lang:
    def __init__(self, language):
        self.__language = language
        
    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self
    @property
    def language(self):
        return self.__language
    
class Keyboard(Item, Lang):
    def __init__(self,name,price,quantity, language):
        super().__init__(self, name,price,quantity)
        self.__language = language
            