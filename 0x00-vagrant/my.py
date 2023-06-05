import openai
openai.api_key="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"
while True:
    ask = input("chat whit me: ")
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt= ask,
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    text = response['choices'][0]['text']
    print("ChatGPT :" +text)