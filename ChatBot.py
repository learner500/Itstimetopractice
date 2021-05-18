#!/usr/bin/env python
# coding: utf-8

# In[1]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# In[2]:


bot = ChatBot('weirdo', storage_adapter='chatterbot.storage.SQLStorageAdapter',input_adapter='chatterbot.input.TerminalAdapter',output_adapter='chatterbot.output.TerminalAdapter',logic_adapters=['chatterbot.logic.BestMatch'],database='./database.sqlite3')


# In[3]:


bot.set_trainer(ListTrainer)
data=open('chat_bot.txt').read()
talk=data.strip().split('\n')
bot.train(talk)


# In[ ]:


while True:
    try:
     bot_input = bot.get_response(None)
            
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

