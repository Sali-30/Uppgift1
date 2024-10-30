
#1. Skapa ett username från ett namn
# namn = " aNnA kaRlSsOn "

# namn = namn.strip() #ta bort mellansnam i början och slutet 
# namn = namn.title() #första bokstaven i varje ord är en versal och de andra gemener 
# namn = namn.replace(" ", "-") #den har ersätter mellanslag med bindestreck 
# print(namn)


# 2. Beställning på ICA
#Skapa en tuple som innehåller kundens beställning.
# beställning = ( "bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")

# #första 3 varorna i beställningen 
# första_tre_varor = beställning[:3]
# print("de första tre varorna:", första_tre_varor)

# #de sista 2 varorna i beställningen 
# sista_två_varor = beställning[-2:]
# print("de sista två varorna:", sista_två_varor)

# #varannan vara 
# varannan_vara = beställning[::2]
# print("varannan vara:", varannan_vara)

# 3. Topplista med filmer med for loopar 

# filmer = [ "Inception", "The Matrix", "Interstellar", "The Prestige"] #listan med filmer 

# filmer.append("Memento") #lägger till filmen i slutet av listan 

# for i in range(len(filmer)):
#     if filmer[i] == "The matrix":
#         filmer[i] = "the lord of the rings" #har byter jag ut filmerna  teh matrix för the lord... 

# for film in filmer: 
#     if film == "The Prestige": #hade eskrivit fel ordet film därför hade problem när jag skulle skriva ut 
#         filmer.remove(film) #loop för att ta bort filmen från listan 


# new_list = []
# for i in range(len(filmer)): 
#     if i == 2:
#         new_list.append("The dark knight")
#     new_list.append(filmer[i])

# filmer = new_list
# print(filmer)
 

#
