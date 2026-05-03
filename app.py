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
    .titulo-principal { color: #1E3A8A; font-size: 42px; font-weight: bold; text-align: center; margin-bottom: 0px; }
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
    # Nome do arquivo de imagem que você subiu
    nome_logo = "IMG_20260210_110844~4.png"
    
    if os.path.exists(nome_logo):
        st.image(nome_logo, use_container_width=True)
    else:
        st.warning("⚠️ Carregando logo...")
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
    aliada à precisão técnica. Especialista em grandes projetos de infraestrutura, unidades industriais 
    farmacêuticas e residências de alto padrão, garantindo que cada detalhe respeite as normas **NBR**.
    """)
    
    st.markdown("### 🛠️ Nossos Serviços")
    
    servicos = {
        "Gerenciamento de Obras": "Implantação de projetos com rigoroso controle de cronograma, custos e qualidade da mão de obra.",
        "Assessoria Técnica": "Suporte especializado para pequenos e médios empreiteiros e proprietários em obras residenciais e comerciais.",
        "Laudos e Normas": "Consultoria em manutenção predial e conformidade técnica baseada na NBR 5674 e outras normas vigentes.",
        "PatologiaBR": "Diagnóstico técnico avançado para análise de problemas estruturais e infiltrações."
    }
    
    for titulo, desc in servicos.items():
        st.markdown(f"""
        <div class="cartao-servico">
            <strong>{titulo}</strong><br>{desc}
        </div>
        """, unsafe_allow_html=True)

with col_contato:
    st.markdown("### 📍 Contato Direto")
    # NÚMERO ATUALIZADO AQUI
    st.info("📞 (13) 99172-8590")
    st.info("✉️ contatoadconstru@gmail.com")
    
    # Botão de WhatsApp com o número correto: 55 + DDD + NUMERO
    st.link_button("CHAMAR NO WHATSAPP", "https://wa.me/5513991728590")

# 5. Rodapé
st.markdown("---")
st.caption("© 2026 AD Construções e Gerenciamento de Obras LTDA. Especialista em Gerir Pessoas e Projetos.")
