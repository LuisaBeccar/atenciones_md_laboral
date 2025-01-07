import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import spacy 

# Cargar el modelo de spacy para español
#sp = spacy.load('es_core_news_sm')

# Configurar el vectorizador con stopwords en español
from spacy.lang.es import stop_words as es_stop_words
counter1 = CountVectorizer(stop_words=list(es_stop_words.STOP_WORDS))
counter2 = CountVectorizer(ngram_range=(2, 2))  # para bigramas

# Función que analiza las atenciones
def contar_atenciones(periodos):
    nombre = []
    virt = []
    pres = []

    for key, periodo in periodos.items():
        if periodo == "":
            continue
        p = 100  # Number of words per row
        words = periodo.split()
        rows = []
        for i in range(0, len(words), p):
            rows.append(' '.join(words[i:i + p]))
        X = pd.Series(rows)

        # Tokenizar individualmente
        X_t1 = counter1.fit_transform(X)
        data1 = pd.DataFrame(X_t1.toarray().sum(axis=0),
                             index=counter1.get_feature_names_out(),
                             columns=['freq'])

        # Para contar binomios
        X_t2 = counter2.fit_transform(X)
        data2 = pd.DataFrame(X_t2.toarray().sum(axis=0),
                             index=counter2.get_feature_names_out(),
                             columns=['freq']).sort_values('freq', ascending=False)

        # Contar atenciones virtuales
        virtuales = (data2.query('index == "recibo certificado"').sum().iloc[0] +
                       data2.query('index == "recibo certificados"').sum().iloc[0] +
                       data2.query('index == "recibo certif"').sum().iloc[0] +
                       data2.query('index == "recibo email"').sum().iloc[0] +
                       data2.query('index == "recibo mail"').sum().iloc[0] +
                       data2.query('index == "se recibe"').sum().iloc[0] +
                       data2.query('index == "recibo aviso"').sum().iloc[0] +
                       data2.query('index == "sector avisa"').sum().iloc[0] +
                       data2.query('index == "envia certif"').sum().iloc[0] +
                       data2.query('index == "envia certificado"').sum().iloc[0] +
                       data2.query('index == "envia certificados"').sum().iloc[0] +
                       data2.query('index == "envia constancia"').sum().iloc[0]+
                       data2.query('index == "envia mail"').sum().iloc[0]+
                       data2.query('index == "envia email"').sum().iloc[0]+
                       data2.query('index == "se comunica"').sum().iloc[0] +
                       data2.query('index == "sector informa"').sum().iloc[0]  +
                       data2.query('index == "me comunico"').sum().iloc[0] +
                       data2.query('index == "se comunica"').sum().iloc[0] +
                       data1.query('index == "llamo"').sum().iloc[0] +
                       data1.query('index == "llama"').sum().iloc[0] +
                       data2.query('index == "intento comunicarme"').sum().iloc[0]
                       )
        
        # Contar atenciones presenciales
        presenciales = (data1.query('index == "concurre"').sum().iloc[0] +
                        data1.query('index == "concurrio"').sum().iloc[0] +
                        data1.query('index == "acude"').sum().iloc[0] +
                        data1.query('index == "acudió"').sum().iloc[0] +
                        data2.query('index == "se presenta"').sum().iloc[0]+
                        data2.query('index == "se presentó"').sum().iloc[0]+
                        data1.query('index == "aporta"').sum().iloc[0])

        # Guardar resultados
        virt.append(virtuales)
        pres.append(presenciales)
        nombre.append(key)

    # Crear DataFrame con resultados
    tabla0 = pd.DataFrame({"nombre": nombre, "virtuales": virt, "presenciales": pres})
    return tabla0


# Función para analizar atenciones prolongadas
def contar_atenciones_prolongadas(prolongados):
    nombre2 = []
    virt2 = []
    pres2 = []

    for key, prolongado in prolongados.items():
        if prolongado == "":
            continue
        p = 100  # Number of words per row
        words = prolongado.split()
        rows = []
        for i in range(0, len(words), p):
            rows.append(' '.join(words[i:i + p]))
        X = pd.Series(rows)

        # Tokenizar individualmente
        X_t1 = counter1.fit_transform(X)
        data1 = pd.DataFrame(X_t1.toarray().sum(axis=0),
                             index=counter1.get_feature_names_out(),
                             columns=['freq'])

        # Para contar binomios
        X_t2 = counter2.fit_transform(X)
        data2 = pd.DataFrame(X_t2.toarray().sum(axis=0),
                             index=counter2.get_feature_names_out(),
                             columns=['freq']).sort_values('freq', ascending=False)

        # Contar atenciones virtuales
        virtuales2 = (data2.query('index == "recibo certificado"').sum().iloc[0] +
               data2.query('index == "recibo certificados"').sum().iloc[0] +
               data2.query('index == "recibo certif"').sum().iloc[0] +
               data2.query('index == "recibo email"').sum().iloc[0] +
               data2.query('index == "recibo mail"').sum().iloc[0] +
               data2.query('index == "se recibe"').sum().iloc[0] +
               data2.query('index == "recibo aviso"').sum().iloc[0] +
               data2.query('index == "sector avisa"').sum().iloc[0] +
               data2.query('index == "envia certif"').sum().iloc[0] +
               data2.query('index == "envia certificado"').sum().iloc[0] +
               data2.query('index == "envia certificados"').sum().iloc[0] +
               data2.query('index == "envia constancia"').sum().iloc[0]+
               data2.query('index == "envia mail"').sum().iloc[0]+
               data2.query('index == "envia email"').sum().iloc[0]+
               data2.query('index == "se comunica"').sum().iloc[0] +
               data2.query('index == "sector informa"').sum().iloc[0]  +
               data2.query('index == "me comunico"').sum().iloc[0] +
               data2.query('index == "se comunica"').sum().iloc[0] +
               data1.query('index == "llamo"').sum().iloc[0] +
               data1.query('index == "llama"').sum().iloc[0] +
               data2.query('index == "intento comunicarme"').sum().iloc[0]
              )
        # Contar atenciones presenciales
        presenciales2 = (data1.query('index == "concurre"').sum().iloc[0] +
                  data1.query('index == "concurrio"').sum().iloc[0] +
                  data1.query('index == "acude"').sum().iloc[0] +
                  data1.query('index == "acudió"').sum().iloc[0] +
                  data2.query('index == "se presenta"').sum().iloc[0]+
                  data2.query('index == "se presentó"').sum().iloc[0]+
                  data1.query('index == "aporta"').sum().iloc[0])

        # Guardar resultados
        virt2.append(virtuales2)
        pres2.append(presenciales2)
        nombre2.append(key)

    # Crear DataFrame con resultados
    tabla02 = pd.DataFrame({"nombre": nombre2, "virtuales": virt2, "presenciales": pres2})
    return tabla02


# Interfaz de Streamlit
#st.title("Análisis de Atenciones de Medicina Ocupacional - Vision Medica en Sanatorio Finochietto")

# Título principal
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Atenciones de Medicina Ocupacional</h1>
        <h3 style="font-size: 26px;">Vision Medica en Sanatorio Finochietto</h3>
        <h3 style="font-size: 26px;"> __________</h3>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("""
    Este informe presenta un análisis detallado de las atenciones realizadas en el departamento de medicina ocupacional 
    del Sanatorio Finochietto. Se quiere saber cuántas intervenciones por medio virtual (mail y llamadas) y presenciales 
    se han realizado en cada período.

    Para usar la app, copiar la columna de observaciones de la planilla y pegarla en la celda del período de tiempo correspondiente. 
    Luego pulsar Ctrl+Enter. (En caso de que no se encuentre el período a evaluar, comunicarse con el soporte: Dra Beccar Varela.)

    Al terminar de cargar los períodos que se desean evaluar, presionar el botón "Calcular Atenciones". 
    Debajo se mostrará una tabla y un gráfico con las atenciones por período. 
    En las atenciones prolongadas se utiliza solo una celda para todas las atenciones sin separar por períodos.
""")
    
# Atenciones Mensuales
st.header("Atenciones Mensuales")

# Inputs para observaciones mensuales
periodos = {}
for mes in ["Enero-Febrero 2024", "Febrero-Marzo 2024", "Marzo-Abril 2024", "Abril-Mayo 2024", "Mayo-Junio 2024", "Junio-Julio 2024",
            "Julio-Agosto 2024", "Agosto-Septiembre 2024", "Septiembre Octubre 2024", "Octubre-Noviembre 2024", "Noviembre-Diciembre 2024", 
            "Diciembre 2024 - Enero 2025", "Enero-Febrero 2025", "Febrero-Marzo 2025" ]:
    periodos[mes] = st.text_area(f"Observaciones para {mes}", "")

# Botón para calcular las atenciones
if st.button("Calcular Atenciones Mensuales"):
    tabla0 = contar_atenciones(periodos)
    st.write(tabla0)

    # Gráfico de barras
    st.subheader("Gráfico de Atenciones Mensuales")
    x = range(len(tabla0))  # X-axis positions
    offset = 0.4  # Separación entre las barras
    plt.bar(x, tabla0['presenciales'], width=0.4, color='red', alpha=0.4, label='Presenciales', align='center')
    plt.bar([i + offset for i in x], tabla0['virtuales'], width=0.4, color='blue', alpha=0.4, label='Virtuales', align='center')
    plt.xlabel("Periodos")
    plt.ylabel("Cantidad")
    plt.title("Estimación de Atenciones de Medicina Ocupacional")
    plt.xticks([i + 0.2 for i in x], tabla0['nombre'])
    plt.xticks(rotation=45)
    plt.grid(True, axis="y")
    plt.legend()
    st.pyplot(plt)

t.markdown(
    """
    <div style="text-align: center;">
        <h1>________________________________</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Atenciones Prolongados
st.header("Atenciones Prolongadas")

# Input para observaciones de atenciones prolongadas
prolongados = {}
prolongados["prolongadas_24"] = st.text_area("Observaciones Prolongadas", "")

# Botón para calcular atenciones prolongadas
if st.button("Calcular Atenciones Prolongadas"):
    tabla02 = contar_atenciones_prolongadas(prolongados)
    st.write(tabla02)

    # Gráfico de barras para prolongadas
    st.subheader("Gráfico de Atenciones Prolongadas")
    x = np.arange(len(tabla02['nombre']))
    plt.bar(x - 0.05, tabla02['presenciales'], width=0.1, color='red', alpha=0.4, label='Presenciales', align='center')
    plt.bar(x + 0.05, tabla02['virtuales'], width=0.1, color='blue', alpha=0.4, label='Virtuales', align='center')
    plt.xlabel('Periodo')
    plt.ylabel('Cantidad')
    plt.title('Atenciones Prolongadas')
    plt.xticks(x, tabla02['nombre'])
    plt.grid(True, axis="y")
    plt.legend()
    st.pyplot(plt)
