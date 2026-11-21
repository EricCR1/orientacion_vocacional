import random

hechos_intereses = {
    'i_realista_1': random.randint(0, 5),
    'i_realista_2': random.randint(0, 5),
    'i_realista_3': random.randint(0, 5),
    'i_realista_4': random.randint(0, 5),
    'i_realista_5': random.randint(0, 5),
    'i_investigativo_1': random.randint(0, 5),
    'i_investigativo_2': random.randint(0, 5),
    'i_investigativo_3': random.randint(0, 5),
    'i_investigativo_4': random.randint(0, 5),
    'i_investigativo_5': random.randint(0, 5),
    'i_artistico_1': random.randint(0, 5),
    'i_artistico_2': random.randint(0, 5),
    'i_artistico_3': random.randint(0, 5),
    'i_artistico_4': random.randint(0, 5),
    'i_artistico_5': random.randint(0, 5),
    'i_social_1': random.randint(0, 5),
    'i_social_2': random.randint(0, 5),
    'i_social_3': random.randint(0, 5),
    'i_social_4': random.randint(0, 5),
    'i_social_5': random.randint(0, 5),
    'i_emprendedor_1': random.randint(0, 5),
    'i_emprendedor_2': random.randint(0, 5),
    'i_emprendedor_3': random.randint(0, 5),
    'i_emprendedor_4': random.randint(0, 5),
    'i_emprendedor_5': random.randint(0, 5),
    'i_convencional_1': random.randint(0, 5),
    'i_convencional_2': random.randint(0, 5),
    'i_convencional_3': random.randint(0, 5),
    'i_convencional_4': random.randint(0, 5),
    'i_convencional_5': random.randint(0, 5)
}   

hechos_aptitudes = {
    'a_razonamiento_verbal_1': random.randint(0, 5),
    'a_razonamiento_verbal_2': random.randint(0, 5),
    'a_razonamiento_verbal_3': random.randint(0, 5),
    'a_razonamiento_abstracto_1': random.randint(0, 5),
    'a_razonamiento_abstracto_2': random.randint(0, 5),
    'a_razonamiento_abstracto_3': random.randint(0, 5),
    'a_mecananica_1': random.randint(0, 5),
    'a_mecananica_2': random.randint(0, 5),
    'a_mecananica_3': random.randint(0, 5),
    'a_memoria_1': random.randint(0, 5),
    'a_memoria_2': random.randint(0, 5),
    'a_memoria_3': random.randint(0, 5),
    'a_aptitud_interpersonal_1': random.randint(0, 5),
    'a_aptitud_interpersonal_2': random.randint(0, 5),
    'a_aptitud_interpersonal_3': random.randint(0, 5),
    'a_destreza_manual_1': random.randint(0, 5),
    'a_destreza_manual_2': random.randint(0, 5),
    'a_destreza_manual_3': random.randint(0, 5),
    'a_razonamiento_numerico_1': random.randint(0, 5),
    'a_razonamiento_numerico_2': random.randint(0, 5),
    'a_razonamiento_numerico_3': random.randint(0, 5),
    'a_aptitud_espacial_1': random.randint(0, 5),
    'a_aptitud_espacial_2': random.randint(0, 5),
    'a_aptitud_espacial_3': random.randint(0, 5),
    'a_creatividad_1': random.randint(0, 5),
    'a_creatividad_2': random.randint(0, 5),
    'a_creatividad_3': random.randint(0, 5),
    ' a_pensamiento_computacional_1': random.randint(0, 5),
    ' a_pensamiento_computacional_2': random.randint(0, 5),
    ' a_pensamiento_computacional_3': random.randint(0, 5),
}

puntajes_intereses = {
    'i_realista': 
sum([hechos_intereses[f'i_realista_{i}'] for i in range(1, 6)])/5,
    'i_investigativo': 
sum([hechos_intereses[f'i_investigativo_{i}'] for i in range(1, 6)])/5,
    'i_artistico': 
sum([hechos_intereses[f'i_artistico_{i}'] for i in range(1, 6)])/5,
    'i_social': 
sum([hechos_intereses[f'i_social_{i}'] for i in range(1, 6)])/5,
    'i_emprendedor': 
sum([hechos_intereses[f'i_emprendedor_{i}'] for i in range(1, 6)])/5,
    'i_convencional': 
sum([hechos_intereses[f'i_convencional_{i}'] for i in range(1, 6)])/5,
}

puntajes_aptitudes = {
    'a_razonamiento_verbal':
sum([hechos_aptitudes[f'a_razonamiento_verbal_{i}'] for i in range(1, 4)])/3,
'a_razonamiento_abstracto':
sum([hechos_aptitudes[f'a_razonamiento_abstracto_{i}'] for i in range(1, 4)])/3,
    'a_mecananica':
sum([hechos_aptitudes[f'a_mecananica_{i}'] for i in range(1, 4)])/3,    
    'a_memoria': 
sum([hechos_aptitudes[f'a_memoria_{i}'] for i in range(1, 4)])/3,
    'a_aptitud_interpersonal':
sum([hechos_aptitudes[f'a_aptitud_interpersonal_{i}'] for i in range(1, 4)])/3,
    'a_destreza_manual':
sum([hechos_aptitudes[f'a_destreza_manual_{i}'] for i in range(1, 4)])/3,
    'a_razonamiento_numerico':
sum([hechos_aptitudes[f'a_razonamiento_numerico_{i}'] for i in range(1, 4)])/3,
    'a_aptitud_espacial':
sum([hechos_aptitudes[f'a_aptitud_espacial_{i}'] for i in range(1, 4)])/3,
    'a_creatividad': 
sum([hechos_aptitudes[f'a_creatividad_{i}'] for i in range(1, 4)])/3,

}

# print("puntajes de Intereses:")
# for interes, valor in puntajes_intereses.items():
#     print(f"{interes}: {valor}")


top_intereses = dict(sorted(puntajes_intereses.items(), key=lambda item: item[1], reverse=True)) #esta línea ordena el diccionario de puntajes de intereses de mayor a menor y lo guarda en la variable top_intereses

(interes_mayor, valor_1), (interes_segundo, valor_2), (interes_tercero, valor_3) = list(top_intereses.items())[:3]


print("Los tres intereses más altos son:")
print(f"1. {interes_mayor}")
print(f"2. {interes_segundo}")
print(f"3. {interes_tercero}")