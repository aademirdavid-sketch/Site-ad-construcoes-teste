import streamlit as st

# Configuração da página
st.set_page_config(page_title="AD Construções", layout="wide", page_icon="🏗️")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #25D366;
        color: white;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (CONTATO) ---
with st.sidebar:
    st.header("📍 Informações de Contato")
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

# --- CORPO DO SITE ---
st.title("🏗️ AD Construções e Gerenciamento de Obras")
st.subheader("Especialistas em Gerir Pessoas e Projetos")

# Seção Sobre
st.markdown("---")
st.header("Sobre Nós")
st.info("""
Com mais de 40 anos de experiência na construção civil, atuamos em grandes projetos de 
infraestrutura, terraplenagem, obras comerciais e residenciais de alto padrão. 
Nosso foco é a excelência técnica e a gestão eficiente de equipes e recursos.
""")

# Seção Serviços
st.header("Nossos Serviços")
c1, c2 = st.columns(2)
with c1:
    st.success("✅ **Gerenciamento de Obras:** Controle de cronograma e custos.")
    st.success("✅ **Assessoria Técnica:** Apoio especializado em obras de pequeno e médio porte.")
with c2:
    st.success("✅ **Laudos e Perícias:** Avaliações baseadas nas normas técnicas.")
    st.success("✅ **Consultoria em NBRs:** Garantia de conformidade técnica e manutenção.")

# --- ÁREA DE INTERAÇÃO DO CLIENTE ---
st.markdown("---")
st.header("📸 Acompanhamento de Obra")
st.write("Área destinada para clientes enviarem fotos do progresso da obra para análise:")

# Campo para o cliente subir a foto
arquivo_foto = st.file_uploader("Selecione a foto da sua obra", type=["jpg", "png", "jpeg"])

if arquivo_foto is not None:
    st.image(arquivo_foto, caption="Foto enviada pelo cliente", use_container_width=True)
    st.success("Foto carregada! O sistema está pronto para análise técnica.")

# Rodapé
st.markdown("---")
st.caption("© 2026 AD Construções e Gerenciamento de Obras - Atendimento especializado.")
