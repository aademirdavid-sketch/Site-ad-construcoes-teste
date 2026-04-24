import streamlit as st

# Configuração da página
st.set_page_config(page_title="AD Construções & PatologiaBR", layout="wide", page_icon="🏗️")

# --- ESTILO VISUAL PERSONALIZADO ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        background-color: #25D366;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        height: 3em;
    }
    .titulo-principal { color: #1E3A8A; font-size: 40px; font-weight: bold; text-align: center; }
    .subtitulo { color: #555; text-align: center; margin-bottom: 30px; }
    .secao { background-color: #f1f4f9; padding: 20px; border-radius: 15px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<p class="titulo-principal">AD Construções e Gerenciamento</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Mestre de Obras Sênior | Especialista em Gerir Pessoas e Projetos</p>', unsafe_allow_html=True)

# --- SOBRE E CONTATO (LADO A LADO) ---
col_foto, col_info = st.columns([1, 2])

with col_foto:
    st.image("https://cdn-icons-png.flaticon.com/512/4333/4333644.png", width=200) # Ícone representativo
    st.write("📍 **São Paulo - SP**")
    st.write("📞 (13) 99172-8599")
    st.write("✉️ contatoadconstru@gmail.com")
    
    url_whatsapp = "https://wa.me/5513991728599"
    st.link_button("Falar no WhatsApp", url_whatsapp)

with col_info:
    st.markdown("### 🏗️ Experiência e Autoridade")
    st.write("""
    Com mais de **40 anos de trajetória na construção civil**, atuo no gerenciamento de obras de 
    infraestrutura, terraplenagem e residências de alto padrão. Meu foco é a excelência técnica 
    e a liderança de equipes para garantir que cada etapa siga rigorosamente as normas NBR.
    """)
    st.markdown("---")
    st.markdown("#### Nossos Serviços")
    st.write("✅ Gerenciamento e Fiscalização de Obras")
    st.write("✅ Assessoria Técnica para Pequenos e Médios Projetos")
    st.write("✅ Consultoria em Manutenção e Normas Técnicas")

# --- SEÇÃO INFERIOR: ANÁLISE DE PATOLOGIAS (PatologiaBR) ---
st.markdown('<div class="secao">', unsafe_allow_html=True)
st.header("🔍 PatologiaBR - Análise de Patologias")
st.write("Utilize nossa ferramenta tecnológica para identificar problemas estruturais ou de acabamento.")

# Upload de imagem [cite: 4, 5]
arquivo_foto = st.file_uploader("Selecione a imagem da obra ou patologia", type=["jpg", "png", "jpeg"])

if arquivo_foto is not None:
    st.image(arquivo_foto, caption="Imagem carregada para análise", use_container_width=True) # [cite: 7]
    
    st.warning("⚠️ **Atenção:** A foto foi carregada no site! [cite: 8]")
    st.info("Para eu receber a análise, clique no botão abaixo e anexe a foto manualmente no WhatsApp. [cite: 9]")
    
    # Botão de ação para o WhatsApp [cite: 10]
    st.link_button("📩 ENVIAR AVISO E FOTO PELO WHATSAPP", url_whatsapp)
st.markdown('</div>', unsafe_allow_html=True)

# --- RODAPÉ ---
st.markdown("---")
st.caption("© 2026 AD Construções - Tecnologia e Experiência aplicada à Engenharia. [cite: 11]")
