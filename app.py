import streamlit as st

# Configuração da página
st.set_page_config(page_title="AD Construções", layout="wide")

# Cabeçalho
st.title("🏗️ AD Construções e Gerenciamento de Obras")
st.subheader("Especialistas em Gerir Pessoas e Projetos")

# Sobre a Empresa
st.markdown("---")
st.header("Sobre Nós")
st.write("""
Com mais de 40 anos de experiência na construção civil, atuamos em grandes projetos de 
infraestrutura, obras comerciais e residenciais de alto padrão. Nosso foco é a 
excelência técnica e a gestão eficiente.
""")

# Serviços
st.header("Nossos Serviços")
col1, col2 = st.columns(2)
with col1:
    st.info("✅ Gerenciamento de Obras")
    st.info("✅ Assessoria Técnica")
with col2:
    st.info("✅ Laudos e Perícias")
    st.info("✅ Consultoria em NBRs")

# Contato
st.markdown("---")
st.write("📍 São Paulo - SP")
