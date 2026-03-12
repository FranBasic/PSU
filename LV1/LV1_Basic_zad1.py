radni_sati = float(input("\nUnesi broj radnih sati: "))
placa_po_satu = float(input("\nUnesi placu po satu: "))

def total_euro(radni_sati, placa_po_satu):
    ukupno=float(radni_sati*placa_po_satu)
    return(ukupno)

print(f"{total_euro(radni_sati, placa_po_satu)} €")