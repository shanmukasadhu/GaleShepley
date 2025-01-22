class man():
    def __init__(self, name, isFree=True, preferences = None, proposedTo = None, engaged = None):
        self.name = name
        self.isFree = isFree
        self.preferences = preferences
        self.proposedTo = proposedTo
        self.engaged = engaged
class women():
    def __init__(self, name, isFree=True, preferences=None, engaged = None):
        self.name = name
        self.isFree = isFree
        self.preferences = preferences
        self.engaged = engaged

def findFreeMen(allMen):
    allFreeMen = [man for man in allMen if man.isFree]
    return allFreeMen


# Define Men
man1 = man(name="Man 1", proposedTo=[])
man2 = man(name="Man 2", proposedTo=[])
man3 = man(name="Man 3", proposedTo=[])
man4 = man(name="Man 4", proposedTo=[])
man5 = man(name="Man 5", proposedTo=[])
man6 = man(name="Man 6", proposedTo=[])
man7 = man(name="Man 7", proposedTo=[])
man8 = man(name="Man 8", proposedTo=[])
man9 = man(name="Man 9", proposedTo=[])
man10 = man(name="Man 10", proposedTo=[])

# Define Women
woman1 = women(name="Woman 1")
woman2 = women(name="Woman 2")
woman3 = women(name="Woman 3")
woman4 = women(name="Woman 4")
woman5 = women(name="Woman 5")
woman6 = women(name="Woman 6")
woman7 = women(name="Woman 7")
woman8 = women(name="Woman 8")
woman9 = women(name="Woman 9")
woman10 = women(name="Woman 10")

# Set Men Preferences
man1.preferences = [woman2, woman3, woman4, woman5, woman1, woman6, woman7, woman8, woman9, woman10]
man2.preferences = [woman1, woman3, woman2, woman5, woman6, woman4, woman8, woman7, woman9, woman10]
man3.preferences = [woman4, woman2, woman1, woman6, woman7, woman3, woman5, woman9, woman8, woman10]
man4.preferences = [woman5, woman6, woman1, woman2, woman4, woman3, woman7, woman9, woman8, woman10]
man5.preferences = [woman7, woman4, woman5, woman2, woman1, woman6, woman8, woman9, woman3, woman10]
man6.preferences = [woman8, woman9, woman10, woman3, woman4, woman1, woman2, woman5, woman6, woman7]
man7.preferences = [woman6, woman7, woman1, woman5, woman2, woman4, woman8, woman9, woman10, woman3]
man8.preferences = [woman9, woman10, woman8, woman3, woman1, woman7, woman5, woman4, woman6, woman2]
man9.preferences = [woman3, woman1, woman4, woman2, woman9, woman5, woman6, woman8, woman10, woman7]
man10.preferences = [woman2, woman3, woman5, woman9, woman7, woman6, woman1, woman8, woman10, woman4]

# Set Women Preferences
woman1.preferences = [man3, man1, man7, man10, man4, man9, man8, man6, man2, man5]
woman2.preferences = [man2, man9, man1, man3, man6, man7, man5, man4, man8, man10]
woman3.preferences = [man5, man6, man8, man9, man3, man1, man10, man4, man2, man7]
woman4.preferences = [man8, man1, man2, man5, man4, man7, man10, man6, man3, man9]
woman5.preferences = [man7, man10, man2, man9, man6, man4, man1, man8, man5, man3]
woman6.preferences = [man1, man3, man5, man2, man6, man8, man7, man9, man4, man10]
woman7.preferences = [man4, man5, man9, man6, man1, man7, man8, man2, man3, man10]
woman8.preferences = [man9, man7, man10, man2, man3, man8, man4, man6, man1, man5]
woman9.preferences = [man6, man4, man8, man1, man3, man7, man9, man2, man5, man10]
woman10.preferences = [man10, man7, man3, man4, man5, man2, man1, man6, man9, man8]

# Collect all Men and Women
allMen = [man1, man2, man3, man4, man5, man6, man7, man8, man9, man10]
allWomen = [woman1, woman2, woman3, woman4, woman5, woman6, woman7, woman8, woman9, woman10]




allFreeMen = findFreeMen(allMen)



while(allFreeMen != []):
    m = allFreeMen[0]
    for women in m.preferences:
        if women not in m.proposedTo:
            w = women
            break
    
    m.proposedTo.append(w)
    if w.isFree:
        w.engaged = m
        m.engaged = w
        w.isFree = False
        m.isFree = False
    else:
        mprime = w.engaged
        if(w.preferences.index(mprime)<w.preferences.index(m)):
            print("Likes her current mans.")
        else:
            w.engaged = m
            m.engaged = w
            w.isFree = False
            m.isFree = False
            mprime.isFree = True
            mprime.engaged = None

    allFreeMen = findFreeMen(allMen)
            
            
for man in allMen:
    print(f"{man.name} is engaged to {man.engaged.name}")
print("")
for woman in allWomen:
    print(f"{woman.name} is engaged to {woman.engaged.name}")

