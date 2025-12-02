#SCOPE - The visibility of variables, where it can be seen and used
#GLOBAL - outside of all function(visible everywhere)
#LOCAL - inside a function(only visible there)

#THE BUG - CRASHES (UnboundLocalError)
def add_bonus():
    score = score + 100
    
score = 500
add_bonus()
