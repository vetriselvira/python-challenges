class Shiritori():
    #def __init__(self,words,gameover):
    words = []
    gameover = None

    def play(self,word):
        if len(self.words) >=1:
            comp_string = self.words[-1]
        if self.words == []:
            self.words.append(word)
            return self.words

        
        elif (word[0] == comp_string[-1]) and word not in self.words:
            #print(f'word[0]{word[0]} ,self.words[-]{self.words[-1]}')
            self.words.append(word)
            return self.words
        else:
             self.gameover = True
             return "gameover"
    def restart(self):
        self.words = []
        self.gameover = False
        return "gamerestarted"


my_shiritori = Shiritori()

my_shiritori.play("apple") 
my_shiritori.play("ear") 
my_shiritori.play("rhino")
my_shiritori.play("corn") 

# Corn does not start with an "o".

print(my_shiritori.words )

# Words should be accessible.

print(my_shiritori.restart() )
print(my_shiritori.words)

# Words list should be set back to empty.

my_shiritori.play("hostess") 
print(my_shiritori.play("stash")) 
print(my_shiritori.play("hostess")) 
# Words cannot have already been said.
