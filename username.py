#1. Skapa ett username från ett namn
namn = " aNnA kaRlSsOn "

namn = namn.strip() #ta bort mellansnam i början och slutet 
namn = namn.title() #första bokstaven i varje ord är en versal och de andra gemener 
namn = namn.replace(" ", "-") #den har ersätter mellanslag med bindestreck 
print(namn)