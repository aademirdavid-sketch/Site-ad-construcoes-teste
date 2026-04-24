import streamlit as st

# Configuração da página
st.set_page_config(page_title="AD Construções & PatologiaBR", layout="wide", page_icon="🏗️")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .instrucao-destaque {
        background-color: #fff3cd;
        color: #856404;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ffeeba;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .botao-zap {
        background-color: #25D366;
        color: white;
        padding: 20px;
        text-align: center;
        text-decoration: none;
        display: block;
        border-radius: 10px;
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("AD Construções")
    st.write("🏗️ **Mestre de Obras Sênior**")
    st.write("👥 **Especialista em Gerir Pessoas**")
    st.markdown("---")
    st.write("✉️ contatoadconstru@gmail.com")
    st.write("📞 (13) 99172-8590")
    url_whatsapp = "https://wa.me/5513991728590"
    st.link_button("Falar no WhatsApp", url_whatsapp)

# --- CONTEÚDO PRINCIPAL ---
st.title("Gerenciamento de Obras e Assessoria Técnica")
st.markdown("---")

tab1, tab2 = st.tabs(["🏗️ Gestão de Obras", "🔍 PatologiaBR (Diagnósticos)"])

with tab1:
    st.write("Foco em gestão de equipes e conformidade com as normas NBR.")

with tab2:
    st.write("Consultoria especializada em diagnóstico de patologias e manutenção predial.")

# --- ÁREA DE ENVIO DE FOTOS ---
st.markdown("---")
st.header("📸 Enviar Foto para Análise")

arquivo = st.file_uploader("Selecione a imagem da obra ou patologia", type=["jpg", "png", "jpeg"])

if arquivo is not None:
    st.image(arquivo, caption="Imagem carregada no site", use_container_width=True)
    
    # --- TEXTO EM DESTAQUE ---
    st.markdown("""
        <div class="instrucao-destaque">
            🚨 ATENÇÃO: A FOTO FOI CARREGADA NO SITE!<br>
            PARA EU RECEBER A FOTO, CLIQUE NO BOTÃO ABAIXO E, AO ABRIR O WHATSAPP, 
            <u>ANEXE A FOTO MANUALMENTE</u> NA CONVERSA.
        </div>
    """, unsafe_allow_html=True)
    
    # Mensagem personalizada
    mensagem_zap = "Olá Ademir, vi a foto no site. Estou te chamando para enviar o arquivo por aqui para análise."
    link_mensagem = f"https://wa.me/5513991728590?text={mensagem_zap.replace(' ', '%20')}"
    
    # Botão Grande
    st.markdown(f'<a href="{link_mensagem}" target="_blank" class="botao-zap">🟢 ENVIAR AVISO E FOTO PELO WHATSAPP</a>', unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.caption("© 2026 AD Construções - Tecnologia e Experiência.")
