import os
from mistralai import Mistral
from API_Key import API_Key

api_key = API_Key
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

print("""===================================
   ⚡ CHIP AI SHELL v1.0 ⚡
   Shell coded by CHIP
===================================\n""")

while True:
    question = input("Enter your question: ")

    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role":"user",
                "content": question,
            },
        ]
    )

    print("\n--- AI RESPONSE ---")
    print(chat_response.choices[0].message.content)
    print("-------------------\n")


