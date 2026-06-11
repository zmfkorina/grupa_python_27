# terminalul are multiple stream-uri de text pe care le primeste si le afiseaza
# STDERR este streamul de erori

print("=============== Inceput de curs exceptii: ==============")
lista1 = [9, 10, 11, 33]

print(lista1)
print(lista1[3])

try:
    vari = int(input("De care index esti curios?"))
    print(lista1[vari])
except IndexError:
    print("we went too far")
except ValueError:
    print("You have to write an integer number")
except BaseException:
    print("You shall not pass")
    #pass

#exception bubble-up

if var2 > 5:
    raise Exception("My variable is too high")

print("=============== sfarsit de curs exceptii: ==============")