import os

# Nastavení cesty ke složce obsahující soubory
cesta_ke_slozce = './photos/gallery/vertical'

# Získání seznamu všech souborů ve složce
soubory = [soubor for soubor in os.listdir(cesta_ke_slozce) if os.path.isfile(os.path.join(cesta_ke_slozce, soubor))]

# Seřazení souborů podle názvu (můžete upravit podle potřeby)
soubory.sort()

# Smyčka pro přejmenování souborů
for index, soubor in enumerate(soubory, start=1):
    # Rozdělení názvu souboru na jméno a příponu
    jmeno, pripona = os.path.splitext(soubor)
    # Vytvoření nového názvu souboru
    novy_nazev = f'photo{index}{pripona}'
    # Přejmenování souboru
    os.rename(os.path.join(cesta_ke_slozce, soubor), os.path.join(cesta_ke_slozce, novy_nazev))
