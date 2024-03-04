# https://medium.com/artificialis/ai-assistants-via-openai-and-hugging-face-api-332fc945837c
from dotenv import dotenv_values
from hugchat import hugchat
from hugchat.login import Login

secrets = dotenv_values('.env')
email = secrets['EMAIL']
pwd = secrets['PWD']


output = open('output.txt', 'w')

class Char_Conversation:
    def __init__(self, email, pwd):
        sign = Login(email=email, passwd=pwd)
        cookie = sign.login()
        return 
    def start_new_conversation(self, cookie):
        char_setting = open('setting.txt','r')
        system_prompt = char_setting.read()
        chatbot = hugchat.ChatBot(cookies=self.cookie)
        return chatbot.new_conversation(system_prompt=system_prompt)
    def generate_response(self, context):
        return 
        
def stop_reading():
    return 

def generate_response(prompt, email, pwd):
    sign = Login(email=email, passwd=pwd)
    cookie = sign.login()
    # create chatbot
    chatbot = hugchat.ChatBot(cookies=cookie.get_dict(), system_prompt=system_prompt)
    
    return chatbot.chat(prompt)

if __name__ == "__main__":
    korli = Char_Conversation(email=email, pwd=pwd)
    



