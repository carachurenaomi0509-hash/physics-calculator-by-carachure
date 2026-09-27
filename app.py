import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# CONFIGURACIÓN
# ==================================================

st.set_page_config(
    page_title="Physics Calculator by Nao",
    page_icon="🚀",
    layout="centered"
)

# ==================================================
# ESTILO
# ==================================================

st.markdown("""
<style>
.main {
    background-color: #fff8fc;
}

h1 {
    text-align: center;
}

h2, h3 {
    color: #444444;
}

.subtitle {
    text-align: center;
    color: #777777;
    font-size: 18px;
}

.resultado {
    padding: 15px;
    border-radius: 12px;
    background-color: #f7e8f3;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# ENCABEZADO
# ==================================================

st.title("🚀 Physics Calculator")

st.markdown(
    "<p class='subtitle'>by Nao · Aprende, calcula y visualiza Física</p>",
    unsafe_allow_html=True
)

st.divider()

# ==================================================
# MENÚ
# ==================================================

opcion = st.sidebar.radio(
    "📚 ¿Qué quieres hacer?",
    [
        "📏 MRU",
        "🚗 MRUA",
        "🏀 Tiro vertical",
        "🚀 Tiro parabólico",
        "🔄 Conversor",
        "📚 Aprender"
    ]
)

# ==================================================
# MRU
# ==================================================

if opcion == "📏 MRU":

    st.header("📏 Movimiento Rectilíneo Uniforme")

    st.write(
        "En MRU un objeto se mueve en línea recta "
        "con velocidad constante."
    )

    st.info("💡 Ingresa dos datos para calcular el tercero.")

    d = st.number_input(
        "Distancia (m)",
        min_value=0.0,
        value=0.0
    )

    v = st.number_input(
        "Velocidad (m/s)",
        min_value=0.0,
        value=0.0
    )

    t = st.number_input(
        "Tiempo (s)",
        min_value=0.0,
        value=0.0
    )

    if st.button("🧮 Calcular MRU"):

        datos = sum([
            d != 0,
            v != 0,
            t != 0
        ])

        if datos < 2:

            st.warning(
                "⚠️ Necesitas ingresar al menos dos datos."
            )

        elif d == 0:

            d = v * t

            st.success(
                f"📏 Distancia = {d:.2f} m"
            )

        elif v == 0:

            v = d / t

            st.success(
                f"🚗 Velocidad = {v:.2f} m/s"
            )

        elif t == 0:

            t = d / v

            st.success(
                f"⏱️ Tiempo = {t:.2f} s"
            )

        if t > 0:

            tiempos = np.linspace(0, t, 100)
            posiciones = v * tiempos

            fig, ax = plt.subplots()

            ax.plot(
                tiempos,
                posiciones
            )

            ax.set_xlabel("Tiempo (s)")
            ax.set_ylabel("Distancia (m)")
            ax.set_title("MRU: Distancia vs Tiempo")
            ax.grid()

            st.pyplot(fig)

        with st.expander("📚 Ver procedimiento"):

            st.write("Fórmula principal:")

            st.latex("d = v \\cdot t")

            st.write("Para calcular velocidad:")

            st.latex("v = \\frac{d}{t}")

            st.write("Para calcular tiempo:")

            st.latex("t = \\frac{d}{v}")


# ==================================================
# MRUA
# ==================================================

elif opcion == "🚗 MRUA":

    st.header(
        "🚗 Movimiento Rectilíneo Uniformemente Acelerado"
    )

    st.write(
        "En MRUA la aceleración permanece constante."
    )

    st.info("💡 Ingresa tres datos para calcular el que falta.")

    vi = st.number_input(
        "Velocidad inicial (m/s)",
        value=0.0
    )

    vf = st.number_input(
        "Velocidad final (m/s)",
        value=0.0
    )

    a = st.number_input(
        "Aceleración (m/s²)",
        value=0.0
    )

    t = st.number_input(
        "Tiempo (s)",
        min_value=0.0,
        value=0.0
    )

    if st.button("🧮 Calcular MRUA"):

        datos = sum([
            vi != 0,
            vf != 0,
            a != 0,
            t != 0
        ])

        if datos < 3:

            st.warning(
                "⚠️ Ingresa al menos tres datos."
            )

        elif vf == 0:

            vf = vi + a * t

            d = vi * t + 0.5 * a * t**2

            st.success(
                f"🚗 Velocidad final = {vf:.2f} m/s"
            )

            st.success(
                f"📏 Distancia = {d:.2f} m"
            )

        elif a == 0:

            a = (vf - vi) / t

            d = vi * t + 0.5 * a * t**2

            st.success(
                f"⚡ Aceleración = {a:.2f} m/s²"
            )

            st.success(
                f"📏 Distancia = {d:.2f} m"
            )

        elif t == 0:

            t = (vf - vi) / a

            d = vi * t + 0.5 * a * t**2

            st.success(
                f"⏱️ Tiempo = {t:.2f} s"
            )

            st.success(
                f"📏 Distancia = {d:.2f} m"
            )

        elif vi == 0:

            vi = vf - a * t

            d = vi * t + 0.5 * a * t**2

            st.success(
                f"🚗 Velocidad inicial = {vi:.2f} m/s"
            )

            st.success(
                f"📏 Distancia = {d:.2f} m"
            )

        with st.expander("📚 Ver procedimiento"):

            st.write("Velocidad final:")

            st.latex(
                "v_f = v_i + at"
            )

            st.write("Distancia:")

            st.latex(
                "d = v_i t + \\frac{1}{2}at^2"
            )

            st.write("Aceleración:")

            st.latex(
                "a = \\frac{v_f-v_i}{t}"
            )


# ==================================================
# TIRO VERTICAL
# ==================================================

elif opcion == "🏀 Tiro vertical":

    st.header("🏀 Tiro vertical")

    st.write(
        "Movimiento de un objeto lanzado verticalmente "
        "bajo la acción de la gravedad."
    )

    vi = st.number_input(
        "Velocidad inicial (m/s)",
        min_value=0.0,
        value=10.0
    )

    g = st.number_input(
        "Gravedad (m/s²)",
        value=9.81
    )

    if st.button("🧮 Calcular tiro vertical"):

        tmax = vi / g

        hmax = vi**2 / (2 * g)

        tiempo_total = 2 * tmax

        vf = 0

        st.success(
            f"⏱️ Tiempo para altura máxima = {tmax:.2f} s"
        )

        st.success(
            f"📏 Altura máxima = {hmax:.2f} m"
        )

        st.success(
            f"⏱️ Tiempo total de vuelo = {tiempo_total:.2f} s"
        )

        st.success(
            f"⬆️ Velocidad en la altura máxima = {vf:.2f} m/s"
        )

        tiempos = np.linspace(
            0,
            tiempo_total,
            200
        )

        alturas = (
            vi * tiempos
            - 0.5 * g * tiempos**2
        )

        fig, ax = plt.subplots()

        ax.plot(
            tiempos,
            alturas
        )

        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel("Altura (m)")
        ax.set_title("Tiro vertical")
        ax.grid()

        st.pyplot(fig)

        with st.expander("📚 Ver procedimiento"):

            st.write(
                "Tiempo para alcanzar la altura máxima:"
            )

            st.latex(
                "t_{max} = \\frac{v_i}{g}"
            )

            st.write(
                "Altura máxima:"
            )

            st.latex(
                "h_{max} = \\frac{v_i^2}{2g}"
            )

            st.write(
                "Posición:"
            )

            st.latex(
                "h = v_i t - \\frac{1}{2}gt^2"
            )


# ==================================================
# TIRO PARABÓLICO
# ==================================================

elif opcion == "🚀 Tiro parabólico":

    st.header("🚀 Tiro parabólico")

    st.write(
        "Movimiento de un objeto lanzado con una velocidad "
        "inicial formando un ángulo."
    )

    vi = st.number_input(
        "Velocidad inicial (m/s)",
        min_value=0.0,
        value=20.0
    )

    angulo = st.number_input(
        "Ángulo (grados)",
        min_value=0.0,
        max_value=90.0,
        value=45.0
    )

    g = st.number_input(
        "Gravedad (m/s²)",
        value=9.81
    )

    if st.button("🧮 Calcular tiro parabólico"):

        theta = math.radians(
            angulo
        )

        vx = (
            vi *
            math.cos(theta)
        )

        vy = (
            vi *
            math.sin(theta)
        )

        tiempo = (
            2 * vy / g
        )

        hmax = (
            vy**2 / (2 * g)
        )

        alcance = (
            vx * tiempo
        )

        st.success(
            f"➡️ Velocidad horizontal = {vx:.2f} m/s"
        )

        st.success(
            f"⬆️ Velocidad vertical = {vy:.2f} m/s"
        )

        st.success(
            f"⏱️ Tiempo de vuelo = {tiempo:.2f} s"
        )

        st.success(
            f"📏 Altura máxima = {hmax:.2f} m"
        )

        st.success(
            f"📐 Alcance horizontal = {alcance:.2f} m"
        )

        tiempos = np.linspace(
            0,
            tiempo,
            200
        )

        x = vx * tiempos

        y = (
            vy * tiempos
            - 0.5 * g * tiempos**2
        )

        fig, ax = plt.subplots()

        ax.plot(
            x,
            y
        )

        ax.set_xlabel(
            "Distancia horizontal (m)"
        )

        ax.set_ylabel(
            "Altura (m)"
        )

        ax.set_title(
            "Trayectoria parabólica"
        )

        ax.grid()

        st.pyplot(fig)

        with st.expander("📚 Ver procedimiento"):

            st.write(
                "Componente horizontal:"
            )

            st.latex(
                "v_x = v_i\\cos(\\theta)"
            )

            st.write(
                "Componente vertical:"
            )

            st.latex(
                "v_y = v_i\\sin(\\theta)"
            )

            st.write(
                "Tiempo de vuelo:"
            )

            st.latex(
                "t = \\frac{2v_y}{g}"
            )

            st.write(
                "Altura máxima:"
            )

            st.latex(
                "h_{max} = \\frac{v_y^2}{2g}"
            )

            st.write(
                "Alcance:"
            )

            st.latex(
                "R = v_x t"
            )


# ==================================================
# CONVERSOR
# ==================================================

elif opcion == "🔄 Conversor":

    st.header("🔄 Conversor de unidades")

    tipo = st.selectbox(
        "¿Qué quieres convertir?",
        [
            "Distancia",
            "Velocidad",
            "Tiempo",
            "Aceleración",
            "Ángulo"
        ]
    )

    if tipo == "Distancia":

        valor = st.number_input(
            "Valor",
            value=1.0
        )

        unidad = st.selectbox(
            "Unidad",
            [
                "m",
                "km",
                "cm",
                "mm",
                "ft",
                "in",
                "mi"
            ]
        )

        factores = {
            "m": 1,
            "km": 1000,
            "cm": 0.01,
            "mm": 0.001,
            "ft": 0.3048,
            "in": 0.0254,
            "mi": 1609.344
        }

        if st.button("🔄 Convertir"):

            metros = (
                valor *
                factores[unidad]
            )

            st.write(
                f"**Metros:** {metros:.4f} m"
            )

            st.write(
                f"**Kilómetros:** {metros/1000:.4f} km"
            )

            st.write(
                f"**Centímetros:** {metros*100:.4f} cm"
            )

            st.write(
                f"**Pies:** {metros/0.3048:.4f} ft"
            )

    elif tipo == "Velocidad":

        valor = st.number_input(
            "Valor",
            value=1.0
        )

        unidad = st.selectbox(
            "Unidad",
            [
                "m/s",
                "km/h",
                "ft/s",
                "mph"
            ]
        )

        factores = {
            "m/s": 1,
            "km/h": 1000 / 3600,
            "ft/s": 0.3048,
            "mph": 1609.344 / 3600
        }

        if st.button("🔄 Convertir"):

            ms = (
                valor *
                factores[unidad]
            )

            st.write(
                f"**m/s:** {ms:.4f}"
            )

            st.write(
                f"**km/h:** {ms*3.6:.4f}"
            )

            st.write(
                f"**ft/s:** {ms/0.3048:.4f}"
            )

            st.write(
                f"**mph:** {ms*3600/1609.344:.4f}"
            )

    elif tipo == "Tiempo":

        valor = st.number_input(
            "Valor",
            value=1.0
        )

        unidad = st.selectbox(
            "Unidad",
            [
                "s",
                "min",
                "h",
                "ms"
            ]
        )

        factores = {
            "s": 1,
            "min": 60,
            "h": 3600,
            "ms": 0.001
        }

        if st.button("🔄 Convertir"):

            segundos = (
                valor *
                factores[unidad]
            )

            st.write(
                f"**Segundos:** {segundos:.4f} s"
            )

            st.write(
                f"**Minutos:** {segundos/60:.4f} min"
            )

            st.write(
                f"**Horas:** {segundos/3600:.4f} h"
            )

    elif tipo == "Aceleración":

        valor = st.number_input(
            "Valor",
            value=1.0
        )

        unidad = st.selectbox(
            "Unidad",
            [
                "m/s²",
                "ft/s²"
            ]
        )

        if st.button("🔄 Convertir"):

            if unidad == "m/s²":

                ms2 = valor

            else:

                ms2 = (
                    valor *
                    0.3048
                )

            st.write(
                f"**m/s²:** {ms2:.4f}"
            )

            st.write(
                f"**ft/s²:** {ms2/0.3048:.4f}"
            )

    elif tipo == "Ángulo":

        valor = st.number_input(
            "Valor",
            value=45.0
        )

        unidad = st.selectbox(
            "Unidad",
            [
                "grados",
                "radianes"
            ]
        )

        if st.button("🔄 Convertir"):

            if unidad == "grados":

                rad = math.radians(
                    valor
                )

                st.write(
                    f"**Radianes:** {rad:.4f}"
                )

            else:

                grados = math.degrees(
                    valor
                )

                st.write(
                    f"**Grados:** {grados:.4f}"
                )


# ==================================================
# APRENDER
# ==================================================

elif opcion == "📚 Aprender":

    st.header("📚 Modo Aprender")

    st.write(
        "Repasa los conceptos y fórmulas principales "
        "antes de resolver tus ejercicios."
    )

    tema = st.selectbox(
        "Elige un tema",
        [
            "MRU",
            "MRUA",
            "Tiro vertical",
            "Tiro parabólico"
        ]
    )

    if tema == "MRU":

        st.subheader("📏 Movimiento Rectilíneo Uniforme")

        st.write(
            "El MRU ocurre cuando un objeto se mueve "
            "en línea recta con velocidad constante."
        )

        st.latex("d = vt")
        st.latex("v = \\frac{d}{t}")
        st.latex("t = \\frac{d}{v}")

    elif tema == "MRUA":

        st.subheader(
            "🚗 Movimiento Rectilíneo Uniformemente Acelerado"
        )

        st.write(
            "En MRUA existe una aceleración constante."
        )

        st.latex(
            "v_f = v_i + at"
        )

        st.latex(
            "d = v_i t + \\frac{1}{2}at^2"
        )

        st.latex(
            "a = \\frac{v_f-v_i}{t}"
        )

    elif tema == "Tiro vertical":

        st.subheader("🏀 Tiro vertical")

        st.write(
            "La gravedad provoca que el objeto "
            "disminuya su velocidad hasta llegar "
            "a cero en la altura máxima."
        )

        st.latex(
            "t_{max} = \\frac{v_i}{g}"
        )

        st.latex(
            "h_{max} = \\frac{v_i^2}{2g}"
        )

        st.latex(
            "h = v_i t - \\frac{1}{2}gt^2"
        )

    elif tema == "Tiro parabólico":

        st.subheader("🚀 Tiro parabólico")

        st.write(
            "El movimiento se puede analizar separando "
            "las componentes horizontal y vertical."
        )

        st.latex(
            "v_x = v_i\\cos(\\theta)"
        )

        st.latex(
            "v_y = v_i\\sin(\\theta)"
        )

        st.latex(
            "t = \\frac{2v_y}{g}"
        )

        st.latex(
            "h_{max} = \\frac{v_y^2}{2g}"
        )

        st.latex(
            "R = v_x t"
        )


# ==================================================
# PIE DE PÁGINA
# ==================================================

st.divider()

st.caption(
    "🚀 Physics Calculator by Nao · Hecho para aprender Física 💗"
)
