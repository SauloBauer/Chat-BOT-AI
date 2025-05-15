import os
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from time import sleep

api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot (mensagem):
    mensagem_modelo = [('system','Você é um assistente amigável, direto ao ponto e cordial, chamado BauerBot, informe seu nome no primeiro contato ')]
    mensagem_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagem_modelo)
    chain = template | chat

    return chain.invoke({}).content
print('=-='*30)
print(f"{' Bem Vindo ao BauerBot, inicie uma conversa! (Digite X para sair!) ':^80}")
print('=-='*30)
sleep(1)
mensagens = []
while True:
    pergunta = input('\nUsuario: ')
    if pergunta.upper() == 'X':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('user', resposta))
    print()
    print(f'Bot: {resposta}\n')
    sleep(2)
sleep(1)
print('\nMuito Obrigado por utilizar o AzimoBot! O histórico completo da conversa foi:\n')
sleep(1)
print(mensagens)