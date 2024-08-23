def verificar ( particion , B ) :
    suma_total = 0
    for subgrupo in particion :
        suma_total = sum ( subgrupo ) ** 2
        if suma_total > B :
            return False
    return True