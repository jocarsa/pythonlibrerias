def gris(pixeles,anchura,altura):
    for x in range(0,anchura):
        for y in range(0,altura):
            rojo = pixeles[x,y][0]
            pixeles[x,y] = (rojo,rojo,rojo)
    return pixeles

def umbral(pixeles,anchura,altura):
    for x in range(0,anchura):
        for y in range(0,altura):
            rojo = pixeles[x,y][0]
            if rojo < 127:
                pixeles[x,y] = (0,0,0)
            else:
                pixeles[x,y] = (255,255,255)
    return pixeles
