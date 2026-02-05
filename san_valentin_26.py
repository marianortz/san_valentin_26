import streamlit as st

if "etapa" not in st.session_state:
    st.session_state.etapa = "inicio"

st.title("💗 Feliz Día de Amor y de Amistad")
st.write("(Pero más del amor)")
st.image("foto1.jpg")

st.header("Elige tu regalo de san valentín:")

if st.session_state.etapa == "inicio":
    col1, col2, col3 = st.columns(3)

    if col1.button("Un postre 🍰"):
        st.session_state.etapa = "opcion"
        st.rerun ()
    if col2.button("Una cena 🕯️"):
        st.session_state.etapa = "opcion"
        st.rerun ()
    if col3.button("Unas tangas (para mí) 👙"):
        st.session_state.etapa = "correcta"

elif st.session_state.etapa == "opcion":
    st.write("¿Estás seguro?")
    st.image("foto4.png", width=100)
    st.write("Podrías mejorar tu regalo")

    c_si, c_no = st.columns(2)

    if c_si.button("Si"):
        st.session_state.etapa = "vuelve_a_pensar"
        st.rerun()
    if c_no.button("Regresar a las opciones"):
        st.session_state.etapa = "inicio"
        st.rerun()

elif st.session_state.etapa == "vuelve_a_pensar":
    st.write("Vuelve a pensarlo")
    st.image("foto3.png", width=100)
    st.write("¿Estás seguro?")

    c_si, c_no = st.columns(2)

    if c_si.button("Si"):
        st.session_state.etapa = "pensar_2"
        st.rerun()
    if c_no.button("Regresar a las opciones"):
        st.session_state.etapa = "inicio"
        st.rerun()

elif st.session_state.etapa == "pensar_2":
    st.image("foto5.png", width=100)
    st.write("¿Seguro, seguro?")

    c_si, c_no = st.columns(2)

    if c_si.button("Si"):
        st.session_state.etapa = "opcion"
        st.rerun()
    if c_no.button("Regresar a las opciones"):
        st.session_state.etapa = "inicio"
        st.rerun()

elif st.session_state.etapa == "correcta":
    st.subheader("¡Felicidades, escogiste la opción correcta!")
    st.image("foto2.png",width=100)
    st.write("Ya después hablamos de las condiciones")
    if st.button("Regresar al inicio"):
        st.session_state.etapa = "inicio"


estilo_footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: black;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    border-top: 1px solid #dcdcdc;
    z-index: 1000; /* Asegura que quede encima de otros elementos */
}
</style>
"""
st.markdown(estilo_footer, unsafe_allow_html=True)

st.markdown('<div class="footer">Todo esto fue creado 99% por mi solín solita porque te quería enseñar un poquito de lo que hago (el otro 1% fue este pie, porque no sabía cómo hacerloS)', unsafe_allow_html=True)