import streamlit as st
import os

# 1. Configuração de Diretrizes da Página
st.set_page_config(
    page_title="AD Construções - Gestão Técnica de Ativos e Obras",
    page_icon="🏗️",
    layout="centered" 
)

# 2. Identidade Visual e Estilização Profissional
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    
    /* Títulos e Textos */
    .header-inst { color: #0a1931; font-size: clamp(24px, 5vw, 38px); font-weight: 800; letter-spacing: -1px; text-align: center; margin-top: 20px; }
    .sub-inst { color: #475569; font-size: 16px; font-weight: 400; text-align: center; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 40px; }
    .section-title { border-bottom: 2px solid #0a1931; color: #0a1931; padding-bottom: 10px; margin-top: 40px; font-weight: bold; text-align: center; }
    
    /* Cartões de Serviço */
    .card {
        background-color: #fcfcfc;
        padding: 25px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .label-tecnico { color: #1e40af; font-weight: 700; font-size: 14px; text-transform: uppercase; display: block; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho Centralizado com Logo 50% Maior
# Ajustamos as proporções de [1, 2, 1] para [0.5, 3, 0.5] para expandir a área da imagem
col_space1, col_logo, col_space2 = st.columns([0.5, 3, 0.5])
with col_logo:
    path_imagem = "IMG_20260210_110844~4.png"
    if os.path.exists(path_imagem):
        # O use_container_width preenche a nova área maior da coluna
        st.image(path_imagem, use_container_width=True)
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/4333/4333644.png", width=250)

st.markdown('<div class="header-inst">AD CONSTRUÇÕES & GERENCIAMENTO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-inst">Consultoria Técnica e Implantação de Projetos de Engenharia</div>', unsafe_allow_html=True)

# 4. Corpo Institucional - Coluna Única
st.markdown('<h3 class="section-title">Excelência Operacional e Rigor Técnico</h3>', unsafe_allow_html=True)

st.write("") 
st.write("""
A **AD Construções** consolida mais de quatro décadas de expertise no setor da Construção Civil, oferecendo soluções de alta 
performance para o gerenciamento de ativos imobiliários, unidades industriais e infraestrutura urbana. 
Nossa metodologia é fundamentada no estrito cumprimento das Normas Brasileiras Regulamentadoras (NBR), 
garantindo a integridade técnica, segurança e viabilidade econômica em todas as fases do empreendimento.
""")

st.markdown("#### Portfólio de Especialidades")

servicos = [
    {
        "label": "Engenharia de Custos e Contratos",
        "desc": "Elaboração de orçamentos analíticos, gestão de suprimentos e controle rigoroso de contratos de mão de obra."
    },
    {
        "label": "Gestão de Implantação e Canteiro",
        "desc": "Coordenação logística, fiscalização de campo e garantia da execução fiel aos projetos executivos."
    },
    {
        "label": "Patologia das Edificações",
        "desc": "Diagnósticos técnicos, laudos periciais e projetos de recuperação predial baseados em ensaios normatizados."
    },
    {
        "label": "Conformidade Normativa (NBR 5674)",
        "desc": "Desenvolvimento e gestão de planos de manutenção preventiva para maximização da vida útil dos ativos."
    }
]

for s in servicos:
    st.markdown(f"""
    <div class="card">
        <span class="label-tecnico">{s['label']}</span>
        <p style="margin:0;">{s['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

# 5. Seção de Contato Centralizada
st.markdown('<h3 class="section-title">Canais de Atendimento Corporativo</h3>', unsafe_allow_html=True)

st.write("")
col_c1, col_c2, col_c3 = st.columns([0.1, 1, 0.1]) 
with col_c2:
    st.markdown("""
    <div style="text-align: center; border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px;">
        <p><strong>Responsável Técnico:</strong> Ademir Aparecido David</p>
        <p style="font-size: 14px; color: #64748b;">Mestre de Obras Sênior | Técnico em Edificações</p>
        <p>📍 Unidade de Operação: São Paulo / SP</p>
        <p style="font-size: 18px; color: #0a1931; font-weight: bold;">📞 (13) 99172-8590</p>
        <p style="color: #1e40af;">contatoadconstru@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.link_button("SOLICITAR CONSULTORIA VIA WHATSAPP", "https://wa.me/5513991728590", type="primary", use_container_width=True)

# 6. Rodapé Corporativo
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #94a3b8; font-size: 12px; padding-bottom: 30px;">
        © 2026 AD Construções e Gerenciamento de Obras LTDA. <br>
        Foco em Performance, Segurança e Sustentabilidade de Ativos Imobiliários.
    </div>
    """, unsafe_allow_html=True)
