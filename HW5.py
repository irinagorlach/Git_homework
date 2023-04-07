class Three:
    biology_class = 'Plants'
    def __init__(self, name, height, age):
        self.__name = name
        self.height = height
        self.age = age

    def fruits(self):
        return 'I have fruits hanging on me'

    def get_name(self):
        return f'Animals, fruits hang on an {self.__name}'

    def set_name(self, new_name):
        self.__name = new_name

Three1 = Three('Oak', 35, 310)

Three2 = Three('Apple_Tree', 4, 20)

Three3 = Three('Apricot_Tree', 3, 10)

class Сreeper(Three):
    def __init__(self, name, height, age, tenacity):
        super().__init__(name, height, age)
        self.tenacity = tenacity

    def braid_the_tree(self):
        return 'I will drink all the juices!'

    def fruits(self):
        return 'I do not have fruits'

Three4 = Сreeper('Philodendron', 15, 3, 5)

