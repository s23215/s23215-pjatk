names = ("Franek","Marek","Zbyszek","Asia","Basia","Kasia",)
surnames = ("Banach", "Currie", "Kowalski", "Studencki")

def looks_like_polish_surname(s):
    polish_suffixes= ("ski","cki")
    for each in polish_suffixes:
        if s.endswith(each):
            return True
    return False

for each in names:
    if each[-1] =='a':
        print (each)

for each in surnames:
    if looks_like_polish_surname(each):
        print (each)

people = []

for i in names:
    for j in surnames:
        if i[-1] == 'a' and looks_like_polish_surname(j):
            j=j[:-1] + 'a'
        people.append((i,j))

for each in people:
    print (each)



