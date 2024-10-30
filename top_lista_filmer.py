# 3. Topplista med filmer med for loopar 


filmer = [ "Inception", "The Matrix", "Interstellar", "The Prestige"] #listan med filmer 

filmer.append("Memento") #lägger till filmen i slutet av listan 

for i in range(len(filmer)):
     if filmer[i] == "The matrix":
         filmer[i] = "the lord of the rings" #har byter jag ut filmerna  teh matrix för the lord... 

for film in filmer: 
     if film == "The Prestige": #hade eskrivit fel ordet film därför hade problem när jag skulle skriva ut 
         filmer.remove(film) #loop för att ta bort filmen från listan 


new_list = [] #Skapar en ny, tom lista som heter new_list.
for i in range(len(filmer)): #Startar en loop som itererar genom varje index i i listan filmer. 
    #range(len(filmer)) skapar en sekvens av index baserat på längden av listan filmer.
    if i == 2: #Kontrollerar om den nuvarande indexen i är lika med 2. Om detta villkor är uppfyllt, exekverar nästa rad.
         new_list.append("The dark knight") #satt till filmen i position 2 i den nya listan 
    new_list.append(filmer[i]) #Lägger till det nuvarande elementet från filmer (vid index i) till new_list.

filmer = new_list #Tilldelar den nya listan new_list till variabeln filmer, vilket effektivt ersätter den ursprungliga listan med den uppdaterade listan.
print(filmer)