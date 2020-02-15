#!/usr/bin/env python
# coding: utf-8

# # Seleção Vlibras 2020

# In[12]:


import pandas as pd
import re
def read(arquivo):
    leitura = pd.read_csv(arquivo, encoding='utf-8', sep=',' )
    return leitura
def reverterString(text):
    return text[::-1]


# In[31]:


CorpusQ1 = read('corpus-q1.csv')


# In[32]:


CorpusQ1_Test = CorpusQ1


# In[33]:


CorpusQ1_Test


# ## Remover espaços duplos

# In[34]:


for dt in CorpusQ1_Test['gi']: 
    dt = re.sub('\s+', " ",dt) # remover todos os espaços duplos


# ## Remover String duplicado

# In[35]:


for dt in CorpusQ1_Test['gi']:
    dt = re.sub(r'(\w+)  \1', r'\1', dt) # remover string duplicado


# ## 1S_DAR_2S MODELO PADRÃO

# In[36]:


for dt in CorpusQ1_Test['gi']: #  1S_DAR_2S -- MODELO PADRÃO
    if(re.findall("[123][P|S]", dt)): #Caso encontre um valor que esteja fora do padrão estabelecido, realizar a alteração.
        txt = re.findall("[123][P|S]\w+", dt)
        dt = re.sub('[123][P|S]','{}'.format(reverterString(txt[0])),dt)


# ## Remover espaço _
# 

# In[37]:


for dt in CorpusQ1_Test['gi']: #remover espaço entre \w e o _
    dt = re.sub("\s_","_", dt)


# ## Adicionar espaço nos qualificadores

# In[38]:


for i in CorpusQ1_Test['gi']:
    dt = re.sub("\w+_+\w","_",dt)
    dt = re.sub("\s_","_",dt)


# ## Adicionar espaço a esquerda 1S_ DAR_3P
# 

# In[39]:


for i in CorpusQ1_Test['gi']:
    tmpregex = re.findall('[123][S|P]_|\w+_[123][S|P]',i)
    print(i)
    i = re.sub(tmpregex[0],tmpregex[0]+' ',i)
    print(i)


# ## toda palavra que vier precedida de "NÃO"

# In[40]:


for i in CorpusQ1_Test['gi']:
    tmpRegexgi = re.findall('NÃO\s', i)
    if tmpRegexgi:
        tmp = tmpRegexgi[0].replace(" ", "_")
        i = re.sub(tmpRegexgi[0], tmp, i)


# In[41]:


for i in CorpusQ1_Test['gi']:
    print(i)


# In[ ]:




