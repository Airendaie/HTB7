from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Edelmira')
trainer = ListTrainer(chatbot)
trainer.train('C:/Users/airen/Documents/htb')
greeting = input('Type something')
while True:
    request=input(greeting+':')
    if request=='Bye' or request =='bye':
        print('Edelmira: Bye')
        break
    else:
        response=chatbot.get_response(request)
        print('Edelmira:',response)
response = chatbot.get_response('I should be writing')
print(response)