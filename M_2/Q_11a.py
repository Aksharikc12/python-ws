'''11.	Following are the initials of players who play various games. Some of these players play more than one game.
Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football: [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]

Write a program to:
a.	List those players who play all three games.
b.	List those players who play exactly one game.
  '''

Cricket = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton = [ "PKM", "ALN", "NV", "KM","RMV"]
player =[]
player.extend(Cricket)
player.extend(Football)
player.extend(Badminton)
u_name = []
for name in Cricket:
    if name in Football:
        if name in Badminton:
            u_name.append(name)
    

print(u_name)

one = []
for i in Cricket:
    if (is_Football(i) or is_Badminton(i)) == False:
        one.append(i)
for i in Football:
    if (is_Cricket(i) or is_Badminton(i)) == False:
        one.append(i)
for i in Badminton:
    if (is_Football(i) or is_Cricket(i) )== False:
        one.append(i)
print(one)