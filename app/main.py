import streamlit as st
from pathlib import Path

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Para Scarlet",
    page_icon="🎟️",
    layout="centered"
)

# Cambia este nombre si tu imagen tiene otro nombre.
# Debes subir la imagen de la entrada a la misma carpeta que este archivo app.py.
TICKET_IMAGE = "entrada_jonas_tapada.png"

# Opcional: pega aquí un link de Spotify/YouTube si quieres dejar una canción.
# Ejemplo YouTube: "https://www.youtube.com/embed/XXXX"
# Ejemplo Spotify embed: "https://open.spotify.com/embed/track/XXXX"
MUSIC_EMBED_URL = "https://youtu.be/SPGMAjkOsLg?si=L3Y28uhtgMaM1GAV"

# -----------------------------
# STYLING
# -----------------------------
st.markdown(
    """
    <style>
      :root{
        --bg1: #fff7fb;
        --bg2: #ffe4f1;
        --bg3: #f5e8ff;
        --card: rgba(255,255,255,.90);
        --border: rgba(150, 45, 120, .18);
        --shadow: 0 18px 44px rgba(120,40,100,.14);
        --ink: rgba(55, 22, 45, .96);
        --muted: rgba(55, 22, 45, .70);
        --accent: #c0267a;
        --accent2: #7c3aed;
        --red: #bf311a;
      }

      html, body, [class*="css"] { 
        color: var(--ink); 
      }

      .stApp{
        background:
          radial-gradient(900px 520px at 50% -140px, rgba(192,38,122,.25), transparent 60%),
          radial-gradient(780px 480px at 110% 10%, rgba(124,58,237,.18), transparent 60%),
          linear-gradient(180deg, var(--bg2) 0%, var(--bg1) 55%, #ffffff 100%);
      }

      .block-container { 
        max-width: 820px; 
        padding-top: 1.4rem; 
        padding-bottom: 2.4rem;
      }

      .title{
        color: var(--accent) !important;
        text-align:center;
        margin: 0;
        font-size: 48px;
        line-height: 1.05;
        font-family: Georgia, 'Times New Roman', serif;
      }

      .subtitle{
        text-align:center;
        color: var(--muted) !important;
        margin-top: 8px;
        font-size: 17px;
      }

      .soft-card{
        border: 1px solid var(--border);
        border-radius: 24px;
        padding: 22px;
        background: var(--card);
        box-shadow: var(--shadow);
        margin-top: 18px;
      }

      .soft-card, 
      .soft-card p, 
      .soft-card div, 
      .soft-card h2,
      .soft-card h3{
        color: var(--ink) !important;
      }

      .center{
        text-align:center;
      }

      .muted{ 
        color: var(--muted) !important; 
      }

      .divider{
        height:1px;
        background: rgba(150,45,120,.14);
        margin:20px 0;
      }

      .tiny-label{
        text-transform: uppercase;
        letter-spacing: 2.5px;
        color: var(--accent2) !important;
        font-size: 12px;
        font-weight: 700;
        text-align:center;
        margin-bottom: 8px;
      }

      .reveal-title{
        font-family: Georgia, 'Times New Roman', serif;
        color: var(--red) !important;
        text-align:center;
        font-size: 38px;
        margin: 4px 0 14px 0;
      }

      .ticket-card{
        border: 2px dashed rgba(192,38,122,.55);
        border-radius: 24px;
        padding: 22px;
        background: linear-gradient(135deg, rgba(255,255,255,.96), rgba(255,239,248,.96));
        box-shadow: 0 16px 34px rgba(192,38,122,.12);
        margin-top: 18px;
      }

      .note{
        font-size: 14px;
        color: var(--muted) !important;
        text-align:center;
        margin-top: 10px;
      }

      div.stButton{
        display: flex;
        justify-content: center;
        margin-top: .2rem !important;
        margin-bottom: .2rem !important;
      }

      .stButton > button{
        min-height: 56px !important;
        border-radius: 16px !important;
        padding: 0 26px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-weight: 800 !important;
        border: 1px solid rgba(192,38,122,.45) !important;
        box-shadow: 0 12px 26px rgba(192,38,122,.20) !important;
        background: linear-gradient(135deg, #ffffff, #fff1f8) !important;
        color: var(--ink) !important;
        line-height: normal !important;
        transform: translateY(1px) !important;
      }

      .stMarkdown, .stMarkdown * {
        color: var(--ink) !important;
      }

      div[data-testid="stAlert"] *{
        color: var(--ink) !important;
      }

      img{
        border-radius: 18px;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<h1 class="title">Para Scarlet</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Una pequeña sorpresa preparada con cariño y un poquito de drama, como corresponde.</p>',
    unsafe_allow_html=True
)

# -----------------------------
# INTRO CARD
# -----------------------------
st.markdown(
    """
    <div class="soft-card center">
      <p class="tiny-label">Antes de abrir</p>
      <h3>Scarlet, este regalo es para que vivas una noche increíble.</h3>
      <p>
        Pensé en cómo darte este regalo, así que espero que lo recibas
      </p>
      <p class="muted">
        Ahora sí... respira, porque tienes que abrir la sorpresa.
      </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# REVEAL BUTTON
# -----------------------------
if "opened" not in st.session_state:
    st.session_state.opened = False

if st.button("Abrir sorpresa"):
    st.session_state.opened = True

# -----------------------------
# REVEAL CONTENT
# -----------------------------
if st.session_state.opened:
    st.balloons()

    st.markdown(
        """
        <div class="ticket-card">
          <p class="tiny-label">Tu regalo es</p>
          <h2 class="reveal-title">Jonas Brothers</h2>
          <p class="center" style="font-size:18px;">
            Espero que no tengas planes para el <strong>11 de mayo</strong>, porque...
          </p>
          <p class="center" style="font-size:22px; font-weight:800; color:#bf311a !important;">
            Te vas a ver a los Jonas Brothers. (Yes, girl)
          </p>
          <div class="divider"></div>
          <p class="center">
            Esta entrada es para ti, para que disfrutes la noche como tú quieras.
            Quiero que cantes, grites, te emociones y lo pases a toda raja.
            Ojalá sea una noche llena de emoción y recuerdos bonitos.
          </p>
          <p class="note">
            La entrada oficial te la enviaré por correo. Esta es solo la entrega dramática del regalo jeje.
            Te amo.
          </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------
    # MUSIC SECTION
    # -----------------------------
    st.markdown(
        """
        <div class="soft-card center">
          <p class="tiny-label">Para entrar en mood</p>
          <p>Antes de ver la entrada, puedes poner una canción de fondo.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if MUSIC_EMBED_URL.strip():
        st.components.v1.iframe(MUSIC_EMBED_URL, height=152, scrolling=False)
    else:
        st.info("Aquí puedes agregar un embed de Spotify o YouTube en la variable MUSIC_EMBED_URL.")

    # -----------------------------
    # TICKET IMAGE SECTION
    # -----------------------------
    ticket_path = Path(TICKET_IMAGE)

    st.markdown(
        """
        <div class="soft-card center">
          <p class="tiny-label">Preview de tu entrada</p>
          <p>El código está tapado por seguridad. La entrada oficial llega por correo.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if ticket_path.exists():
        st.image(str(ticket_path), use_container_width=True)
    else:
        st.warning(
            f"Aún falta subir la imagen de la entrada. Guarda la imagen como '{TICKET_IMAGE}' en la misma carpeta de app.py."
        )

    st.markdown(
        """
        <div class="soft-card center">
          <p>
            Espero que la pases precioso, que cantes tus canciones favoritas y que esta sea una noche muy especial para ti.
            Te amo. 
          </p>
          <p class="muted">Con cariño, Thiare</p>
        </div>
        """,
        unsafe_allow_html=True
    )

