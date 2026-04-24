import streamlit as st

# Configuração da página
st.set_page_config(page_title="AD Construções & PatologiaBR", layout="wide", page_icon="🏗️")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .stButton>button {
        background-color: #25D366;
        color: white;
        border-radius: 12px;
        width: 100%;
        font-weight: bold;
    }
    .main-header {
        color: #1E3A8A;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (IDENTIDADE E CONTACTO) ---
with st.sidebar:
    st.image("https://www.gstatic.com/images/branding/product/2x/contacts_96dp.png", width=100) # Espaço para o seu logo
    st.header("Contacto Profissional")
    st.write("✉️ **Email:**")
    st.write("contatoadconstru@gmail.com")
    
    st.write("📞 **Telefone:**")
    st.write("(13) 99172-8599")
    
    st.markdown("---")
    # Link direto para o WhatsApp
    url_whatsapp = "https://wa.me/5513991728599"
    st.link_button("Falar no WhatsApp", url_whatsapp)
    
    st.markdown("---")
    st.write("🏠 São Paulo - SP")
    st.caption("Mestre de Obras Sênior & Técnico em Edificações")

# --- CORPO PRINCIPAL ---
st.title("🏗️ AD Construções e Gerenciamento de Obras")
st.subheader("Especialista em Gerir Pessoas e Projetos")

# Resumo Profissional
st.markdown("---")
st.header("Experiência e Autoridade")
st.info("""
Com mais de 40 anos de trajetória na Construção Civil, atuamos na gestão de grandes projetos 
de infraestrutura, terraplenagem e obras residenciais de alto padrão. Unimos a experiência de 
canteiro com a tecnologia para entregar resultados seguros e eficientes.
""")

# Áreas de Atuação
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📋 Gestão e Consultoria")
    st.write("- Gerenciamento de Obras Comerciais e Residenciais")
    st.write("- Assessoria Técnica para Pequeno e Médio Porte")
    st.write("- Conformidade com Normas Técnicas (NBR)")

with col2:
    st.markdown("### 🔍 Diagnóstico e Tecnologia")
    st.write("- Análise de Patologias nas Edificações")
    st.write("- Laudos de Manutenção (NBR 5674)")
    st.write("- Certificação de Mão de Obra")

# --- INTEGRAÇÃO PATOLOGIABR ---
st.markdown("---")
st.header("📸 Área de Diagnóstico - PatologiaBR")
st.write("Utilize a nossa ferramenta de análise técnica. Suba uma foto para identificação de possíveis patologias:")

# Upload de foto para análise
arquivo_foto = st.file_uploader("Submeter imagem para análise técnica", type=["jpg", "png", "jpeg"])

if arquivo_foto is not None:
    st.image(arquivo_foto, caption="Imagem submetida para análise", use_container_width=True)
    st.success("Imagem carregada com sucesso. A análise técnica via PatologiaBR está pronta para processamento.")
    st.write("ℹ️ *Esta funcionalidade utiliza inteligência de dados para suporte em diagnósticos estruturais.*")

# Rodapé
st.markdown("---")
st.caption("© 2026 AD Construções - Tecnologia aplicada à Construção Civil.")
