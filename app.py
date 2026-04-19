import os
from groq import Groq
from pyfiglet import figlet_format
from colorama import Fore, init
from dotenv import load_dotenv

load_dotenv()

init(autoreset=True)

print(Fore.RED + figlet_format("ChatLib"))

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)



def chat_groq(prompt):
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Você é um assistente útil e direto."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant",
        temperature=0.7,
        max_tokens=1024
    )
    return completion.choices[0].message.content



if __name__ == "__main__":
    try:
        while True:
            user_input = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")

            if user_input.lower() == "sair":
                print("Encerrando o chat. Até mais!")
                break

            response = chat_groq(user_input)
            print(Fore.GREEN + f"\nResposta: {response}")

    except KeyboardInterrupt:
        print("\nEncerrado manualmente (Ctrl + C). Até mais!")
        