''' to get unique names'''

Cricket = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton = [ "PKM", "ALN", "NV", "KM","RMV"]
player =[]
player.extend(Cricket)
player.extend(Football)
player.extend(Badminton)
u_name = []
for name in player:
    if name in u_name:
        pass
    else:
        u_name.append(name)

print(u_name)