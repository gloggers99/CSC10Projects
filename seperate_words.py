mystring="elephantkangarooaardvarkanteatersquirrelflamingomongoosechipmunkgoldfishbluebirdstarfishbullfrog"
animals = []
if len(mystring) % 8 == 0:
    for i in range(0, round(len(mystring)/8)):
        animals.append(mystring[i*8:((i*8)+8)])

print(animals)

