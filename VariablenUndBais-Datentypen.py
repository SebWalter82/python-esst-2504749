# Das ist ein Kommentar in Ihrer Uebungsdatei

"""
Mehrzeilger Kommentar
"""

'''
Das geht auch.
'''

print('Hallo Welt!')

#Zahlen 
#ineger Zahlen - ganze Zahlen 
var_integer = 12

#float Zahlen - Komma Zahlen
var_float = 5.1

#Beispiel:
var_erg_Summe1 = var_integer + var_float
print("Ergebnis =", var_erg_Summe1)

#Zeichen (englisch: character)
mein_zeichen = 'x'
mein_text = "Hallo, hier ist mein Text."
print(mein_zeichen)
print(mein_text)

#Bool - Wahr oder Falsch?
var_wahr = True
var_falsch = False
print(var_wahr)

#Liste (Reihe von Variablen)
var_meine_Liste = [0, 10]   #Die Eckige Klammer [] kommt mit opt + 5
var_meine_Liste.append(70)  #Die Liste um die Zahl 70 erweitern.
print(var_meine_Liste)
# Die liste geht immer an Stelle 0 los. 
# Die Null ist also Stelle Null und die Eins stelle Eins.
var_meine_Liste[1] = 15 #In der Liste Position 1 neu beschreiben mit Wert 15. Also 10 -> 15.
print(var_meine_Liste)
print('Meine Liste an Postition 2:', var_meine_Liste[2])