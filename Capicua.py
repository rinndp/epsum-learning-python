print("-----------------------------------------------------------")
print(" 😈INGRESA UN NÚMERO Y TE DIREMOS SI ES CAPICÚA O NO 😈")
print("-----------------------------------------------------------")
numeroExaminar = str(input("Ingresa el número que quiere examinar: "))
esCapicua = True
for i in range(len(numeroExaminar)//2):
    if numeroExaminar[i] != numeroExaminar[-i - 1]:
        esCapicua = False

if esCapicua:
    print("El número SI es capicua")
else:
    print("El número NO es capicua")







