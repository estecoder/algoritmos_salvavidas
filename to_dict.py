from typing import List, Dict
#convertir una lista de listas a lista de diccionarios, cambia orden de datos
def list_to_dict(lista: list, headers: list):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        
        # llamada recursiva en cada mitad
        list_to_dict(izquierda,headers)
        list_to_dict(derecha,headers)
        
        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if type(izquierda[i])!=dict:
                lista[k] = dict(zip(headers,izquierda[i]))
                i += 1
                k += 1
            elif type(derecha[j])!=dict:
                lista[k] = dict(zip(headers,derecha[j]))
                j += 1
                k += 1
            else:
                lista[k] = izquierda[i]
                lista[k+1] = derecha[j]
                i += 1
                j += 1
                k += 2
        #Escribe restante por izquierda cuando excede el index
        while i < len(izquierda):
            if type(izquierda[i])!=dict:
                lista[k] = dict(zip(headers,izquierda[i]))
                k +=1
            else:
                lista[k] = izquierda[i]
                k +=1
            i += 1
        #Escribe restante por derecha cuando excede el index    
        while j < len(derecha):
            if type(derecha[j])!=dict:
                lista[k] = dict(zip(headers,derecha[j]))
                k += 1
            else:
                lista[k] = derecha[j]
                k += 1
            j += 1
        
        return lista

def find_keys(in_dict: dict, val: int):
    keys = list(in_dict.keys())
    values = list(in_dict.values())
    return keys[values.index(val)]

#IMPLEMENTAR ESTO CON RECURSIVIDAD
def limpiar_acentos(text: List[str]):
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for palabra in text:
        for acen in acentos:
            if acen in palabra:
                i = text.index(palabra)
                palabra = palabra.replace(acen, acentos[acen])
                text[i]=palabra
    return text


