idm = 0
idn = 0
for c in range (1, 8):
    pess = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if 2025 - pess >= 18:
        idm = idm + 1
    else:
        idn = idn + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(idm))
print("E também tivemos {} pessoas menores de idade".format(idn))