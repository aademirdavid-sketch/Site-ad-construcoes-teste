import streamlit as st
import os

# 1. Configuração de Diretrizes da Página
st.set_page_config(
    page_title="AD Construções - Gestão Técnica de Obras",
    page_icon="🏗️",
    layout="wide"
)

# 2. Identidade Visual e Estilização Acadêmica/Profissional
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    .header-inst { color: #0a1931; font-size: 38px; font-weight: 800; letter-spacing: -1px; margin-bottom: 5px; }
    .sub-inst { color: #475569; font-size: 18px; font-weight: 400; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 1px; }
    .section-title { border-bottom: 2px solid #0a1931; color: #0a1931; padding-bottom: 10px; margin-top: 30px; font-weight: bold; }
    .card {
        background-color: #fcfcfc;
        padding: 25px;
        border-radius: 4px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        height: 400%;
    }
    .label-tecnico { color: #1e40af; font-weight: 600; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho Estrutural (Logo e Identificação)
col_logo, col_tit = st.columns([1, 2])

with col_logo:
    # Vinculação do ativo de imagem
    path_imagem = "IMG_20260210_110844~4.png"
    if os.path.exists(path_imagem):
        st.image(path_imagem, use_container_width=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/4333/4333644.png", width=True)

with col_tit:
    st.markdown('<div class="header-inst">AD CONSTRUÇÃO E GERENCIAMENTO DE OBRAS</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-inst">Consultoria Técnica e Implantação de Projetos</div>', unsafe_allow_html=True)

st.write("---")

# 4. Corpo Institucional
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown('<h3 class="section-title">Excelência Operacional e Rigor Técnico</h3>', unsafe_allow_html=True)
    st.write("""
    Com trajetória consolidada de mais de quatro décadas no setor da Construção Civil, a **AD Construções** oferece 
    soluções integradas para o gerenciamento de obras, unidades industriais e infraestrutura urbana. 
    Nossa atuação é pautada pelo estrito cumprimento das Normas Regulamentadoras e pela otimização 
    processual, garantindo a conformidade técnica e a viabilidade financeira dos empreendimentos.
    """)

    st.markdown("#### Especialidades e Frentes de Atuação")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card">
            <span class="label-tecnico">Orçamento</span>
            <p>Elaboração de orçamentos detalhados, controle de insumos e gestão de contratos de mão de obra (labor-only).</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card">
            <span class="label-tecnico">PATOLOGIA DAS EDIFICAÇÕES</span>
            <p>Diagnósticos técnicos e planos de recuperação predial fundamentados em análise estrutural e ensaios normatizados.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        <div class="card">
            <span class="label-tecnico">GESTAO DE IMPLANTAÇÃO</span>
            <p>Coordenação de canteiro, logística de suprimentos e fiscalização de execução conforme projetos executivos.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card">
            <span class="label-tecnico">CONFORMIDADE NBR 5674</span>
            <p>Desenvolvimento de programas de manutenção predial preventiva e corretiva para garantia de vida útil do ativo.</p>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.markdown('<h3 class="section-title">Canais de Atendimento</h3>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown("**Corpo Técnico Responsável:**")
        st.write("Ademir David")
        st.caption("Técnico em Edificações | Mestre de Obras Sênior")
        
        st.write("---")
        
        st.markdown("**Unidade de Atendimento:**")
        st.write("📍 São Paulo / SP")
        
        st.write("---")
        
        st.markdown("**Contato Corporativo:**")
        st.markdown("📞 **(13) 99172-8590**")
        st.markdown("📧 **contatoadconstru@gmail.com**")
        
        st.write("")
        st.link_button("SOLICITAR CONSULTORIA VIA WHATSAPP", "https://wa.me/5513991728590", type="primary")

# 5. Rodapé Corporativo
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #94a3b8; font-size: 12px;">
        © 2026 AD Construções e Gerenciamento de Obras LTDA. <br>
        Foco em Performance, Segurança e Sustentabilidade de Ativos Imobiliários.
    </div>
    """, unsafe_allow_html=True)
