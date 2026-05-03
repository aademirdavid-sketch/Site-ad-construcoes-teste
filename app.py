import streamlit as st
import os

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
        height: 3.5em;
    }
    .titulo-principal { color: #1E3A8A; font-size: 42px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitulo { color: #555; text-align: center; font-size: 20px; margin-bottom: 30px; }
    .cartao-servico {
        background-color: #f8f9fa;
        padding: 20px;
        border-left: 5px solid #1E3A8A;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .secao-patologia { background-color: #f1f4f9; padding: 30px; border-radius: 15px; margin-top: 40px; border: 1px solid #d1d9e6; }
    </style>
    """, unsafe_allow_html=True)

# --- TOPO: LOGO E TÍTULO ---
col_logo, col_tit = st.columns([1, 4])

with col_logo:
    # Tenta carregar a logo do GitHub. Se não existir, coloca um ícone temporário.
    if os.path.exists("IMG_20260210_110844~4.png"):
        st.image("IMG_20260210_110844~4.png",width=300)
    else:
        st.info("Upload 'logo_ad.png' no GitHub")
        st.image("https://cdn-icons-png.flaticon.com/512/4333/4333644.png", width=120)

with col_tit:
    st.markdown('<p class="titulo-principal">AD Construções e Gerenciamento</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Mestre de Obras Sênior | Especialista em Gerir Pessoas e Projetos</p>', unsafe_allow_html=True)

st.markdown("---")

# --- SEÇÃO 1: SOBRE E CONTATO ---
col_info, col_contato = st.columns([2, 1])

with col_info:
    st.subheader("🏗️ Autoridade no Canteiro de Obras")
    st.write("""
    Com mais de **40 anos de experiência**, Ademir Aparecido David traz a segurança da vivência prática 
    aliada à precisão técnica. Especialista em grandes projetos de infraestrutura e residências de alto padrão, 
    garantindo que cada detalhe respeite as normas **NBR**.
    """)

with col_contato:
    st.markdown("### 📍 Contato Direto")
    st.write("📞 (13) 99172-8599")
    st.write("✉️ contatoadconstru@gmail.com")
    url_whatsapp = "https://wa.me/5513991728599"
    st.link_button("CHAMAR NO WHATSAPP", url_whatsapp)

# --- SEÇÃO 2: SERVIÇOS (NOVA SEÇÃO) ---
st.markdown("## 🛠️ Nossos Serviços")
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown('<div class="cartao-servico"><h4>Gerenciamento</h4>Controle rigoroso de cronograma, custos e qualidade da mão de obra.</div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="cartao-servico"><h4>Assessoria Técnica</h4>Suporte especializado para pequenos e médios empreiteiros e proprietários.</div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="cartao-servico"><h4>Laudos e NBR</h4>Consultoria em manutenção predial e conformidade com normas técnicas.</div>', unsafe_allow_html=True)

# --- SEÇÃO 3: PATOLOGIABR (PARTE INFERIOR) ---
st.markdown('<div class="secao-patologia">', unsafe_allow_html=True)
st.header("🔍 PatologiaBR - Diagnóstico Técnico")
st.write("Área destinada à análise de problemas estruturais, infiltrações e patologias da construção.")

arquivo_foto = st.file_uploader("Suba aqui a foto da patologia para análise", type=["jpg", "png", "jpeg"])

if arquivo_foto is not None:
    st.image(arquivo_foto, caption="Imagem em análise", use_container_width=True)
    st.warning("✅ **FOTO CARREGADA!**")
    st.info("Para que eu receba o seu arquivo, clique no botão abaixo e anexe a foto manualmente no WhatsApp.")
    st.link_button("📩 ENVIAR PARA O MESTRE PELO WHATSAPP", url_whatsapp)
st.markdown('</div>', unsafe_allow_html=True)

# --- RODAPÉ ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("© 2026 AD Construções - Excelência e Tecnologia na Construção Civil.")
