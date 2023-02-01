import math 

def sumcplx(c1,c2):
    real = (c1[0]+c2[0])
    img = (c1[1]+c2[1])
    resultado = (real,img)
    return resultado

def multcplx(c1,c2):
    real = ((c1[0]*c2[0])-(c1[1]*c2[1]))
    img = ((c1[0]*c2[1])+(c2[0]*c1[1]))
    resultado = (real,img)
    return resultado 

def restcplx(c1,c2):
    real = (c1[0]-c2[0])
    img = (c1[1]-c2[1])
    resultado = (real,img)
    return resultado

def divcplx(c1,c2):
    real = ((c1[0]*(c2[0]))+(c1[1]*c2[1]))/(c2[0]**2+c2[1]**2)
    img = ((c2[0]*(c1[1]))-(c1[0]*c2[1]))/(c2[0]**2+c2[1]**2)
    resultado = (real,img)
    return resultado
    
def modcplx(c):
    resultado = math.sqrt(c[0]**2+c[1]**2)
    return resultado

def conjcplx(c):
    real = (c[0])
    img = (c[1]*(-1))
    resultado = (real,img)
    return resultado

def ptoccplx(c):
    modulo = (modcplx((c[0],c[1])))
    fase = (math.radians(fasecplx((c[0],c[1]))))
    cos = math.cos(fase)
    sin = math.sin(fase)
    real = (modulo*cos)
    img = (modulo*sin)
    resultado = (real,img)
    return resultado

def fasecplx(c):
    fase = math.degrees(math.atan2(c[1],c[0]))
    return fase

def prettypcplx(c):
    resultado = print(c[0],"+",c[1],"i")
    return resultado
    