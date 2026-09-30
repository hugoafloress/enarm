import streamlit as st
import datetime
import random

# Configuración de la página
st.set_page_config(
    page_title="Para mi novio hermoso ❤️",
    page_icon="💖",
    layout="centered"
)

# Efecto de bienvenida al abrir
st.snow()

# Título Principal
st.title("💖 Para el Amor de mi Vida 💖")
st.subheader("Una cartita especial hecha con todo mi corazón... ✨")

st.write("---")

# Pestañas interactivas
tab1, tab2, tab3, tab4 = st.tabs([
    "💌 Cartitas de Amor", 
    "⏳ Nuestro Tiempo", 
    "🎲 Razones para Amarte", 
    "💘 Pregunta Especial"
])

# ---------------------------------------------------------
# PESTAÑA 1: CARTAS INTERACTIVAS
# ---------------------------------------------------------
with tab1:
    st.header("✉️ Cartas de Amor")
    st.write("Abre la cartita que necesites leer hoy:")
    
    with st.expander("💌 Léeme cuando tengas un día difícil o estés cansado"):
        st.write("""
        **Mi niño hermoso:**  
        Sé que hay días que pueden ser pesados y agotadores, pero quiero recordarte lo increíble y fuerte que eres. 
        No olvides que no estás solo en nada; siempre estaré aquí para darte un abrazo bien apretado, escucharte o simplemente consentirte. 
        Respira profundo, todo estará bien. ¡Te amo muchísimo! 💖
        """)

    with st.expander("💖 Léeme cuando extrañes mis besos y abrazos"):
        st.write("""
        **Amor de mi vida:**  
        Si estás leyendo esto y no estoy a tu lado, cierra los ojos por 5 segundos e imagíname dándote un beso gigante en la mejilla y abrazándote tan fuerte que se te olvide todo lo malo. 
        Pronto nos veremos para darnos todos los abrazos acumulados. ¡Contando las horas para verte! 💋
        """)

    with st.expander("✨ Léeme cuando quieras saber cuánto significas para mí"):
        st.write("""
        **Mi amor:**  
        Eres mi lugar seguro, mi persona favorita en todo el universo y la razón de mis sonrisas más sinceras. 
        Llegaste a mi vida a iluminarlo todo y agradezco cada segundo a tu lado. Gracias por ser tan lindo, atento y por amarme de la forma en que lo haces. 
        ¡Eres el mejor novio del mundo entero! 🥰
        """)

# ---------------------------------------------------------
# PESTAÑA 2: CONTADOR DE TIEMPO
# ---------------------------------------------------------
with tab2:
    st.header("⏳ Nuestro Tiempo Juntos")
    st.write("¿Cuánto tiempo llevamos siendo los más felices?")
    
    # 👈 CAMBIA AQUÍ TU FECHA DE INICIO (Año, Mes, Día)
    fecha_inicio = datetime.date(2023, 5, 15)  
    hoy = datetime.date.today()
    dias_juntos = (hoy - fecha_inicio).days

    col1, col2, col3 = st.columns(3)
    col1.metric("Días Juntos", f"{dias_juntos} ☀️")
    col2.metric("Horas de Amor", f"{dias_juntos * 24} ⏱️")
    col3.metric("Minutos Felices", f"{dias_juntos * 24 * 60} 💖")

    st.info(f"📅 Juntos desde el **{fecha_inicio.strftime('%d/%m/%Y')}** 💕")

# ---------------------------------------------------------
# PESTAÑA 3: GENERADOR DE RAZONES
# ---------------------------------------------------------
with tab3:
    st.header("🎲 Razones por las que te amo")
    st.write("Presiona el botón para descubrir una razón:")

    razones = [
        "Amo la forma en que tus ojos brillan cuando sonríes. ✨",
        "Amo lo atento y cariñoso que eres conmigo siempre. 💕",
        "Amo tus abrazos que me hacen sentir en paz. 🫂",
        "Amo cómo me haces reír incluso cuando estoy triste. 😂",
        "Amo la voz hermosa que tienes y cómo me hablas bonito. 🗣️❤️",
        "Amo que seas mi mejor amigo y mi novio al mismo tiempo. 👩‍❤️‍👨",
        "Amo todos los momentos que pasamos juntos. 📸",
        "Amo simplemente todo de ti, exactamente como eres. ❤️"
    ]

    if st.button("✨ ¡Toca aquí para descubrir una razón!"):
        st.success(f"💖 **{random.choice(razones)}**")
        st.balloons()

# ---------------------------------------------------------
# PESTAÑA 4: PREGUNTA ESPECIAL
# ---------------------------------------------------------
with tab4:
    st.header("💘 Una pregunta muy importante...")
    st.subheader("¿Prometes seguir haciéndome la persona más feliz del mundo por siempre?")

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("¡SÍ, ACEPTO CADA SEGUNDO! ❤️"):
            st.balloons()
            st.snow()
            st.success("🎉 **¡SABÍA QUE DIRÍAS QUE SÍ!** Te amo con todo mi corazón, eres el novio más maravilloso del mundo. 😘❤️✨")

    with col_b:
        if st.button("No... 😜"):
            st.warning("⚠️ Error: Esa opción no está disponible porque me amas demasiado. ¡Intenta con el botón de la izquierda! 😂💖")

# Pie de página
st.write("---")
st.caption("Hecho con muchísimo amor especialmente para ti 💖✨")
