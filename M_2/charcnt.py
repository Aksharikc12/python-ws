names = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
print(list(map(lambda x:len(x),names)))

data = "raj,siva,Mani,sonu,Anu,Tanvi"
print(list(map(lambda x:x.capitalize(),data.split(","))))
print(list(filter (lambda x:x.startswith("A"), map(lambda x:x.capitalize(),data.split(",")))))