import google.generativeai as genai
import os
import discord

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("生命的意義是什麼?")

print(response.text)

