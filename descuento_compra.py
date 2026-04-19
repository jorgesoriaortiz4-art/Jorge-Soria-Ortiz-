# Jorge Soria Ortiz
compra = float(input("Total de la compra: "))

if compra > 1000:
    descuento = compra * 0.1
    total = compra - descuento
    print("Descuento aplicado. Total:", total)
else:
    print("No hay descuento. Total:", compra)
