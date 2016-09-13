import message

sendMessage = message.Message(name = 'Send message')
reciveMessage = message.Message(name = 'Recive message')

sendMessage.start()
reciveMessage.start()