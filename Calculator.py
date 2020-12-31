import streamlit as st
import math


st.markdown("<style>h1{color:lightgrey;}</style>",unsafe_allow_html=True)
st.markdown("<style>.reportview-container{ background: linear-gradient(#876363, #FFEFA1); color: white; }</style>", unsafe_allow_html=True)

st.title("Fischis Pidsa Comjuter 🍕🐟")
st.write("Grüß dich, Fischi. Hier kannst du berechnen, welche Pidsa das bessere Preis-Leistungs-Verhältnis hat")
st.write("Pidsa 1:")
first_price = st.number_input("Preis in Euro ")
first_durchmesser = st.number_input("Durchmesser in cm ")
st.write("Pidsa 2:")
second_price = st.number_input("Preis in Euro")
second_durchmesser = st.number_input("Durchmesser in cm")


if first_price and first_durchmesser and second_durchmesser and second_price:
    crust = st.write("Rand mitberechnen?")
    with_crust = st.checkbox("ja")
    without_crust = st.checkbox("nein")
    button = st.button("Los geht's")
    if button:
        if without_crust:
            first_radius = (first_durchmesser-4)/2
            second_radius = (second_durchmesser-4)/2
        else:
            first_radius = first_durchmesser/2
            second_radius = second_durchmesser/2
        first_flaeche = math.pi*first_radius**2
        first_cost_cm = first_price/ first_flaeche
        second_flaeche = math.pi*second_radius**2
        second_cost_cm = second_price / second_flaeche

        st.write("Pidsa 1: ", round(first_cost_cm,2)," Euro pro cm2")
        st.write("Pidsa 2: ", round(second_cost_cm,2), " Euro pro cm2")

        st.balloons()
else:
    st.write("Tschulligom, da fehlt noch mindestens eine Zahl!")