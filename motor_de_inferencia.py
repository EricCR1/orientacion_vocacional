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
    'i_artistico_1': random.randint(0  , 5),
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
    'a_mecanica_1': random.randint(0, 5),
    'a_mecanica_2': random.randint(0, 5),
    'a_mecanica_3': random.randint(0, 5),
    'a_memoria_1': random.randint(0, 5),
    'a_memoria_2': random.randint(0, 5),
    'a_memoria_3': random.randint(0, 5),
    'a_interpersonal_1': random.randint(0, 5),
    'a_interpersonal_2': random.randint(0, 5),
    'a_interpersonal_3': random.randint(0, 5),
    'a_destreza_manual_1': random.randint(0, 5),
    'a_destreza_manual_2': random.randint(0, 5),
    'a_destreza_manual_3': random.randint(0, 5),
    'a_razonamiento_numerico_1': random.randint(0, 5),
    'a_razonamiento_numerico_2': random.randint(0, 5),
    'a_razonamiento_numerico_3': random.randint(0, 5),
    'a_espacial_1': random.randint(0, 5),
    'a_espacial_2': random.randint(0, 5),
    'a_espacial_3': random.randint(0, 5),
    'a_creatividad_1': random.randint(0, 5),
    'a_creatividad_2': random.randint(0, 5),
    'a_creatividad_3': random.randint(0, 5),
    'a_pensamiento_computacional_1': random.randint(0, 5),
    'a_pensamiento_computacional_2': random.randint(0, 5),
    'a_pensamiento_computacional_3': random.randint(0, 5),
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

# print("puntajes de Intereses:")
# for interes, valor in puntajes_intereses.items():
#     print(f"{interes}: {valor}")

puntajes_aptitudes = {
    'a_razonamiento_verbal':
min (1, ((sum([hechos_aptitudes[f'a_razonamiento_verbal_{i}'] for i in range(1, 4)])/3) - 1)/3),
'a_razonamiento_abstracto':
min (1, ((sum([hechos_aptitudes[f'a_razonamiento_abstracto_{i}'] for i in range(1, 4)])/3) - 1)/3),
    'a_mecanica':
min (1, ((sum([hechos_aptitudes[f'a_mecanica_{i}'] for i in range(1, 4)])/3) - 1)/3),    
    'a_memoria': 
min (1, ((sum([hechos_aptitudes[f'a_memoria_{i}'] for i in range(1, 4)])/3) - 1)/3),
    'a_interpersonal':
min (1, ((sum([hechos_aptitudes[f'a_interpersonal_{i}'] for i in range(1, 4)])/3) - 1)/3),
    'a_destreza_manual':
min (1, ((sum([hechos_aptitudes[f'a_destreza_manual_{i}'] for i in range(1, 4)])/3) - 1)/3),
    'a_razonamiento_numerico':
min (1, ((sum([hechos_aptitudes[f'a_razonamiento_numerico_{i}'] for i in range(1, 4)])/3) - 1)/3),
    'a_espacial':
min (1, ((sum([hechos_aptitudes[f'a_espacial_{i}'] for i in range(1, 4)])/3) - 1)/3),
    'a_creatividad': 
min (1, ((sum([hechos_aptitudes[f'a_creatividad_{i}'] for i in range(1, 4)])/3) - 1)/3),
    'a_pensamiento_computacional':
min (1, ((sum([hechos_aptitudes[f'a_pensamiento_computacional_{i}'] for i in range(1, 4)])/3) - 1)/3),
}

top_intereses = dict(sorted(puntajes_intereses.items(), key=lambda item: item[1], reverse=True)) #esta línea ordena el diccionario de puntajes de intereses de mayor a menor y lo guarda en la variable top_intereses

(interes_primero, valor_1), (interes_segundo, valor_2), (interes_tercero, valor_3) = list(top_intereses.items())[:3]# esta línea guarda los tres intereses mas altos y los guarda en variables separadas


# print("Los tres intereses más altos son:")
# print(f"1. {interes_primero} con un puntaje de {valor_1}")
# print(f"2. {interes_segundo} con un puntaje de {valor_2}")
# print(f"3. {interes_tercero} con un puntaje de {valor_3}")

interes_fisico_matematico = 0
interes_quimico_biologico = 0
interes_economico_administrativo = 0
interes_humanidades= 0


match interes_primero:
    case 'i_realista':
        interes_fisico_matematico = interes_fisico_matematico + 6
        interes_quimico_biologico = interes_quimico_biologico + 6
        interes_economico_administrativo = interes_economico_administrativo + 3
        interes_humanidades = interes_humanidades + 0

    case 'i_investigativo':
        interes_fisico_matematico = interes_fisico_matematico + 9
        interes_quimico_biologico = interes_quimico_biologico + 9
        interes_economico_administrativo = interes_economico_administrativo + 0
        interes_humanidades = interes_humanidades + 3
    case 'i_artistico':
        interes_fisico_matematico = interes_fisico_matematico + 6
        interes_quimico_biologico = interes_quimico_biologico + 6
        interes_economico_administrativo = interes_economico_administrativo + 3
        interes_humanidades = interes_humanidades + 6
    case 'i_social':
        interes_fisico_matematico = interes_fisico_matematico + 3
        interes_quimico_biologico = interes_quimico_biologico + 3
        interes_economico_administrativo = interes_economico_administrativo + 6
        interes_humanidades = interes_humanidades + 9
    case 'i_emprendedor':
        interes_fisico_matematico =  interes_fisico_matematico + 0
        interes_quimico_biologico =  interes_quimico_biologico + 0
        interes_economico_administrativo =  interes_economico_administrativo + 9
        interes_humanidades =  interes_humanidades + 6
    case 'i_convencional':
        interes_fisico_matematico =  interes_fisico_matematico + 3
        interes_quimico_biologico =  interes_quimico_biologico + 3
        interes_economico_administrativo =  interes_economico_administrativo + 6
        interes_humanidades =  interes_humanidades + 3

match interes_segundo:
    case 'i_realista':
        interes_fisico_matematico = interes_fisico_matematico + 6
        interes_quimico_biologico = interes_quimico_biologico + 0
        interes_economico_administrativo = interes_economico_administrativo + 4
        interes_humanidades = interes_humanidades + 2

    case 'i_investigativo':
        interes_fisico_matematico = interes_fisico_matematico + 4
        interes_quimico_biologico = interes_quimico_biologico + 2
        interes_economico_administrativo = interes_economico_administrativo + 2
        interes_humanidades = interes_humanidades + 4
    case 'i_artistico':
        interes_fisico_matematico = interes_fisico_matematico + 2
        interes_quimico_biologico = interes_quimico_biologico + 4
        interes_economico_administrativo = interes_economico_administrativo + 0
        interes_humanidades = interes_humanidades + 6
    case 'i_social':
        interes_fisico_matematico = interes_fisico_matematico + 0
        interes_quimico_biologico = interes_quimico_biologico + 6
        interes_economico_administrativo = interes_economico_administrativo + 2
        interes_humanidades = interes_humanidades + 4
    case 'i_emprendedor':
        interes_fisico_matematico =  interes_fisico_matematico + 2
        interes_quimico_biologico =  interes_quimico_biologico + 4
        interes_economico_administrativo =  interes_economico_administrativo + 4
        interes_humanidades =  interes_humanidades + 2
    case 'i_convencional':
        interes_fisico_matematico =  interes_fisico_matematico + 4
        interes_quimico_biologico =  interes_quimico_biologico + 2
        interes_economico_administrativo =  interes_economico_administrativo + 6
        interes_humanidades =  interes_humanidades + 0

match interes_tercero:
    case 'i_realista':
        interes_fisico_matematico = interes_fisico_matematico + 2
        interes_quimico_biologico = interes_quimico_biologico + 3
        interes_economico_administrativo = interes_economico_administrativo + 2
        interes_humanidades = interes_humanidades + 2

    case 'i_investigativo':
        interes_fisico_matematico = interes_fisico_matematico + 1
        interes_quimico_biologico = interes_quimico_biologico + 2
        interes_economico_administrativo = interes_economico_administrativo + 3
        interes_humanidades = interes_humanidades + 3
    case 'i_artistico':
        interes_fisico_matematico = interes_fisico_matematico + 0
        interes_quimico_biologico = interes_quimico_biologico + 1
        interes_economico_administrativo = interes_economico_administrativo + 2
        interes_humanidades = interes_humanidades + 2
    case 'i_social':
        interes_fisico_matematico = interes_fisico_matematico + 1
        interes_quimico_biologico = interes_quimico_biologico + 0
        interes_economico_administrativo = interes_economico_administrativo + 3
        interes_humanidades = interes_humanidades + 1
    case 'i_emprendedor':
        interes_fisico_matematico =  interes_fisico_matematico + 2
        interes_quimico_biologico =  interes_quimico_biologico + 1
        interes_economico_administrativo =  interes_economico_administrativo + 2
        interes_humanidades =  interes_humanidades + 0
    case 'i_convencional':
        interes_fisico_matematico =  interes_fisico_matematico + 3
        interes_quimico_biologico =  interes_quimico_biologico + 2
        interes_economico_administrativo =  interes_economico_administrativo + 1
        interes_humanidades =  interes_humanidades + 1

# print("Resultados de la ponderación de intereses:")
# print(f"Resultado Físico-Matemático: {interes_fisico_matematico/18}")
# print(f"Resultado Químico-Biológico: {interes_quimico_biologico/18}")
# print(f"Resultado Económico-Administrativo: {interes_economico_administrativo/18}")
# print(f"Resultado Humanidades: {interes_humanidades/18}")

aptitudes_fuertes_fisico_matematico = puntajes_aptitudes['a_razonamiento_numerico']+ puntajes_aptitudes['a_razonamiento_abstracto'] + puntajes_aptitudes['a_pensamiento_computacional'] + puntajes_aptitudes['a_espacial']
# print ("Aptitudes fuertes Físico-Matemático:", aptitudes_fuertes_fisico_matematico)

aptitud_fisico_matematico = ((aptitudes_fuertes_fisico_matematico)+(0.5 * (puntajes_aptitudes['a_mecanica']  + puntajes_aptitudes['a_destreza_manual'] )))/5
# print ("Aptitud Físico-Matemático:", aptitud_fisico_matematico)

aptitud_quimico_biologico = (((puntajes_aptitudes['a_razonamiento_verbal'] + puntajes_aptitudes['a_razonamiento_numerico'] + puntajes_aptitudes['a_memoria'] + puntajes_aptitudes['a_razonamiento_abstracto'] ))+(0.5 * (puntajes_aptitudes['a_interpersonal']  + puntajes_aptitudes['a_destreza_manual'] )))/5

aptitud_economico_administrativo = (((puntajes_aptitudes['a_razonamiento_numerico'] )+ (puntajes_aptitudes['a_interpersonal'] ))+(0.5 * (puntajes_aptitudes['a_razonamiento_verbal']  + puntajes_aptitudes['a_memoria'] )))/3

aptitud_humanidades= (((puntajes_aptitudes['a_razonamiento_verbal'] + puntajes_aptitudes['a_creatividad'] + puntajes_aptitudes['a_interpersonal'] + puntajes_aptitudes['a_memoria'] ))+(0.5 * (puntajes_aptitudes['a_espacial']  + puntajes_aptitudes['a_destreza_manual'] )))/5

# print("Resultados de la ponderación de aptitudes:")
# print(f"Aptitud Físico-Matemático: {aptitud_fisico_matematico}")
# print(f"Aptitud Químico-Biológico: {aptitud_quimico_biologico}")
# print(f"Aptitud Económico-Administrativo: {aptitud_economico_administrativo}")
# print(f"Aptitud Humanidades: {aptitud_humanidades}")


resultado_final_fisico_matematico = 100 * (0.6 * interes_fisico_matematico/18 + 0.4 * aptitud_fisico_matematico)
print(f"Resultado final Físico-Matemático: {resultado_final_fisico_matematico} %")

resultado_final_quimico_biologico = 100 * (0.6 * interes_quimico_biologico/18 + 0.4 * aptitud_quimico_biologico)
print(f"Resultado final Químico-Biológico: {resultado_final_quimico_biologico} %")

resultado_final_economico_administrativo = 100 * (0.6 * interes_economico_administrativo/18 + 0.4 * aptitud_economico_administrativo)
print(f"Resultado final Económico-Administrativo: {resultado_final_economico_administrativo} %")

resultado_final_humanidades = 100 * (0.6 * interes_humanidades/18 + 0.4 * aptitud_humanidades)
print(f"Resultado final Humanidades: {resultado_final_humanidades} %")