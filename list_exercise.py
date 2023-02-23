boys = ["ahmet", "mehmet", "mustafa", "mahmut", "burak", "enes", "selim"]
girls = ["fatma", "betül" ,"nurdan", "elif", "tuba", "ayşe"]

print(boys)
print(girls)

print(boys[1])                 # mehmet
print(boys[1:])                # ['mehmet', 'mustafa', 'mahmut', 'burak', 'enes', 'selim']
print(boys[2:])                # ['mustafa', 'mahmut', 'burak', 'enes', 'selim']
print(boys[2:4])               # ['mustafa', 'mahmut']
print(boys[:4])                # ['ahmet', 'mehmet', 'mustafa', 'mahmut']
print(boys[2],boys[5])         # mustafa enes
print(boys[-1])                # selim
print(boys[-3:])               # ['burak', 'enes', 'selim']
print(boys[-2:])               # ['enes', 'selim']

print(girls[5])
girls[5]= "yurdusev"
print(girls[5])