import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ─────────────────────────────────────────────
# CONFIGURACIÓN DE PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Tablero para dibujo",
    page_icon="🎨",
    layout="wide"
)

# ─────────────────────────────────────────────
# ESTILOS VISUALES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(20, 184, 166, 0.15), transparent 30%),
        radial-gradient(circle at top right, rgba(99, 102, 241, 0.14), transparent 28%),
        #f8fafc;
    color: #0f172a;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
    border-right: 1px solid rgba(148, 163, 184, 0.25);
}

[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
}

/* Inputs del sidebar */
[data-testid="stSidebar"] .stSelectbox,
[data-testid="stSidebar"] .stSlider,
[data-testid="stSidebar"] .stColorPicker {
    background: rgba(255, 255, 255, 0.06);
    padding: 14px;
    border-radius: 16px;
    border: 1px solid rgba(226, 232, 240, 0.12);
    margin-bottom: 12px;
}

/* Títulos */
h1 {
    color: #0f172a !important;
    font-size: 2.6rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.04em;
}

h2, h3 {
    color: #1e293b !important;
    font-weight: 700 !important;
}

/* Tarjetas */
.hero-card {
    background: linear-gradient(135deg, #ffffff 0%, #eefcff 100%);
    border: 1px solid #ccfbf1;
    padding: 34px;
    border-radius: 28px;
    margin-bottom: 22px;
    box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08);
}

.hero-badge {
    display: inline-block;
    background: #ccfbf1;
    color: #0f766e;
    padding: 7px 13px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.03em;
    text-transform: uppercase;
    margin-bottom: 14px;
}

.hero-text {
    color: #475569;
    font-size: 1.03rem;
    line-height: 1.65;
    margin: 0;
    max-width: 760px;
}

.canvas-card {
    background: rgba(255, 255, 255, 0.94);
    border: 1px solid #e2e8f0;
    padding: 24px;
    border-radius: 26px;
    box-shadow: 0 20px 55px rgba(15, 23, 42, 0.08);
}

.info-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 5px solid #14b8a6;
    padding: 18px 20px;
    border-radius: 20px;
    margin-bottom: 18px;
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.05);
}

.sidebar-panel {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(226, 232, 240, 0.14);
    border-radius: 18px;
    padding: 16px;
    margin-bottom: 16px;
}

.sidebar-panel p {
    font-size: 0.88rem;
    line-height: 1.5;
    margin: 8px 0 0 0;
    color: #cbd5e1 !important;
}

.size-box {
    background: rgba(20, 184, 166, 0.12);
    border: 1px solid rgba(94, 234, 212, 0.25);
    border-radius: 16px;
    padding: 12px 14px;
    margin-bottom: 10px;
}

.size-label {
    font-size: 0.82rem;
    color: #cbd5e1 !important;
    margin-bottom: 4px;
}

.size-value {
    font-size: 1.15rem;
    font-weight: 800;
    color: #ffffff !important;
}

/* Canvas */
iframe {
    border-radius: 18px !important;
}

/* Ocultar elementos innecesarios */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER PRINCIPAL
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-card">
    <span class="hero-badge">Herramienta creativa</span>
    <h1>🎨 Tablero para dibujo</h1>
    <p class="hero-text">
        Dibuja libremente, crea formas básicas y ajusta los colores del tablero desde el panel lateral.
        La interfaz está organizada para que tengas las herramientas principales siempre a la mano.
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎛️ Panel de dibujo")

    st.markdown("""
    <div class="sidebar-panel">
        <strong>Propiedades del tablero</strong>
        <p>
            Configura la herramienta, el grosor del trazo y los colores antes de empezar a dibujar.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Canvas dimensions
    st.markdown("### 📐 Dimensiones")

    canvas_width = 600
    canvas_height = 400

    st.markdown(f"""
    <div class="size-box">
        <div class="size-label">Ancho del tablero</div>
        <div class="size-value">{canvas_width}px</div>
    </div>

    <div class="size-box">
        <div class="size-label">Alto del tablero</div>
        <div class="size-value">{canvas_height}px</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ✏️ Herramientas")

    # Drawing mode selector
    drawing_mode = st.selectbox(
        "Herramienta de dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Stroke width slider
    stroke_width = st.slider(
        'Selecciona el ancho de línea',
        1,
        30,
        15
    )

    st.markdown("### 🎨 Colores")

    # Stroke color picker
    stroke_color = st.color_picker(
        "Color de trazo",
        "#FFFFFF"
    )

    # Background color
    bg_color = st.color_picker(
        "Color de fondo",
        "#000000"
    )

# ─────────────────────────────────────────────
# CONTENIDO PRINCIPAL
# ─────────────────────────────────────────────
left_col, right_col = st.columns([3, 1])

with left_col:
    st.markdown("""
    <div class="canvas-card">
        <h3 style="margin-top:0;">🖌️ Área de dibujo</h3>
        <p style="color:#64748b; margin-top:-4px;">
            Usa el mouse o el touchpad para dibujar directamente sobre el tablero.
        </p>
    """, unsafe_allow_html=True)

    # Create a canvas component with dynamic key
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}"  # Dynamic key based on dimensions
    )

    st.markdown("</div>", unsafe_allow_html=True)

with right_col:
    st.markdown(f"""
    <div class="info-card">
        <h3 style="margin-top:0;">⚙️ Estado actual</h3>
        <p><strong>Herramienta:</strong><br>{drawing_mode}</p>
        <p><strong>Grosor:</strong><br>{stroke_width}px</p>
        <p><strong>Tamaño:</strong><br>{canvas_width} × {canvas_height}px</p>
    </div>

    <div class="info-card">
        <h3 style="margin-top:0;">💡 Uso rápido</h3>
        <p style="color:#475569;">
            Cambia la herramienta en el panel izquierdo y luego dibuja sobre el tablero.
            Puedes modificar el grosor, el color del trazo y el fondo cuando quieras.
        </p>
    </div>
    """, unsafe_allow_html=True)
