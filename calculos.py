import pandas as pd
import streamlit as st
from datetime import datetime

# Obtener las tasas y fechas ingresadas por el usuario
FCB = st.text_input("Ingrese tasa facial:")
st.write("FCB:", FCB)
base = st.text_input("Ingrese la base del bono:")
st.write("Base:", base)
tasa_anual = st.text_input('Ingrese tasa de referencia anual:')
st.write("Tasa Anual:", tasa_anual)
fecha_emision = st.date_input('Seleccione la fecha de emisión')
fecha_vencimiento = st.date_input('Seleccione la fecha de vencimiento')


# Validar que las tasas no estén vacías
if FCB and base and tasa_anual:
    # Convertir las tasas a números
    FCB = float(FCB)
    base = float(base)
    tasa_anual = float(tasa_anual)

    # Calcular la tasa diaria
    tasa_diaria = (1 + (tasa_anual/100))**(1 / base) - 1

    # Mostrar resultados
    st.write('Tasa diaria: ', f'{round(tasa_diaria*100,3)}%')
else:
    st.warning('Por favor, ingrese valores válidos para las tasas.')

# Mostrar fechas
st.write('Fecha de emisión:', fecha_emision)
st.write('Fecha de vencimiento:', fecha_vencimiento)

# =C4/((1+$C$10)^(B4-$B$3)) VPFCB
if fecha_emision and fecha_vencimiento:

    # Obtener el año de emisión y vencimiento
    año_emision = fecha_emision.year
    año_vencimiento = fecha_vencimiento.year
    mes_dia_vencimiento = fecha_vencimiento.strftime('%m-%d')

    # Crear la lista de fechas de pago de cupones

    cupones = []
    for i in range(int(año_vencimiento)-int(año_emision)+1):
        cupones.append(f'{int(año_emision)+i}-{mes_dia_vencimiento}')

    df_cupones = pd.DataFrame({'Pago_cupones': cupones})
    df_cupones['Pago_cupones'] = pd.to_datetime(
        df_cupones['Pago_cupones'], format='%Y-%m-%d')

    st.write('Fechas de cupones:')
    st.write(df_cupones)

    # VALOR ACTUAL VPFCB

    VPFCB = []
    emision = pd.to_datetime(fecha_emision)
    for i in df_cupones['Pago_cupones']:
        # Extraer el número de días

        dias_diferencia = (i - emision).days
        st.write(dias_diferencia)
        VPFCB.append(round((FCB/((1 + tasa_diaria)**(dias_diferencia))), 3))
    # st.write(dias_diferencia)
    # st.write(fecha_emision_timestamp)
    VPFCB = pd.DataFrame({'VPFCB': VPFCB})
    st.write(VPFCB)


else:
    st.warning('Por favor, ingrese fechas válidas de emisión y vencimiento.')
