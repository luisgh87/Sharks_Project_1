
#1.np.where
np.where(array < 0.5,1,0, np.where(array < 0.8,2,0) #if,elif,else
#donde el array valga menos de 0.5 

array = np.array([pikachu, charmander, squirtle, bulbasau)
np.where(array==pikachu,hola,np)

#2.one hot encoding(get_dummies)
´´´	
import pandas as pd
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
encoding de los paises

se van a crear 35 columnas por cada pais y se van a rellenar con 0 y 1
´´´	
#4.uso de corchetes en pandas
df['columna'] #seleccionar una columna
type(df['columna']) #es una serie
df[["columna"]]#doble corchete para que sea un dataframe
cols = ['columna1','columna2']#lista de columnas
df[cols][df[columna1] > 0.5] #seleccionar columnas y filas

#5.date time
type[df.invoicedate[0]]
str(df.invoicedate[0]) #convertir a string para poder usar el split

#6.sobreescribir un pedazo de un dataframe

df[df.Country=='United Kingdom'].index. #Me da el indice de UK
df.loc[indice,"Quantity"]=-1 #sobreescribo el valor de la cantidad

#7.drop filas
donde el menos uno 
df.drop[columnns=['Quantity'],inplace=True] #inplace para que se quede en el dataframe

#8.generadores
gen = i for i in range(10) #generador de numeros del 0 al 9
next(gen) #me da el primer numero
def gen(n):
    for i in range(n):
        yield i #generador de numeros del 0 al n-1
gen(10)
next(gen) #me da el primer numero

#9.apply a un dataframe
df[[columna1,columna2]].apply(lambda x: x[columna1]*x[columna2],axis=1) #axis=1 para que lo haga por filas
df[columns.sort_values(by='columna1',ascending=False)] #ordenar por columna1 de mayor a menor

#10- Funcional vs POO
#Funcional
def suma(a,b):
    return a+b
#POO
class Suma:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def suma(self):
        return self.a + self.b