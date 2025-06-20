import pandas as pd
import streamlit as st 
import plotly_express as px

#Creamos el encabezado de la página
st.header('Información de vehículos de US')

car_data = pd.read_csv('vehicles_us.csv') #vamos a leer los datos de los vehiculos


st.write('¿Selecciona el o los gráficoas que se desea ver?')

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




button_modelos = st.button('Inspeccionar modelos y tipo por condición')

if button_modelos: 
    st.write('Modeloes y tipo por la condición del coche')
    fig = px.sunburst(car_data,path=['condition','type','model'],values='price')
    fig.show()