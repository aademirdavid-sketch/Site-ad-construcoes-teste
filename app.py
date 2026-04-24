import streamlit as st

# Configuração da página
st.set_page_config(page_title="AD Construções - Diagnóstico", layout="wide")

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("AD Construções")
    st.write("📞 (13) 99172-8599")
    st.write("✉️ contatoadconstru@gmail.com")
    st.markdown("---")
    st.info("Utilize o formulário ao lado para enviar detalhes da sua obra para análise técnica.")

# --- CORPO PRINCIPAL ---
st.title("🔍 Área de Diagnóstico Técnico")
st.write("Preencha os dados abaixo para que o Mestre Ademir David possa analisar sua patologia.")

# --- FORMULÁRIO DE ENVIO ---
with st.form("formulario_analise", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        nome = st.text_input("Seu Nome ou Nome da Obra:")
        contato = st.text_input("Seu WhatsApp/Telefone:")
        
    with col2:
        categoria = st.selectbox("Tipo de problema:", 
                                ["Infiltração", "Fissura/Racha", "Revestimento Soltando", "Umidade", "Outros"])
    
    descricao = st.text_area("Descreva o que está acontecendo:")
    
    foto = st.file_uploader("Suba aqui a foto da patologia (JPG/PNG):", type=["jpg", "png", "jpeg"])
    
    botao_enviar = st.form_submit_button("Enviar para Análise Técnica")

if botao_enviar:
    if nome and contato and foto:
        st.success(f"✅ Recebido, {nome}!")
        
        # Exibição do resumo para o cliente
        st.markdown("### Resumo do Envio")
        st.write(f"**Contato:** {contato}")
        st.write(f"**Problema:** {categoria}")
        st.write(f"**Descrição:** {descricao}")
        st.image(foto, caption="Foto enviada", width=400)
        
        st.warning("⚠️ IMPORTANTE: Como estamos em fase de teste, tire um 'Print' desta tela ou envie as informações acima para o WhatsApp (13) 99172-8599 para garantir o atendimento imediato.")
    else:
        st.error("❌ Por favor, preencha o nome, contato e envie a foto.")

# Rodapé
st.markdown("---")
st.caption("© 2026 AD Construções - Sistema de Triagem de Patologias.")
