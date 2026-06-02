from groq import Groq
api_key = "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"
Client = Groq(api_key = api_key)
while True:
    prompt = input("Enter your prompt: ")
    if prompt.lower() == "exit":
        print("Exiting the chat.")
        break
    response = Client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=1024
    )
    print("AI Response:", response.choices[0].message.content)