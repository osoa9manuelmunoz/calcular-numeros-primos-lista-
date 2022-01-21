from sqlalchemy import true

m = int(input("que numeros 1.000.000.000 presione 1  o 100.000.000.000 presione 2: ")) #aqui se escoje que de los dos numeros va sacar los primos

if 1==m: # si el usuario eligio el 1 pues se realiza el proceso de 1.000.000.000

    def primos(n):
        losprimos=[] # se genera los numros primos en la lista 
        for x in range(2,n): #se cuenta desde 2 al numero indicado que se le dio a n 

            val=True #val agrega aquellos valores nesesarios si se ha realizado bien las operaciones necesaria 

            for y in range(2,x): 

                if x%y == 0: #si x e y se genera un resultado igual a 0, no esta cumpliendo las reglas de los primos 

                    val=False #entonces no se va validar el numero 
                    break
                    
            if val: #como se determino el funcionamiento de val agrgara aquellos verdaderos y lo que no pues no se agregan 

                losprimos.append(x)  #aqui se empiesa agregar los valores   
        return losprimos     
    n=1000000000
    print(primos(n))
    print("la cantidad de numeros primos que se encuentra son: ",len(primos(n))) # como es una lista se utiliza len para que cuente todos los numeros que se encuentre hay

elif 2==m: # en esta caso no se eligio el 1 pues el 2 y se realiza el procedimiento 

        def primos(n):
            losprimos=[]
            for x in range(2,n): 
                val=True
                for y in range(2,x): 
                    if x%y == 0: 
                       val=False
                       break
                if val: 
                    losprimos.append(x)    
            return losprimos     
        n=100000000000
        print(primos(n))
        print("la cantidad de numeros primos que se encuentra son: ",len(primos(n)))
    
else:
    print("por favor elegir al guno de los nos numeros que se le indica") # si el usuario da un numero con respecto 1 o 2 pues se le envia este mensaje 








    




