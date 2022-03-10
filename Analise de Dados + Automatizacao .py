#!/usr/bin/env python
# coding: utf-8

# In[36]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install plotly.express')


# <h2> Exercicio </h2>
# <p> Básicamente, uma empresa está tendo prejuizos em cancelamentos inesperados de seus clientes, crie gráficos usando a tabela e desenvolva conclusões sobre as perdas lucrativas. </p>

# In[2]:


import pandas as pd 
import plotly.express as px 
# exportar a base de dados para o python (jupyter)


tabela = pd.read_csv(r"C:\Users\giova\OneDrive\Área de Trabalho\Aula 2 - Telecom\telecom_users.csv")
tabela = tabela.drop(["IDCliente", "Unnamed: 0", "Genero"], axis=1)
display(tabela)


# <h2> Passo 2 - tratamento de dados <h2>

# In[3]:


# analisar se o python le corretamente os dados
print(tabela.info())


# passar o valor para numerico
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# verificar alguma coluna vazia
tabela = tabela.dropna(how="all", axis=1)
# verificar alguma linha vazia
tabela = tabela.dropna(how="any", axis=0)


#  <h3> Passo 3 - Analise Geral </h3>

# In[4]:


# consultar clientes que cancelaram e que nao cancelaram
print(tabela["Churn"].value_counts())
# consultar % dos clientes que cancelaram e que nao cancelaram
print(tabela["Churn"].value_counts(normalize="True").map("{:.1%}".format))


# In[ ]:





# <h2>Passo 4 - Analise Detalhada </h2>

# In[5]:


for colunas in tabela.columns:
    grafico = px.histogram(tabela, x=colunas, color="Churn")
    grafico.show()


# <h3> Conclusoes </h3>
# 

# - Clientes cancelam nos primeiros meses
#     - Problemas na entrada
#     - Problemas na retenção de clientes
# 
# - Pessoas com familias na mesma operadora tem menos chance de cancelar 
# 
# - Quantos mais serviços ele tem, menor a chance de cancelar 
# 
# - Algum problema no serviço de fibra
#     - A taxa de cancelamento na fibra está maior
# 
# - Contrato mensal tem muita taxa de cancelamento
#     - Descontos para plano anual ou 3 meses
#     
# - Boleto taxa alta
#     - Desconto nas outras formas de pagamento

# <h2> Passo 5 - Envio de Email </h2>
# <h4> 5.1 - Instalacao pyautogui - pyperclip </h4>

# In[19]:


get_ipython().system('pip install pyautogui')
get_ipython().system('pip install pyperclip')
import time


# <h4> 5.2 - Automatizacao </h4>

# In[33]:


#import
import pyautogui
import pyperclip


conclusao = f'''
 Clientes cancelam nos primeiros meses
        - Problemas na entrada
        - Problemas na retenção de clientes

 Pessoas com familias na mesma operadora tem menos chance de cancelar 

 Quantos mais serviços ele tem, menor a chance de cancelar 

 Algum problema no serviço de fibra
        - A taxa de cancelamento na fibra está maior

 Contrato mensal tem muita taxa de cancelamento
        - Descontos para plano anual ou 3 meses
    
 Boleto taxa alta
        - Desconto nas outras formas de pagamento
'''


pyautogui.hotkey("ctrl","t")
time.sleep(3)
pyautogui.write(r"https://outlook.live.com/mail/0/")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=152, y=167)
time.sleep(3)
pyautogui.write(r"galegod14@gmail.com")
time.sleep(4)
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(3)
pyautogui.write("conclusao analise de dados")
time.sleep(3)
pyautogui.press("tab")
time.sleep(3)
pyautogui.write(conclusao)
time.sleep(3)
pyautogui.click(x=366, y=652)
time.sleep(3)
pyautogui.hotkey("ctrl","w")


# In[ ]:





# In[29]:


time.sleep(5)
pyautogui.position(x=366, y=652)


# In[ ]:




