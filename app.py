import streamlit as st
import os

# 1. Configuração da Página
st.set_page_config(
    page_title="AD Construções e Gerenciamento",
    page_icon="🏗️",
    layout="wide"
)

# 2. Estilo Visual (CSS)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .titulo-principal { color: #1E3A8A; font-size: 42px; font-weight: bold; text-align: center; }
    .subtitulo { color: #555; text-align: center; font-size: 20px; margin-bottom: 30px; }
    .cartao-servico {
        background-color: #f8f9fa;
        padding: 20px;
        border-left: 5px solid #1E3A8A;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Topo: Logo e Título
col_logo, col_tit = st.columns([1, 3])

with col_logo:
    # Nome do arquivo que você subiu por último
    nome_logo = "IMG_20260210_110844~4.png"
    
    if os.path.exists(nome_logo):
        # use_container_width=True faz a logo ocupar todo o espaço da coluna lateral
        st.image(nome_logo, use_container_width=True)
    else:
        st.warning("⚠️ Carregando logo...")
        # Ícone temporário caso o arquivo não seja lido
        st.image("https://cdn-icons-png.flaticon.com/512/4333/4333644.png", width=120)

with col_tit:
    st.markdown('<p class="titulo-principal">AD Construções e Gerenciamento</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Mestre de Obras Sênior | Técnico em Edificações</p>', unsafe_allow_html=True)

st.markdown("---")

# 4. Conteúdo Principal: Quem Somos e Contato
col_info, col_contato = st.columns([2, 1])

with col_info:
    st.markdown("### 🏗️ Autoridade no Canteiro de Obras")
    st.write(f"""
    Com mais de **40 anos de experiência**, Ademir Aparecido David traz a segurança da vivência prática 
    aliada à precisão técnica. Especialista em grandes projetos de infraestrutura e residências de alto padrão, 
    garantindo que cada detalhe respeite as normas **NBR**.
    """)
    
    st.markdown("### 🛠️ Nossos Serviços")
    
    servicos = {
        "Gerenciamento": "Implantação de projetos com rigoroso controle de cronograma, custos e qualidade.",
        "Assessoria Técnica": "Suporte especializado para pequenos e médios empreiteiros e proprietários.",
        "Laudos e NBR": "Consultoria em conformidade técnica e manutenção predial.",
        "PatologiaBR": "Diagnóstico técnico de problemas estruturais e infiltrações."
    }
    
    for titulo, desc in servicos.items():
        st.markdown(f"""
        <div class="cartao-servico">
            <strong>{titulo}</strong><br>{desc}
        </div>
        """, unsafe_allow_html=True)

with col_contato:
    st.markdown("### 📍 Contato Direto")
    st.info("📞 (13) 99172-8599")
    st.info("✉️ contatoadconstru@gmail.com")
    
    if st.button("CHAMAR NO WHATSAPP"):
        st.write("Redirecionando...")

# 5. Rodapé
st.markdown("---")
st.caption(f"© {2026} AD Construções e Gerenciamento de Obras LTDA - Tambaú/SP para o Brasil.")
