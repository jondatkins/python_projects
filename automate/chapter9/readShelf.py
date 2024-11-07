import shelve

shelfFile = shelve.open("mydata")
print(type(shelfFile))
print(shelfFile["cats"])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
