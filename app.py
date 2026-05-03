import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="AD Construções e Gerenciamento",
    page_icon="🏗️",
    layout="wide"
)

# --- ESTILIZAÇÃO CUSTOMIZADA ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Verificação e exibição da Logomarca atualizada
    # Usamos 'use_container_width=True' para que ela ocupe todo o espaço da lateral
    logo_path = "IMG_20260210_110844~4.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.sidebar.error("Arquivo de logo não encontrado. Verifique o nome no GitHub.")
    
    st.markdown("---")
    st.title("Navegação")
    menu = st.radio("Selecione uma opção:", ["Início", "Serviços", "Sobre", "Contato"])

# --- CONTEÚDO PRINCIPAL ---

if menu == "Início":
    st.title("AD Construções e Gerenciamento de Obras LTDA")
    st.subheader("Soluções de engenharia com foco em qualidade e técnica.")
    st.write("""
    Bem-vindo ao portal da AD Construções. Atuamos com gerenciamento de obras residenciais 
    e comerciais, garantindo que cada etapa do projeto siga as normas técnicas vigentes.
    """)
    st.info("Utilizamos tecnologia de ponta para acompanhamento e inspeção de obras.")

elif menu == "Serviços":
    st.title("Nossos Serviços")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🏗️ Gerenciamento")
        st.write("- Implantação de projetos")
        st.write("- Gestão de equipes e cronogramas")
        st.write("- Controle de materiais e custos")
        
    with col2:
        st.write("### 🔍 Consultoria Técnica")
        [span_3](start_span)st.write("- Consultoria em Patologias de Construção[span_3](end_span)")
        [span_4](start_span)st.write("- Especialista em Recuperação Predial[span_4](end_span)")
        st.write("- Assessoria técnica para pequenas e médias obras")

elif menu == "Sobre":
    st.title("Sobre o Profissional")
    [span_5](start_span)[span_6](start_span)st.write("### Ademir Aparecido David[span_5](end_span)[span_6](end_span)")
    st.write("""
    Profissional com vasta experiência no setor da construção civil, acumulando competências 
    essenciais para o sucesso de qualquer empreendimento.
    """)
    st.markdown(f"""
    - **[span_7](start_span)Mestre de Obras Sênior / Técnico em Edificações**[span_7](end_span)
    - **[span_8](start_span)Especialista em Recuperação Predial**[span_8](end_span)
    - **[span_9](start_span)[span_10](start_span)Consultor e Construtor**[span_9](end_span)[span_10](end_span)
    - **[span_11](start_span)[span_12](start_span)Empresário em AD Gerenciamento de Obras LTDA**[span_11](end_span)[span_12](end_span)
    """)

elif menu == "Contato":
    st.title("Fale Conosco")
    st.write("Interessado em nossos serviços? Entre em contato através do formulário abaixo ou pelas redes sociais.")
    
    with st.form("contato_form"):
        nome = st.text_input("Seu Nome")
        email = st.text_input("Seu E-mail")
        mensagem = st.text_area("Como podemos ajudar?")
        submit = st.form_submit_button("Enviar Mensagem")
        
        if submit:
            st.success(f"Obrigado, {nome}! Sua mensagem foi enviada com sucesso.")

# --- RODAPÉ ---
st.markdown("---")
st.caption("© 2026 AD Construções e Gerenciamento de Obras LTDA. Todos os direitos reservados.")
