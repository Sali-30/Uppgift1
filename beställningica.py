# 2. Beställning på ICA
#Skapa en tuple som innehåller kundens beställning.
beställning = ( "bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")

#första 3 varorna i beställningen 
första_tre_varor = beställning[:3]
print("de första tre varorna:", första_tre_varor)

#de sista 2 varorna i beställningen 
sista_två_varor = beställning[-2:]
print("de sista två varorna:", sista_två_varor)

#varannan vara 
varannan_vara = beställning[::2]
print("varannan vara:", varannan_vara)