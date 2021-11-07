class Book():
    def __init__(self,title,author):
        self.title =  title
        self.author = author

    def gettitle(self):
      return "title:{}".format(self.title) 

    def getauthor(self):
      return "author:{}".format(self.author) 

vv = Book("vetri","mylife")
print(vv.title)
print(vv.author)
print(vv.gettitle())
print(vv.getauthor())



