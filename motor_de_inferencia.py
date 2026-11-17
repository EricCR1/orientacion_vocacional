UMBRAL = 70

hechos = {

    "i_realista":      {"tipo": "interes", "nombre": "Realista",      "valor": None, "cumple": None},
    "i_investigativo": {"tipo": "interes", "nombre": "Investigativo", "valor": None, "cumple": None},
    "i_artistico":     {"tipo": "interes", "nombre": "Artístico",     "valor": None, "cumple": None},
    "i_social":        {"tipo": "interes", "nombre": "Social",        "valor": None, "cumple": None},
    "i_emprendedor":   {"tipo": "interes", "nombre": "Emprendedor",   "valor": None, "cumple": None},
    "i_convencional":  {"tipo": "interes", "nombre": "Convencional",  "valor": None, "cumple": None},


    "a_razonamiento_verbal":     {"tipo": "aptitud", "nombre": "Razonamiento verbal",     "valor": None, "cumple": None},
    "a_razonamiento_abstracto":  {"tipo": "aptitud", "nombre": "Razonamiento abstracto",  "valor": None, "cumple": None},
    "a_mecanica":                {"tipo": "aptitud", "nombre": "Mecánica",                "valor": None, "cumple": None},
    "a_memoria":                 {"tipo": "aptitud", "nombre": "Memoria",                 "valor": None, "cumple": None},
    "a_aptitud_interpersonal":   {"tipo": "aptitud", "nombre": "Aptitud interpersonal",   "valor": None, "cumple": None},
    "a_destreza_manual":         {"tipo": "aptitud", "nombre": "Destreza manual",         "valor": None, "cumple": None},
    "a_razonamiento_numerico":   {"tipo": "aptitud", "nombre": "Razonamiento numérico",   "valor": None, "cumple": None},
    "a_aptitud_espacial":        {"tipo": "aptitud", "nombre": "Aptitud espacial",        "valor": None, "cumple": None},
    "a_creatividad":             {"tipo": "aptitud", "nombre": "Creatividad",             "valor": None, "cumple": None},
    "a_pensamiento_computacional": {"tipo": "aptitud", "nombre": "Pensamiento computacional", "valor": None, "cumple": None},
}



def evaluar(clave):
    hecho = hechos[clave]
    valor = hecho ["valor"]
    if valor is None: 
        return None
    hecho["cumple"] = valor >= UMBRAL
    return hecho ["cumple"]



hechos["i_realista"]["valor"] = 85       # imprimirá True
print("Interés Realista cumple:", evaluar("i_realista"))

hechos["a_razonamiento_verbal"]["valor"] = 50        # imprimirá False
print("Aptitud Razonamiento abstracto cumple:", evaluar("a_razonamiento_verbal"))