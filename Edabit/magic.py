class magic():
    def replace(self,string,char1,char2):
        return string.replace(char1,char2)

    def length(self,string):
        return len(string)

    def trim(self,string):
        return string.strip()

    def list_slice(self,list,tuple):
        a,b  = tuple
        if list[a-1:b] == []:
            
            return -1
        else:
            print(-1)
            return list[a-1:b]

print(magic().replace("AzErty-QwErty", "E", "e") )

print(magic().length("hello world") )

print(magic().trim("      python is awesome      ") )

print(magic().list_slice([], (2, 4))) 