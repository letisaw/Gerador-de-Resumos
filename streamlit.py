import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyD4GWsagJRszkPWbRw-Qajm3P_rnZDnwFA"
genai.configure(api_key="AIzaSyD4GWsagJRszkPWbRw-Qajm3P_rnZDnwFA")

# Inicializar o modelo
model = genai.GenerativeModel("gemini-2.0-flash")

def gerar_resumo(texto):
    prompt = f"Resuma o seguinte texto:\n\n{texto}"
    response = model.generate_content(prompt)
    return response.text

# Configuração do Streamlit
st.title("Gerador de Resumos com Google Gemini")
st.subheader("Insira um texto e obtenha um resumo gerado pela IA")

user_text = st.text_area("Digite ou cole seu texto:")

if st.button("Gerar Resumo"):
    if user_text:
        resumo = gerar_resumo(user_text)
        st.write("**Resumo:**")
        st.write(resumo)
    else:
        st.warning("Por favor, insira um texto para gerar um resumo.")

