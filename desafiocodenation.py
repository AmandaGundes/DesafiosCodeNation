
# coding: utf-8

# In[1]:


import requests
import json
import hashlib
response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=4d7c751e8bb002dab672581ec75b9eb1a19566c0')
print(response.status_code)
print(response.content)

answer = response.json()
print(answer)

with open('answer.json', 'w') as json_file:
    json.dump(answer, json_file, indent = 4)
    
text_dec = 'plans are worthless, but planning is everything. dwight d. eisenhower'

with open('answer.json', 'r') as arq:
    data = json.load(arq)
    data['decifrado'] = text_dec
with open('answer.json', 'w') as arq:
    json.dump(data, arq)

with open('answer.json', 'r') as arq:
    data = json.load(arq)
    encoding = arq.encoding

res_crip = hashlib.sha1(data['decifrado'].encode(encoding)).hexdigest()
data['resumo_criptografico'] = res_crip

with open('answer.json', 'w') as arq:
    json.dump(data, arq)


# In[13]:


answer = {'answer' : open('answer.json')}


# In[14]:


send = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=4d7c751e8bb002dab672581ec75b9eb1a19566c0', files = answer)
print(send.status_code)
print(send.content)

