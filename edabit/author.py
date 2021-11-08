class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def get_title(self):
        return "title:{}".format(self.title)

    def get_author(self):
        return "author:{}".format(self.author)


vv = Book("vetri","mylife")
print(vv.title)
print(vv.author)
print(vv.get_title())
print(vv.get_author())



