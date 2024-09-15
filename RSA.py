import math
import pandas as pd

# Izvada algoritma nosaukumu un versiju / Print the Algorithm name and version
print("Radikāļu neitralizēšanas aktivitātes noteikšana izmantojot viedtālruņa attēlu analīzi RGB krāsu sistēmā / Determination of radical scavenging activity using smartphone image analysis in the RGB colour system")
print("Algorithm version: v.1.0")
print()

# Ievada I0, IDPPH un paraugu skaitu / Input I0, IDPPH and the number of samples
I0 = float(input("Lūdzu, ievadiet I0 vērtību / Please enter the value of I0:"))
IDPPH = float(input("Lūdzu, ievadiet IDPPH vērtību / Please enter a value for IDPPH:"))
paraugu_sk = int(input("Lūdzu, ievadiet analizējamo paraugu skaitu / Please enter the number of samples to be analyzed:"))

# Aprēkina ADPPH vērtību / Calculate the value of ADPPH
ADPPH = -math.log(IDPPH / I0)

data = []

# Cikls, kas nepieciešams, lai iegūtu datus no katra parauga / Loop to obtain data from each sample
for i in range(paraugu_sk):
    parauga_nosaukums = input(f"\nLūdzu, ievadiet {i + 1}. parauga nosaukumu / Please enter {i + 1}. sample name: ")
    R = float(input(f"Lūdzu, ievadiet {parauga_nosaukums} R krāsu kanāla vērtību / Please enter the R colour channel value of {parauga_nosaukums}:"))
    G = float(input(f"Lūdzu, ievadiet {parauga_nosaukums} G krāsu kanāla vērtību / Please enter {parauga_nosaukums} G colour channel value:"))

# Aprēķina RG_avg, Aoil un RSA vērtības / Calculate RG_avg, Aoil un RSA values 
    RG_avg = (R + G) / 2
    Aoil = -math.log(RG_avg / I0)
    RSA = (ADPPH - Aoil) / ADPPH * 100

# Izvada iegūtos datus / print aou the obtained data
    print(f"\n{parauga_nosaukums} iegūtie dati / Data obtained from n{parauga_nosaukums}:")
    print(f"RSA: {RSA:.2f}%")

# Pievieno datus sarakstam / Append data to the list
    data.append([parauga_nosaukums, R, G, RG_avg, Aoil, RSA])

# Izveido DataFrame no datiem / Create a DataFrame from the data
df = pd.DataFrame(data, columns=["Parauga nosaukums Sample name", "R", "G", "RG vidējā vērtība RG average value", "Aoil", "RSA"])

#Ievada MS Excel faila nosaukumu / Input the MS Excel file name and save it
excel_faila_nosaukums = input("\nLūdzu, ievadiet saglabājamo Excel faila nosaukumu (bez .xlsx) / Please enter the name of the Excel file to be saved (without .xlsx): ")

df.to_excel(f"{excel_faila_nosaukums}.xlsx", index=False)

# Izvada pazinojumu par saglabâtu failu / Print a message about the saved file
print(f"Dati ir saglabāti failā {excel_faila_nosaukums}.xlsx / The data is saved in the file {excel_faila_nosaukums}.xlsx")
