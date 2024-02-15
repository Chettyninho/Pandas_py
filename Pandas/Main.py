import pandas as pd
from datetime import datetime

#Llenar los Arrays recorriendo el json
response = [
    {
        "salary": "$3,946.45",
        "age": 23,
        "name": "Bird Ramsey",
        "gender": "male",
        "proyect": "NIMON",
        "email": "birdramsey@nimon.com"
    },
    {
        "salary": "$2,499.49",
        "age": 31,
        "name": "Jonathan Martinez",
        "gender": "male",
        "proyect": "LUXURIA",
        "email": "jonatanmart@luxuria.com"
    },
    {
        "salary": "$2,820.18",
        "age": 34,
        "name": "Kristie Cole",
        "gender": "female",
        "proyect": "QUADEEBO",
        "email": "kristiecole@quadeebo.com"
    },
    {
        "salary": "$3,277.32",
        "age": 30,
        "name": "Leonor Cross",
        "gender": "female",
        "proyect": "GRONK",
        "email": "leonorcross@gronk.com"
    },
    {
        "salary": "$1,972.47",
        "age": 28,
        "name": "Marsh Mccall",
        "gender": "male",
        "proyect": "ULTRIMAX",
        "email": "marshmccall@ultrimax.com"
    },
    {
        "salary": "$3,124.45",
        "age": 25,
        "name": "Carlitos Jonas",
        "gender": "male",
        "proyect": "NIMON",
        "email": "carlitosjonas@nimon.com"
    },
    {
        "salary": "$1,499.49",
        "age": 34,
        "name": "Bordell Carlman",
        "gender": "female",
        "proyect": "LUXURIA",
        "email": "lillianburgess@luxuria.com"
    },
    {
        "salary": "$2,420.18",
        "age": 34,
        "name": "Cristina Cole",
        "gender": "female",
        "proyect": "QUADEEBO",
        "email": "criscol@quadeebo.com"
    },
    {
        "salary": "$4,277.32",
        "age": 30,
        "name": "Leonora Ruseleve",
        "gender": "female",
        "proyect": "GRONK",
        "email": "leonorarus@gronk.com"
    },
    {
        "salary": "$2,972.47",
        "age": 28,
        "name": "Martiño Rivas",
        "gender": "male",
        "proyect": "ULTRIMAX",
        "email": "marriv@ultrimax.com"
    }
]
#Referenciamos la entrada de cada campo
nombres = [entry["name"] for entry in response]
edades = [entry["age"] for entry in response]
salarios = [entry["salary"] for entry in response]
proyectos = [entry["proyect"] for entry in response]
#relacionar la data
df = pd.DataFrame({'Nombre':nombres,'Edad':edades,'Salario':salarios,'Proyecto':proyectos})
#filtrar los mayores de 30 y de gronk
df = df[(df['Edad'] < 30) & (df['Proyecto'] != 'GRONK')]

# Aplicar el aumento del 10% a los salarios
df['Salario'] = df['Salario'].replace('[\$,]', '', regex=True).astype(float)
df['Salario'] *= 1.1

# Cambiar el símbolo de dólar por euro
df['Salario'] = '€' + df['Salario'].astype(str)

# Obtener el mes y año actual
now = datetime.now()
mes_anio = now.strftime("%m-%Y")

# Crear el archivo Excel
nombre_excel = f"NominasExtra-{mes_anio}.xlsx"
df.to_excel(nombre_excel, index=False)

print(f"Archivo Excel '{nombre_excel}' creado exitosamente.")