#!/usr/bin/env python
# coding: utf-8

# <img src="Archivos/miad4.png" width=800x>
# 
# # Estructuras de datos: listas, tuplas, conjuntos y diccionarios
# 
# En este taller implementarás listas, tuplas y diccionarios para resolver diversos ejercicios.
# 
# 
# ## Habilidades en práctica
# 
# Al realizar este taller podrás revisar tu progreso para:
# 
# **1.** Declarar tuplas, listas y diccionarios.<br> 
# **2.** Consultar y modificar los valores almacenados en estructuras de datos y estructuras de datos anidadas.<br> 
# **3.** Utilizar el rebanado en estructuras de datos ordenadas (listas y tuplas).<br> 
# **4.** Utilizar métodos para modificar, reordenar, u operar estructuras de datos.<br> 
# 
# 
# ## Instrucciones
# 
# En cada uno de los siguientes ejercicios deberás escribir el código solicitado estrictamente en las celdas indicadas para ello, teniendo en cuenta las siguientes recomendaciones:
# 
# * No crear, eliminar o modificar celdas de este Notebook (salvo lo que se te indique), pues puede verse afectado el proceso de calificación automática.
# * La calificación se realiza de manera automática con datos diferentes a los proporcionados en este taller. Por consiguiente, tu código debe funcionar para diferentes instancias de cada uno de los ejercicios; una instancia hace referencia al valor de los parámetros.
# * La calificación de cada ejercicio depende del valor que tome la variable especificada en su enunciado. Por lo tanto, aunque declares variables adicionales en tu código, es escencial que utilices los nombres de las variables propuestas en los enunciados de los ejercicios para guardar el resultado final.
# 
# A continuación puedes ver un ejemplo de los enunciados y ejercicios que encontrarás en este taller.

# ## Meses del año
# 
# A continuación encuentras una lista llamada `lista_meses` que contiene todos los meses del año.

# In[3]:


# No modifiques esta celda

lista_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


# ### Ejemplo
# 
# Extrae los últimos tres meses del año de la lista `lista_meses` y almacénalos en una nueva lista llamada `cuarto_trimestre`.

# In[4]:


# YOUR CODE HERE
cuarto_trimestre = lista_meses[-3:]
cuarto_trimestre


# ## El proyecto inmobiliario 
# 
# El gerente de un proyecto inmobiliario registró en la siguiente tabla el número de casas vendidas en los últimos seis meses:
# 
# |Mes|Ventas|
# |:-------:|:-----------:|
# |1| 20|
# |2| 21|
# |3| 22|
# |4| 20|
# |5| 21|
# |6| 27|
# 
# *Resuelve los ejercicios del 1 al 3 con base en este enunciado.*

# ### Ejercicio 1
# 
# Declara una lista llamada `lista_ventas` en la que se almacene la información de la columna ventas.

# In[5]:


# YOUR CODE HERE
lista_ventas = [20,21,22,20,21,27]


# In[6]:


## PRUEBAS

# Caso 1: no existe la lista.
try:
    lista_ventas
except:
    raise NotImplementedError("No declaraste una variable llamada lista_ventas.",)
    
# Caso 2: el código se ejecuta con errores
try:
    exec(_i)
except:
    raise RuntimeError("Tu código produce un error al ejecutarse.")

# Caso 3: no es una lista.
assert type(lista_ventas) == list, f"Tu variable lista_ventas no es de tipo {list.__name__}."
    
# Caso 4: la lista contiene valores de tipo incorrecto
for i in lista_ventas:
    assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."

# Caso 5: la lista no contiene todos los valores correctos
try:
    assert lista_ventas.count(20) >= 2
    assert lista_ventas.count(21) >= 2
    assert lista_ventas.count(22) >= 1
    assert lista_ventas.count(27) >= 1
except AssertionError as e:
    e.args += ("Tu lista no contiene toda la información de la tabla.",)
    raise e
    
# Caso 6: la lista contiene valores que no existen en la columna
assert len(set(lista_ventas)) == 4, "Tu lista contiene valores incorrectos."

# Caso 7: la lista tiene el tamaño incorrecto
assert len(lista_ventas) == 6, "Tu lista tiene un tamaño mayor al esperado."

# Caso 8: la lista es correcta
try:
    assert lista_ventas[0] == 20
    assert lista_ventas[1] == 21
    assert lista_ventas[2] == 22
    assert lista_ventas[3] == 20
    assert lista_ventas[4] == 21
    assert lista_ventas[5] == 27
except AssertionError as e:
    e.args += ("Los valores de tu lista están desordenados.",)
    raise e

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 2 
# 
# De manera inesperada, a algunos de los compradores del mes `mes_a_actualizar` le negaron el crédito. Teniendo en cuenta lo anterior, el número de casas vendidas de ese mes ha sido actualizado y está almacenado en la variable `ventas_mes_a_actualizar`. Utiliza estas variables en tu código.

# In[8]:


# No modifiques esta celda

mes_a_actualizar = 4
ventas_mes_a_actualizar = 18


# Modifica la lista de ventas `lista_ventas` para actualizar ese valor.

# In[9]:


# YOUR CODE HERE
lista_ventas [mes_a_actualizar-1]= ventas_mes_a_actualizar


# In[10]:


## PRUEBAS

# Base variables
lista_ventas = [20, 21, 22, 20, 21, 27]
mes_a_actualizar = 3
ventas_mes_a_actualizar = 17

try:
    # Caso 1: no existe la lista.
    try:
        lista_ventas
    except:
        raise NotImplementedError("No existe una variable llamada lista_ventas.",)
        
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
        
    # Caso 3: el código modifica los parametros del problema
    try:
        assert mes_a_actualizar == 3
        assert ventas_mes_a_actualizar == 17
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
        
    # Caso 4: no es una lista.
    assert type(lista_ventas) == list, f"Tu variable lista_ventas no es de tipo {list.__name__}."

    # Caso 5: el código no utiliza las variables mes_a_actualizar y ventas_mes_a_actualizar
    assert _i.find("mes_a_actualizar") >= 0, "Tu código no utiliza la variable mes_a_actualizar."
    assert _i.find("ventas_mes_a_actualizar") >= 0, "Tu código no utiliza la variable ventas_mes_a_actualizar."

    # Caso 6: la lista contiene valores de tipo incorrecto
    for i in lista_ventas:
        assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."

    # Caso 7: la lista tiene el tamaño incorrecto
    assert len(lista_ventas) == 6, "Tu lista no tiene el tamaño correcto."

    # Caso 8: la lista es correcta
    try:
        assert lista_ventas[0] == 20
        assert lista_ventas[1] == 21
        assert lista_ventas[mes_a_actualizar - 1] == ventas_mes_a_actualizar
        assert lista_ventas[3] == 20
        assert lista_ventas[4] == 21
        assert lista_ventas[5] == 27
    except AssertionError as e:
        e.args += ("Tu respuesta es incorrecta. Es posible que no hayas modificado la posición correcta.",)
        raise e
        
except:
    # Restaurar variables base originales
    mes_a_actualizar = 4
    ventas_mes_a_actualizar = 18
    raise
    
finally:
    # Restaurar variables base originales y respuesta estudiante
    mes_a_actualizar = 4
    ventas_mes_a_actualizar = 18
    lista_ventas = [20, 21, 22, 20, 21, 27]
    exec(_i)

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 3
# 
# El gerente del proyecto solicitó que se le reporten los `n` mayores niveles de ventas mensuales de casas, ordenados de mayor a menor. La variable en la que guardes el resultado debe tener el nombre `mejores_ventas`. Haz uso de la lista `lista_ventas`.
# 
# **Pista:** el método `sort` recibe un parámetro llamado `reverse`.

# In[11]:


# No modifiques esta celda

n = 3


# In[12]:


# YOUR CODE HERE
lista_ventas.sort()
lista_ventas.reverse()
mejores_ventas = lista_ventas[0:n]
mejores_ventas


# In[13]:


## PRUEBAS

# Base variables
n = 4

try:
    # Caso 1: no existe la lista.
    try:
        mejores_ventas
    except:
        raise NotImplementedError("No declaraste una variable llamada mejores_ventas.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert n == 4
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es una lista.
    assert type(mejores_ventas) == list, f"Tu variable mejores_ventas no es de tipo {list.__name__}."

    # Caso 5: el código no utiliza las variables mes_a_actualizar y ventas_mes_a_actualizar
    assert _i.find("lista_ventas") >= 0, "Tu código no utiliza la variable lista_ventas."
    assert _i.find("n") >= 0, "Tu código no utiliza la variable n."

    # Caso 6: la lista contiene valores de tipo incorrecto
    for i in mejores_ventas:
        assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."
    
    # Caso 7: la lista tiene el tamaño incorrecto
    assert len(mejores_ventas) == n, "Tu lista no tiene el tamaño correcto."
    
    # Caso 8: la lista no contiene los valores correctos
    try:
        assert mejores_ventas.count(22) >= 1
        assert mejores_ventas.count(21) >= 2
        assert mejores_ventas.count(27) >= 1
    except AssertionError as e:
        e.args += ("Tu lista no contiene los valores correctos.",)
        raise e

    # Caso 9: la lista es correcta
    try:
        assert mejores_ventas[0] >= mejores_ventas[1]
        assert mejores_ventas[1] >= mejores_ventas[2]
        assert mejores_ventas[2] >= mejores_ventas[3]
    except AssertionError as e:
        e.args += ("Tu lista no esta en orden descendente.",)
        raise e
        
    # Caso 10: la lista no esta ordenada
    try:
        assert mejores_ventas[0] == 27
        assert mejores_ventas[1] == 22
        assert mejores_ventas[2] == 21
        assert mejores_ventas[3] == 21
    except AssertionError as e:
        e.args += ("Tu respuesta es incorrecta.",)
        raise e  
        
except:
    # Restaurar variables base originales
    n = 3
    raise

finally:
    # Restaurar variables base originales
    n = 3

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## La compañía de encuestas
# 
# Una compañía de encuestas requiere hacer llamadas telefónicas a un grupo de personas y solo cuenta con dos operarios. Un operario debe llamar a la primera mitad de las personas (ordenándolas alfabéticamente), mientras que el otro llamará a la segunda mitad. La variable `nombres` almacena una lista con los nombres de las personas a llamar.

# In[14]:


# No modifiques esta celda

nombres = ["Sara", "Juan", "Alberto", "Ana", "Enrique", "Lola"]


# ### Ejercicio 4
# 
# Haciendo uso de la lista `nombres` y otras posibles listas auxiliares que necesites, debes crear las siguientes dos listas:
# 
# * La primera debe llamarse `primera_mitad` y contener la primera mitad de las personas en orden alfábetico. En caso de haber un número impar de personas, por ejemplo 5, en esta primera lista se incluyen las primeras tres personas.
# * La segunda debe llamarse `segunda_mitad` y contener la segunda mitad de personas, según el orden alfabético.
# 
# **Pista:** para aproximar números decimales a enteros, el paquete `math` incluye las funciones `ceil` (aproxima al entero superior) y `floor` (aproxima al entero inferior).

# In[18]:


# YOUR CODE HERE

nombres.sort()
import math
numero= math.ceil(len(nombres)/2)

primera_mitad = nombres[0: numero]
print(primera_mitad)

segunda_mitad = nombres[- numero +1:]
print(segunda_mitad)


# In[19]:


## PRUEBAS

# Base variables
nombres = ["Andrea", "Felipe", "Emilio", "Carolina", "Gabriel", "Susana", "Antonia"]

try:
    # Caso 1: no se declaro la lista
    # primera_mitad
    try:
        primera_mitad
    except:
        raise NotImplementedError("No declaraste una variable llamada primera_mitad.",)
        
    # segunda_mitad
    try:
        segunda_mitad
    except:
        raise NotImplementedError("No declaraste una variable llamada segunda_mitad.",)
    
    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert nombres == ["Andrea", "Felipe", "Emilio", "Carolina", "Gabriel", "Susana", "Antonia"]
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es una lista.
    # primera_mitad
    assert type(primera_mitad) == list, f"Tu variable primera_mitad no es de tipo {list.__name__}."
    
    # segunda_mitad
    assert type(segunda_mitad) == list, f"Tu variable segunda_mitad no es de tipo {list.__name__}."
        
    # Caso 5: el código no utiliza la lista nombres 
    assert _i.find("nombres") >= 0, "Tu código no utiliza la lista nombres."

    # Caso 6: la lista contiene valores de tipo incorrecto
    # primera_mitad
    for i in primera_mitad:
        assert type(i) == str, f"Tu lista primera_mitad contiene valores que no son de tipo {str.__name__}."
    
    # segunda_mitad
    for i in segunda_mitad:
        assert type(i) == str, f"Tu lista segunda_mitad contiene valores que no son de tipo {str.__name__}."
    
    # Caso 7: las listas tienen el tamaño incorrecto
    # primera_mitad
    assert len(primera_mitad) == 4, "Tu lista primera_mitad no tiene el tamaño correcto."
    
    # segunda_mitad
    assert len(segunda_mitad) == 3, "Tu lista segunda_mitad no tiene el tamaño correcto."
    
    # Caso 8: la lista no contiene los valores correctos
    # primera_mitad
    try:
        assert primera_mitad.count("Andrea") >= 1
        assert primera_mitad.count("Antonia") >= 1
        assert primera_mitad.count("Carolina") >= 1
        assert primera_mitad.count("Emilio") >= 1
    except AssertionError as e:
        e.args += ("Tu lista primera_mitad no contiene los valores correctos.",)
        raise e
        
    # segunda_mitad
    try:
        assert segunda_mitad.count("Felipe") >= 1
        assert segunda_mitad.count("Gabriel") >= 1
        assert segunda_mitad.count("Susana") >= 1
    except AssertionError as e:
        e.args += ("Tu lista segunda_mitad no contiene los valores correctos.",)
        raise e

    # Caso 9: las listas son correctas
    # primera_mitad
    try:
        assert primera_mitad[0] == "Andrea"
        assert primera_mitad[1] == "Antonia"
        assert primera_mitad[2] == "Carolina"
        assert primera_mitad[3] == "Emilio"
    except AssertionError as e:
        e.args += ("Tu respuesta es incorrecta. Es posible que tu lista primera_mitad no este ordenada alfabéticamente.",)
        raise e
    
    # segunda_mitad
    try:
        assert segunda_mitad[0] == "Felipe"
        assert segunda_mitad[1] == "Gabriel"
        assert segunda_mitad[2] == "Susana"
    except AssertionError as e:
        e.args += ("Tu respuesta es incorrecta. Es posible que tu lista segunda_mitad no este ordenada alfabéticamente.",)
        raise e   
    
except:
    # Restaurar variables base originales
    nombres = ["Sara", "Juan", "Alberto", "Ana", "Enrique", "Lola"]
    raise
    
finally:
    # Restaurar variables base originales
    nombres = ["Sara", "Juan", "Alberto", "Ana", "Enrique", "Lola"]

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Las letras del abecedario
# 
# A continuación encontrarás declarada una lista que contiene listas anidadas con las letras del alfabeto.
# 
# *Resuelve los ejercicios del 5 al 8 con base en este enunciado.*

# In[20]:


# No modifiques esta celda

lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]


# ### Ejercicio 5
# 
# Haciendo uso de la lista `lista_abecedario`, obtén las primeras tres letras del abecedario y almacénalas en una lista con nombre `lista_abc`. 

# In[21]:


# YOUR CODE HERE
lista_abc = lista_abecedario[0:3]
lista_abc


# In[22]:


## PRUEBAS

# Caso 1: no existe la lista.
try:
    lista_abc
except:
    raise NotImplementedError("No declaraste una variable llamada lista_abc.",)

# Caso 2: el código se ejecuta con errores
try:
    exec(_i)
except:
    raise RuntimeError("Tu código produce un error al ejecutarse.")

# Caso 3: no es una lista.
assert type(lista_abc) == list, f"Tu variable lista_abc no es de tipo {list.__name__}."

# Caso 4: el código no utiliza la lista lista_abecedario 
assert _i.find("lista_abecedario") >= 0, "Tu código no utiliza la lista lista_abecedario."

# Caso 5: la lista contiene valores de tipo incorrecto
for i in lista_abc:
    assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
    
# Caso 6: la lista no contiene los valores esperados
try:
    assert lista_abc.count('a') >= 1
    assert lista_abc.count('b') >= 1
    assert lista_abc.count('c') >= 1
except AssertionError as e:
    e.args += ("Tu lista no contiene los valores correctos.",)
    raise e

# Caso 7: la lista tiene el tamaño incorrecto
assert len(lista_abc) == 3, "Tu lista no tiene el tamaño correcto."

# Caso 8: la lista es correcta
try:
    assert lista_abc[0] == 'a'
    assert lista_abc[1] == 'b'
    assert lista_abc[2] == 'c'
except AssertionError as e:
    e.args += ("Los valores de tu lista están desordenados.",)
    raise e

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 6
# 
# Haciendo uso de la lista `lista_abecedario`, obtén una lista con las letras d y e, y almacénala en una lista con nombre `lista_de`.

# In[23]:


# YOUR CODE HERE
lista_de = lista_abecedario[3][0:2]
lista_de


# In[24]:


## PRUEBAS

# Caso 1: no existe la lista.
try:
    lista_de
except:
    raise NotImplementedError("No declaraste una variable llamada lista_de.",)

# Caso 2: el código se ejecuta con errores
try:
    exec(_i)
except:
    raise RuntimeError("Tu código produce un error al ejecutarse.")

# Caso 3: no es una lista.
assert type(lista_de) == list, f"Tu variable lista_de no es de tipo {list.__name__}."

# Caso 4: el código no utiliza la lista lista_abecedario 
assert _i.find("lista_abecedario") >= 0, "Tu código no utiliza la lista lista_abecedario."

# Caso 5: la lista contiene valores de tipo incorrecto
for i in lista_de:
    assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
    
# Caso 6: la lista no contiene los valores esperados
try:
    assert lista_de.count('d') >= 1
    assert lista_de.count('e') >= 1
except AssertionError as e:
    e.args += ("Tu lista no contiene los valores correctos.",)
    raise e

# Caso 7: la lista tiene el tamaño incorrecto
assert len(lista_de) == 2, "Tu lista no tiene el tamaño correcto."

# Caso 8: la lista es correcta
try:
    assert lista_de[0] == 'd'
    assert lista_de[1] == 'e'
except AssertionError as e:
    e.args += ("Los valores de tu lista están desordenados.",)
    raise e

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 7
# 
# Haciendo uso de la lista `lista_abecedario` y posibles listas auxiliares que necesites, crea una lista con las letras f, g y h, y almacénala en una lista con nombre `lista_fgh`. 

# In[25]:


# YOUR CODE HERE
lista_fgh = lista_abecedario[3][2] + ["h"] 
lista_fgh


# In[26]:


## PRUEBAS

# Caso 1: no existe la lista.
try:
    lista_fgh
except:
    raise NotImplementedError("No declaraste una variable llamada lista_fgh.",)

# Caso 2: el código se ejecuta con errores
try:
    exec(_i)
except:
    raise RuntimeError("Tu código produce un error al ejecutarse.")

# Caso 3: no es una lista.
assert type(lista_fgh) == list, f"Tu variable lista_fgh no es de tipo {list.__name__}."

# Caso 4: el código no utiliza la lista lista_abecedario 
assert _i.find("lista_abecedario") >= 0, "Tu código no utiliza la lista lista_abecedario."

# Caso 5: la lista contiene valores de tipo incorrecto
for i in lista_fgh:
    assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
    
# Caso 6: la lista no contiene los valores esperados
try:
    assert lista_fgh.count('f') >= 1
    assert lista_fgh.count('g') >= 1
    assert lista_fgh.count('h') >= 1
except AssertionError as e:
    e.args += ("Tu lista no contiene los valores correctos.",)
    raise e

# Caso 7: la lista tiene el tamaño incorrecto
assert len(lista_fgh) == 3, "Tu lista no tiene el tamaño correcto."

# Caso 8: la lista es correcta
try:
    assert lista_fgh[0] == 'f'
    assert lista_fgh[1] == 'g'
    assert lista_fgh[2] == 'h'
except AssertionError as e:
    e.args += ("Los valores de tu lista estan desordenados.",)
    raise e

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 8
# 
# Haciendo uso de las listas anteriormente creadas y posibles listas auxiliares que necesites, genera una lista que contenga las primeras diez letras del abecedario y llámala `lista_a_j`.

# In[27]:


# YOUR CODE HERE
lista_ij = ["i","j"]
lista_a_j = lista_abc + lista_de + lista_fgh + lista_ij
lista_a_j


# In[28]:


## PRUEBAS

# Caso 1: no existe la lista.
try:
    lista_a_j
except:
    raise NotImplementedError("No declaraste una variable llamada lista_a_j.",)

# Caso 2: el código se ejecuta con errores
try:
    exec(_i)
except:
    raise RuntimeError("Tu código produce un error al ejecutarse.")
    
# Caso 3: no es una lista.
assert type(lista_a_j) == list, f"Tu variable lista_a_j no es de tipo {list.__name__}."

# Caso 4: el código no utiliza las listas lista_abc, lista_de y lista_fgh
assert _i.find("lista_abc") >= 0, "Tu código no utiliza la lista lista_abc."
assert _i.find("lista_de") >= 0, "Tu código no utiliza la lista lista_de."
assert _i.find("lista_fgh") >= 0, "Tu código no utiliza la lista lista_fgh."

# Caso 5: la lista contiene valores de tipo incorrecto
for i in lista_a_j:
    assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
    
# Caso 6: la lista no contiene los valores esperados
try:
    assert lista_a_j.count('a') >= 1
    assert lista_a_j.count('b') >= 1
    assert lista_a_j.count('c') >= 1
    assert lista_a_j.count('d') >= 1
    assert lista_a_j.count('e') >= 1
    assert lista_a_j.count('f') >= 1
    assert lista_a_j.count('g') >= 1
    assert lista_a_j.count('h') >= 1
    assert lista_a_j.count('i') >= 1
    assert lista_a_j.count('j') >= 1
except AssertionError as e:
    e.args += ("Tu lista no contiene los valores correctos.",)
    raise e

# Caso 7: la lista tiene el tamaño incorrecto
assert len(lista_fgh) == 3, "Tu lista no tiene el tamaño correcto."

# Caso 8: la lista es correcta
try:
    assert lista_a_j[0] == 'a'
    assert lista_a_j[1] == 'b'
    assert lista_a_j[2] == 'c'
    assert lista_a_j[3] == 'd'
    assert lista_a_j[4] == 'e'
    assert lista_a_j[5] == 'f'
    assert lista_a_j[6] == 'g'
    assert lista_a_j[7] == 'h'
    assert lista_a_j[8] == 'i'
    assert lista_a_j[9] == 'j'
except AssertionError as e:
    e.args += ("Los valores de tu lista estan desordenados.",)
    raise e

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Los números primos
# 
# Un equipo de ingenieros de sistemas está trabajando con números primos para realizar encriptaciones, en la siguiente celda encuentras los números primos del 1 al 100.
# 
# *Resuelve los ejercicios 9 y 10 con base en este enunciado.*

# In[29]:


# No modifiques esta celda

tupla_primos =  (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


# ### Ejercicio 9
# 
# Encuentra cuál índice de la tupla `tupla_primos` le corresponde al número `a_buscar` y almacénalo en una variable llamada `indice`.

# In[31]:


# No modifiques esta celda

a_buscar = 73


# In[32]:


# YOUR CODE HERE
indice = tupla_primos.index(a_buscar)


# In[33]:


## PRUEBAS

# Base variables
a_buscar = 73

try:
    # Caso 1: no existe la variable.
    try:
        indice
    except:
        raise NotImplementedError("No declaraste una variable llamada indice.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert a_buscar == 73
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
        
    # Caso 4: no es de tipo int.
    assert type(indice) == int, f"Tu variable indice no es de tipo {int.__name__}."

    # Caso 5: el código no utiliza las variables tupla_primos y a_buscar
    assert _i.find("tupla_primos") >= 0, "Tu código no utiliza la variable tupla_primos."
    assert _i.find("a_buscar") >= 0, "Tu código no utiliza la variable a_buscar."

    # Caso 6: la respuesta es correcta
    assert indice == 20, "Tu respuesta es incorrecta."
        
except:
    # Restaurar variables base originales
    a_buscar = 41
    raise
    
finally:
    # Restaurar variables base originales
    a_buscar = 41

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 10
# 
# El equipo de ingenieros de sistemas decidió cambiar levemente los números a usar para la encriptación. Ahora, en vez de utilizar todos los números primos del 1 al 100, decidieron elegir un número sí, un número no, dentro de un rango definido por `lim_inferior` y `lim_superior` (incluyéndolos). Por ejemplo, si `lim_inferior` es 5 y `lim_superior` es 31, los números utilizados para la encriptación serían los siguientes: 5,11,17,23,31. 
# 
# Crea una tupla con la secuencia que necesita el equipo y llámala `tupla_secuencia`. Haz uso de la tupla `tupla_primos`.
# 
# **Pista**: a la instrucción de rebanado se le puede agregar un tercer elemento separándolo con dos puntos, para indicar a cuantos pasos rebanar la estructura de datos ordenada. Ejemplo: `tupla[indice_inicio : indice_fin : pasos]`

# In[36]:


# No modifiques esta celda

lim_inferior = 3
lim_superior = 53


# In[37]:


# YOUR CODE HERE
indice1 = tupla_primos.index(lim_inferior)
indice2 = tupla_primos.index(lim_superior)


tupla_secuencia = tupla_primos[indice1:indice2 +1 : 2]
tupla_secuencia


# In[38]:


## PRUEBAS

# Base variables
lim_inferior = 17
lim_superior = 47

try:
    # Caso 1: no existe la tupla.
    try:
        tupla_secuencia
    except:
        raise NotImplementedError("No declaraste una variable llamada tupla_secuencia.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert lim_inferior == 17
        assert lim_superior == 47
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")

    # Caso 4: no es una tupla.
    assert type(tupla_secuencia) == tuple, f"Tu variable tupla_secuencia no es de tipo {tuple.__name__}."
        
    # Caso 5: el código no utiliza las variables tupla_primos, lim_inferior y lim_superior 
    assert _i.find("tupla_primos") >= 0, "Tu código no utiliza la variable tupla_primos."
    assert _i.find("lim_inferior") >= 0, "Tu código no utiliza la variable lim_inferior."
    assert _i.find("lim_superior") >= 0, "Tu código no utiliza la variable lim_superior."

    # Caso 6: la tupla contiene valores de tipo incorrecto
    for i in tupla_secuencia:
        assert type(i) == int, f"Tu tupla contiene valores que no son de tipo {int.__name__}."

    # Caso 7: la tupla no contiene los limites correctos
    assert tupla_secuencia[0] == lim_inferior, "Tu tupla no inicia en el límite inferior."
    assert tupla_secuencia[len(tupla_secuencia)-1] == lim_superior, "Tu tupla no termina en el límite superior."

    # Caso 8: la tupla tiene el tamaño incorrecto
    assert len(tupla_secuencia) == 5, "Tu tupla no tiene el tamaño correcto."

    # Caso 9: la tupla es correcta
    try:
        assert tupla_secuencia[0] == 17
        assert tupla_secuencia[1] == 23
        assert tupla_secuencia[2] == 31
        assert tupla_secuencia[3] == 41
        assert tupla_secuencia[4] == 47
    except AssertionError as e:
        e.args += ("Tu respuesta es incorrecta.",)
        raise e
        
except:
    # Restaurar variables base originales
    lim_inferior = 3
    lim_superior = 53
    raise

finally:
    # Restaurar variables base originales
    lim_inferior = 3
    lim_superior = 53

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## La fábrica de muebles
# 
# Una fábrica de muebles hace escritorios a la medida con dos tipos de madera: caoba y arce. La empresa registró los pedidos semanales de ambas referencias de madera: en la primera semana debe fabricar tres escritorios de caoba y dos de arce, en la segunda semana necesita dos escritorios de caoba y cuatro de arce, y en la última semana un escritorio de cada tipo.
# 
# En la siguiente celda encontrarás tres tuplas que hacen referencia a los pedidos de cada semana. 
# 
# *Resuelve los ejercicios 11 y 12 con base en este enunciado.*

# In[39]:


# No modifiques esta celda

pedidos_semana_1 = (3,2)
pedidos_semana_2 = (2,4)
pedidos_semana_3 = (1,1)


# ### Ejercicio 11
# 
# Declara una tupla con el nombre `tupla_pedidos` que anide las tres tuplas declaradas en la anterior celda de código. La tupla `tupla_pedidos` debe quedar en órden cronológico.

# In[40]:


# YOUR CODE HERE
tupla_pedidos = (pedidos_semana_1 , pedidos_semana_2 ,pedidos_semana_3)
tupla_pedidos


# In[41]:


## PRUEBAS

# Base variables
pedidos_semana_1 = (5,4)
pedidos_semana_2 = (3,3)
pedidos_semana_3 = (1,6)

try:
    # Caso 1: no existe la tupla.
    try:
        tupla_pedidos
    except:
        raise NotImplementedError("No declaraste una variable llamada tupla_pedidos.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert pedidos_semana_1 == (5,4)
        assert pedidos_semana_2 == (3,3)
        assert pedidos_semana_3 == (1,6)
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es una tupla.
    assert type(tupla_pedidos) == tuple, f"Tu variable tupla_pedidos no es de tipo {tuple.__name__}."

    # Caso 5: el código no utiliza las variables pedidos_semana_1, pedidos_semana_2 y pedidos_semana_3 
    assert _i.find("pedidos_semana_1") >= 0, "Tu código no utiliza la variable pedidos_semana_1."
    assert _i.find("pedidos_semana_2") >= 0, "Tu código no utiliza la variable pedidos_semana_2."
    assert _i.find("pedidos_semana_3") >= 0, "Tu código no utiliza la variable pedidos_semana_3."

    # Caso 6: la tupla contiene valores de tipo incorrecto
    for i in tupla_pedidos:
        assert type(i) == tuple, f"Tu tupla contiene valores que no son de tipo {tuple.__name__}. Es posible que no tengas las tuplas anidadas."
        
    # Caso 7: la lista no contiene los valores esperados
    try:
        assert tupla_pedidos.count((5,4)) >= 1
        assert tupla_pedidos.count((3,3)) >= 1
        assert tupla_pedidos.count((1,6)) >= 1
    except AssertionError as e:
        e.args += ("Tu lista no contiene los valores correctos.",)
        raise e

    # Caso 8: la tupla tiene el tamaño incorrecto
    assert len(tupla_pedidos) == 3, "Tu tupla no tiene el tamaño correcto."

    # Caso 9: la tupla es correcta
    try:
        assert tupla_pedidos[0] == (5,4)
        assert tupla_pedidos[1] == (3,3)
        assert tupla_pedidos[2] == (1,6)
    except AssertionError as e:
        e.args += ("Los valores de tu tupla están desordenados.",)
        raise e

except:
    # Restaurar variables base originales
    pedidos_semana_1 = (3,2)
    pedidos_semana_2 = (2,4)
    pedidos_semana_3 = (1,1)
    raise

finally:
    # Restaurar variables base originales y respuesta estudiante
    pedidos_semana_1 = (3,2)
    pedidos_semana_2 = (2,4)
    pedidos_semana_3 = (1,1)
    exec(_i) 

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 12
# 
# Utiliza la función de Python `sum` para obtener el total de pedidos de la semana `s` y almacena el resultado en una variable llamada `total_pedidos_semana_s`. Haz uso de la tupla `tupla_pedidos`.

# In[42]:


# No modifiques esta celda

s = 2


# In[43]:


# YOUR CODE HERE
total_pedidos_semana_s = sum(tupla_pedidos[s-1])
total_pedidos_semana_s


# In[44]:


## PRUEBAS

# Base variables
s = 1

try:
    # Caso 1: no existe la variable.
    try:
        total_pedidos_semana_s
    except:
        raise NotImplementedError("No declaraste una variable llamada total_pedidos_semana_s.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert s == 1
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es un int.
    assert type(total_pedidos_semana_s) == int, f"Tu variable total_pedidos_semana_s no es de tipo {int.__name__}."

    # Caso 5: el código no utiliza la variable tupla_pedidos
    assert _i.find("tupla_pedidos") >= 0, "Tu código no utiliza la variable tupla_pedidos."
   
    # Caso 6: la respuesta es correcta
    assert total_pedidos_semana_s == 5, "Tu respuesta es incorrecta."
    
except:
    # Restaurar variables base originales
    s = 2
    raise

finally:
    # Restaurar variables base originales
    s = 2

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Meses 
# 
# En la siguiente celda encontrarás un diccionario incompleto con el último día de cada mes del año.

# In[45]:


# No modifiques esta celda

dicc_meses = {"Enero":31,
              "Febrero":28,
              "Marzo": 31,
              "Abril": 30,
              "Mayo":31,
              "Julio":31,
              "Agosto":31,
              "Septiembre":30,
              "Noviembre":30}


# ### Ejercicio 13
# 
# Completa el diccionario `dicc_meses` con los meses faltantes.

# In[46]:


# YOUR CODE HERE
dicc_meses["Junio"] = 30
dicc_meses["Octubre"] = 31
dicc_meses["Diciembre"] = 31
dicc_meses


# In[47]:


## PRUEBAS

# Caso 1: no existe el diccionario.
try:
    dicc_meses
except:
    raise NotImplementedError("No existe una variable llamada dicc_meses.",)
    
# Caso 2: el código se ejecuta con errores
try:
    exec(_i)
except:
    raise RuntimeError("Tu código produce un error al ejecutarse.")
    
# Caso 3: no es un diccionario.
assert type(dicc_meses) == dict, f"Tu variable dicc_meses no es de tipo {dict.__name__}."

# Caso 4: el código no utiliza el diccionario dicc_meses
assert _i.find("dicc_meses") >= 0, "Tu código no utiliza el diccionario dicc_meses."

# Caso 5: el diccionario contiene valores de tipo incorrecto
for i in dicc_meses.keys():
    assert type(i) == str, f"Tu diccionario contiene llaves que no son de tipo {str.__name__}."

for j in dicc_meses.values():
    assert type(j) == int, f"Tu diccionario contiene valores que no son de tipo {int.__name__}."

# Caso 6: el diccionario tiene el tamaño incorrecto
assert len(dicc_meses) == 12, "Tu diccionario no tiene el tamaño correcto."
    
# Caso 7: el diccionario no contiene los valores/llaves correctos/as
assert set(dicc_meses.keys()) == {'Diciembre', 'Noviembre', 'Octubre', 'Septiembre', 'Agosto', 'Julio', 'Junio', 'Mayo', 'Abril', 'Marzo', 'Febrero', 'Enero'}, "Las llaves de tu diccionario no son correctas."
assert set(dicc_meses.values()) == {31, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 28}, "Los valores de tu diccionario no son correctos."

# Caso 8: el diccionario es correcto 
try:
    assert dicc_meses['Enero'] == 31
    assert dicc_meses['Febrero'] == 28
    assert dicc_meses['Marzo'] == 31
    assert dicc_meses['Abril'] == 30
    assert dicc_meses['Mayo'] == 31
    assert dicc_meses['Junio'] == 30
    assert dicc_meses['Julio'] == 31
    assert dicc_meses['Agosto'] == 31
    assert dicc_meses['Septiembre'] == 30
    assert dicc_meses['Octubre'] == 31
    assert dicc_meses['Noviembre'] == 30
    assert dicc_meses['Diciembre'] == 31
except AssertionError as e:
    e.args += ("Tu respuesta es incorrecta.",)
    raise e

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Una matriz en un diccionario 
# 
# Adaptado de Downey, A., Elkner, J., & Meyers, C. (2012).
# 
# Una tienda de videojuegos está analizando si una familia comprará la nueva consola de videojuegos con base en dos variables: el número de hijos (un hijo o más) y las horas que comparten los padres al día con sus hijos (una hora o más). La compañía representó sus resultados en la siguiente matriz, donde las columnas corresponden al número de hijos y las filas al número de horas diarias que los padres comparten con sus hijos:
# 
# $$\begin{matrix} 0 & 1 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 1 \end{matrix}$$
# 
# Según esta matriz, una familia en la que los padres disponen de tres horas para compartir con sus hijos y que tiene cuatro hijos comprará la consola de videojuegos. Asimismo, en una familia en la que los padres disponen de una hora para compartir con sus hijos y que tiene tres hijos no la comprará. 
# 
# *Resuelve los ejercicios 14 y 15 con base en este enunciado.*

# ### Ejercicio 14
# 
# Crea un diccionario con el nombre `matriz`, que contenga únicamente los casos en los que la familia comprará la consola. Las llaves del dicccionario deben ser tuplas que indiquen la cantidad de horas y cantidad de hijos. Además, tanto los componentes de la llave como el valor deben ser númericos. Si también representas los casos en los que la familia no comprará la consola, no obtendrás puntuación.

# In[48]:


# YOUR CODE HERE
matriz = { (1 ,2): 1, (1, 4): 1 , (1 ,5): 1, (2, 5): 1, (3, 1): 1, (3, 4): 1, (4, 1): 1, (4, 3): 1, (4, 5): 1}
matriz


# In[49]:


## PRUEBAS

# Caso 1: no existe el dicccionario.
try:
    matriz
except:
    raise NotImplementedError("No declaraste una variable llamada matriz.",)

# Caso 2: el código se ejecuta con errores
try:
    exec(_i)
except:
    raise RuntimeError("Tu código produce un error al ejecutarse.")

# Caso 3: no es un diccionario.
assert type(matriz) == dict, f"Tu variable matriz no es de tipo {dict.__name__}."

# Caso 4: el diccionario contiene valores de tipo incorrecto
for i in matriz.keys():
    assert type(i) == tuple, f"Tu diccionario contiene llaves que no son de tipo {tuple.__name__}."

for j in matriz.values():
    assert type(j) == int, f"Tu diccionario contiene valores que no son de tipo {int.__name__}."
    assert j == 1, "Tu diccionario representa casos en los que la familia no comprará la consola."

# Caso 5: el diccionario tiene el tamaño incorrecto
assert len(matriz) == 9, "Tu diccionario no tiene el tamaño correcto."
    
# Caso 6: el diccionario es correcto
assert set(matriz.keys()) == {(1,2), (1,4), (1,5), (2,5), (3,1), (3,4), (4,1), (4,3), (4,5)}, "Las llaves de tu diccionario no son correctas."

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ### Ejercicio 15
# 
# Consulta el diccionario para saber si una familia, que tiene `h` hijos y en la que los padres disponen de `t` horas diarias para compartir con ellos, comprará la consola. Debes hacer uso del diccionario `matriz` y no lo puedes modificar. Guarda el valor resultante en una variable que se llame `prediccion_familia`.
# 
# **Nota**: la variable `prediccion_familia` debe tomar el valor de 1 si la familia comprará la consola, y 0 en caso contrario.

# In[50]:


# No modifiques esta celda

h = 5
t = 2


# In[51]:


# YOUR CODE HERE
indice = (h,t)

prediccion_familia = matriz.get(indice, 0)
prediccion_familia


# In[52]:


## PRUEBAS

# Base variables
h = 4
t = 4

try:
    # Caso 1: no existe la variable.
    try:
        prediccion_familia
    except:
        raise NotImplementedError("No declaraste una variable llamada prediccion_familia.",)

    # Caso 2: el código se ejecuta con errores
    try:
        exec(_i)
    except:
        raise RuntimeError("Tu código produce un error al ejecutarse.")
    
    # Caso 3: el código modifica los parametros del problema
    try:
        assert h == 4
        assert t == 4
    except:
        raise AssertionError("Tu código no debe modificar los datos del problema.")
    
    # Caso 4: no es un int.
    assert type(prediccion_familia) == int, f"Tu variable prediccion_familia no es de tipo {int.__name__}."

    # Caso 5: el código no utiliza la variable matriz
    assert _i.find("matriz") >= 0, "Tu código no utiliza la variable matriz."
   
    # Caso 6: la respuesta es correcta
    assert prediccion_familia == 0, "Tu respuesta es incorrecta. Recuerda que debes representar con un 0 el caso en el que la familia no comprará la consola."  
    
except:
    # Restaurar variables base originales
    h = 5
    t = 2
    raise

finally:
    # Restaurar variables base originales
    h = 5
    t = 2

# Mensaje de felicitaciones
print("Felicidades, realizaste este ejercicio correctamente.")


# ## Referencias
#  
# Downey, A., Elkner, J., & Meyers, C. (2012). How To Think Like A Computer Scientist: Learning with Python. Segunda Edición. Recuperado de: https://www.openbookproject.net/thinkcs/python/english2e/index.html

# ## Créditos
# 
# __Autor(es)__: Jorge Esteban Camargo Forero, Juan Felipe Rengifo Méndez, Alejandro Mantilla Redondo, Diego Alejandro Cely Gómez
#  
# __Fecha última actualización__: 06/08/2021

# In[ ]:




