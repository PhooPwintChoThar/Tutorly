from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="deepseek_api_key", base_url="https://api.deepseek.com")


system_prompt = "You are a skillful software engineer who ca solve all bugs and errors."
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What's your favorite type of pizza?"},
]


response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=conversation,
    max_tokens=200, #limit the response whether it finishes or not
    temperature=0.2, #low temperature -> precise, high temperature->creative
    presence_penalty = 0.8, #higher value penaltizes the repeating words in conversation
    frequency_penalty=0.9,#higher value penaltizes the repeating words in response
) 

# Extract response from  API result
reply = response.choices[0].message.content.strip()

print("Answer:", reply)