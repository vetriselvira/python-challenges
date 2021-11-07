class Pagination:
    items = []
    pageSize =24
    start_index = 0
    page_count = 0
    display_items = []

    def __init__(self,items,pageSize):
        self.items = items
        self.pageSize = pageSize

    def getvisibleitems (self):
        #index = 0
        #while index < classobject.pageSize:
        #    classobject.display.append(classobject.items[index])
        #    index = index + 1
        #return classobject.display
        
        self.end_index = self.start_index + self.pageSize
        t = self.items[self.start_index:self.end_index]
        self.start_index = self.end_index
        return t


p = "abcdefghijklmnopqrstuvwxyz"
lst=list(p)
#print(lst)
p = Pagination(lst, 4)
#print(p.items)

print(p.getvisibleitems())
print(p.getvisibleitems())
print(p.getvisibleitems())
print(p.getvisibleitems())


