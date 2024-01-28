import streamlit as st
import pandas as pd
import numpy as np
import os
import warnings
import io
import base64
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="???", page_icon=Image.open(
    'assets/defi.jpg'), layout="wide")

# ------ MENU ------

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['Bonos', 'Stocks'],
        default_index=0,
        icons=["house-heart", "journal-bookmark-fill"],
        menu_icon="cast",
    )

# ------ Bonos ------

if selected == 'Bonds':

    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=['Coupon', 'Without Coupon'],
            icons=["table", "table"],
            menu_icon="cast",
            default_index=0,
        )

    # con cupón

    if selected == 'Coupon':
        st.title("Coupon")
        st.markdown(
            """""")

    # Sin cupón

    if selected == 'Without Coupon':

        st.title("Without Coupon")
        st.markdown(
            """""")

# ------ Acciones ------

if selected == 'Stocks':

    st.title('Stocks')
    st.markdown(
        """""")
