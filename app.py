import streamlit as st

# Configuração da página
st.set_page_config(page_title="AD Construções & PatologiaBR", layout="wide", page_icon="🏗️")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        background-color: #25D366;
        color: white;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 12px;
    }
    .stButton>button:hover { background-color: #128C7E; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("AD Construções")
    st.subheader("Ademir Aparecido David")
    st.write("🏗️ **Mestre de Obras Sênior**")
    st.write("📐 **Técnico em Edificações**")
    st.write("👥 **Especialista em Gerir Pessoas**")
    
    st.markdown("---")
    st.header("📍 Contato")
    st.write("✉️ contatoadconstru@gmail.com")
    st.write("📞 (13) 99172-8590")
    
    # Link do WhatsApp principal
    url_whatsapp = "https://wa.me/5513991728590"
    st.link_button("Falar no WhatsApp", url_whatsapp)
    
    st.markdown("---")
    st.caption("São Paulo - SP | 40+ anos de experiência")

# --- CONTEÚDO PRINCIPAL ---
st.title("Gerenciamento de Obras e Assessoria Técnica")
st.markdown("---")

# Seção de Serviços em Abas
tab1, tab2 = st.tabs(["🏗️ Gestão de Obras", "🔍 PatologiaBR (Diagnósticos)"])

with tab1:
    st.write("""
    ### Experiência de Canteiro e Gestão Profissional
    Atuamos em grandes projetos de infraestrutura e obras residenciais de alto padrão, 
    focando na gestão eficiente de equipes e conformidade com as normas NBR.
    """)

with tab2:
    st.write("""
    ### Tecnologia Aplicada à Engenharia
    Consultoria especializada em diagnóstico de patologias e manutenção predial 
    conforme a **NBR 5674**.
    """)

# --- ÁREA DE ENVIO DE FOTOS (O SEU PEDIDO) ---
st.markdown("---")
st.header("📸 Enviar Foto para Análise")
st.warning("⚠️ **Instrução:** Após selecionar a foto abaixo, ela aparecerá na tela. Em seguida, clique no botão verde para me enviar o aviso pelo WhatsApp.")

# Campo de upload
arquivo = st.file_uploader("Escolha a imagem da obra ou patologia", type=["jpg", "png", "jpeg"])

if arquivo is not None:
    st.image(arquivo, caption="Imagem carregada", use_container_width=True)
    st.success("✅ Foto carregada no site!")
    
    # Mensagem personalizada para o WhatsApp
    mensagem_zap = "Olá Ademir, acabei de carregar uma foto no seu site para análise técnica. Vou te enviar a imagem aqui agora."
    link_mensagem = f"https://wa.me/5513991728590?text={mensagem_zap.replace(' ', '%20')}"
    
    st.markdown(f"""
        <a href="{link_mensagem}" target="_blank">
            <button style="width:100%; background-color:#25D366; color:white; border:none; padding:15px; border-radius:10px; font-weight:bold; cursor:pointer;">
                🟢 CLIQUE AQUI PARA ME ENVIAR A FOTO PELO WHATSAPP
            </button>
        </a>
    """, unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.caption("© 2026 AD Construções - Tecnologia e Experiência.")
