import pandas as pd
import streamlit as st 
import plotly_express as px

#Creamos el encabezado de la página
st.header('Información de vehículos de US')

car_data = pd.read_csv('vehicles_us.csv') #vamos a leer los datos de los vehiculos


st.markdown("### 🔍 Selecciona el o los gráficos que se desea ver")
# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir dispersión')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro.')
    # creamos el histograma
    fig = px.histogram(car_data, x="odometer")

    #mostramos un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
     

if build_scatter: # al hacer click en el botón de dispersión
    st.write('Gráfico de dispersión del Odometro y el precio de los coches.')

    # creamos el gráfico de dispersión
    fig_disp = px.scatter(car_data, x="odometer", y="price")

    # mostramos el gráfico
    st.plotly_chart(fig_disp, use_container_width=True)





st.markdown("### 🔍 Inspeccionar modelos y tipo por condición")
# vamos a crear una oción intereactica para ver los diferentes modelos según el tipo y condición
st.write('Inspeccionar modelos y tipo por condición')

modelos_unicos = car_data['model'].unique() # Extraemos lo modelos únicos

if 'modelo_seleccionado' not in st.session_state:  # si no hemos seleccionado ningún modelos asignamos el primero
    st.session_state['modelo_seleccionado'] = modelos_unicos[0]

# Creamos el combo de las opcciones de los modelos y lo gardamos en la sessión
modelo = st.selectbox("Selecciona un modelo",modelos_unicos,
                      index=list(modelos_unicos).index(st.session_state['modelo_seleccionado'])) # Ponemo siempre el que está en la sessión


# Guardamos la selección actual
st.session_state['modelo_seleccionado'] = modelo

# filtramos los valores según el modelo
cat_data_filtered = car_data[car_data['model'] == modelo]

# vamos a mostrar las gráficas si existe el modelo

if not cat_data_filtered.empty:
    fig = px.sunburst(
        cat_data_filtered,
        path=['condition', 'type'],
        values='price',
        title=f"Distribución de percios para el modelo: {modelo}"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No hay datos para ese modelo.")