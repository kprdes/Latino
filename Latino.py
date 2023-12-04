import streamlit as st
import pandas as pd

def main():
    st.title("Encuesta Corporación Latinoamericana de Estudios")

    # Crear diccionario para almacenar respuestas
    respuestas = {
        "Nombre": "", "Edad": 0, "Genero": "", "Ciudad": "",
        "Estado Civil": "", "Hijos": 0, "NoHijos" : "", "Ocupacion": "",
        "Sector Trabajo": "", "Cargo": "", "Tiempo Trabajo": 0,
        "Responsabilidades": "", "Ingresos": 0, "Nivel Estudios": "",
        "Programa Estudio": "", "Razon Eleccion": "",
        "Habilidades": "", "Formacion Interes": "",
        "Motivacion Salud": "", "Criterios Eleccion": "",
        "Medios Informacion": ""
    }

    programas = ['', 'Enfermería', 'Servicios Farmacéuticos', 'Veterinaria', 'Administrativo en Salud', 'Preescolar', 'Técnico en Avalúos']
    edades_hijos = ['', '0 a 3', '4 a 6', ' 6 a 10', 'Adolecente', 'Adulto']
    sectores = ['Educación', 'Industrial', 'Transporte']
    Horarios = ['Diurno', 'Nocturno', 'Fines de Semana']
    Nivel_Ingresos = ['','0 a $500.000', '$500.000 a $1.000.000', '$1.000.000 a $1.500.000', '$1.500.000 a $2.000.000', 'Más de $2.000.000']
    Motivo_De_Eleccion = ['', 'Por recomendacion', '']

    # Sección 2.1: Datos personales
    st.header("2.1. Datos personales")
    respuestas["Nombre"] = st.text_input("1. ¿Cuál es tu nombre?")
    respuestas["Edad"] = st.number_input("2. ¿Qué edad tienes?", min_value=0)
    respuestas["Genero"] = st.radio("3. ¿Cuál es tu género?", ("Masculino", "Femenino", "Otro"))
    respuestas["Ciudad"] = st.text_input("4. ¿En qué ciudad vives?")
    respuestas["Estado Civil"] = st.selectbox("5. ¿Cuál es tu estado civil?", ("Soltero", "Casado", "Divorciado", "Viudo"))
    Hijos = st.radio("6. ¿Tienes hijos?", ('No', 'Si'))
    if Hijos == 'Si':
        respuestas["Hijos"] = st.number_input("6. 1¿cuántos hijos tiene?", min_value=0)
        respuestas["NoHijos"] = st.selectbox("6. 2 Cuantos años tienen", edades_hijos)


    # Sección 2.2: Datos laborales
    st.header("2.2. Datos laborales")
    respuestas["Ocupacion"] = st.selectbox("7. ¿A qué te dedicas?", ('', 'Trabajo', 'Estudio', 'Trabajo y Estudio', 'Otro'))
    if respuestas["Ocupacion"] == 'Trabajo' or respuestas["Ocupacion"] == 'Trabajo y Estudio':
        respuestas["Sector Trabajo"] = st.selectbox("8. ¿En qué sector trabajas?", sectores)
        respuestas["Cargo"] = st.text_input("9. ¿Qué cargo ocupas?")
        respuestas["Tiempo Trabajo"] = st.number_input("10. ¿Cuánto tiempo llevas trabajando en tu actual empleo?", min_value=0)
        respuestas["Responsabilidades"] = st.selectbox("11. ¿Cuál es tu horario?", Horarios)
        respuestas["Ingresos"] = st.selectbox("12. ¿Qué nivel de ingresos tienes?", Nivel_Ingresos)

    # Sección 2.3: Datos educativos
    st.header("2.3. Datos educativos")
    respuestas["Nivel Estudios"] = st.text_input("13. ¿En qué colegio terminaste tus estudios?")
    respuestas["Programa Estudio"] = st.selectbox("14. ¿Qué programa estás estudiando?", programas)
    respuestas["Razon Eleccion"] = st.text_area("15. ¿Por qué elegiste ese programa?")
    respuestas["Habilidades"] = st.text_area("16. ¿Qué habilidades o competencias te gustaría desarrollar o mejorar en el programa que estas estudiando?")
    respuestas["Formacion Interes"] = st.radio("17. ¿Te gustaría que el programa técnico tuviera una especialización?", ('No', 'Si'))
    if respuestas["Formacion Interes"] == 'Si':
        respuestas["Formacion Interes"] =  st.text_input("17.1 ¿En qué te gustaría especializarte?")

    # Sección 2.4: Datos de consumo
    st.header("2.4. Datos de consumo")
    respuestas["Motivacion Salud"] = st.text_area("18. ¿Qué te motiva o te lleva a buscar una formación o capacitación en el sector salud?")
    respuestas["Criterios Eleccion"] = st.text_area("19. ¿Qué factores o criterios tienes en cuenta a la hora de elegir una institución educativa?")
    respuestas["Medios Informacion"] = st.text_area("20. ¿Qué medios o canales usas para informarte sobre las opciones de formación o capacitación disponibles?")

    # Botón para guardar en CSV
    if st.button("Guardar respuestas"):
        guardar_respuestas(respuestas)

def guardar_respuestas(respuestas):
    # Intentar cargar el archivo CSV existente si existe
    try:
        df_existente = pd.read_csv("respuestas_encuesta.csv")
    except FileNotFoundError:
        # Si el archivo no existe, crear un DataFrame vacío
        df_existente = pd.DataFrame()

    # Crear DataFrame a partir del diccionario de respuestas
    df_nuevo = pd.DataFrame(respuestas, index=[0])

    # Concatenar el DataFrame existente con el nuevo
    df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)

    # Guardar el DataFrame combinado en el archivo CSV
    df_final.to_csv("respuestas_encuesta.csv", index=False)
    st.success("¡Respuestas guardadas!")

main()
