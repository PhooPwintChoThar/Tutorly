from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="deepseek_api_key", base_url="https://api.deepseek.com")

#simple prompt
prompt = "Can you tell me an engineering joke?"

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=100 #limit the response whether it finishes or not
    temperature=0.2 #low temperature -> precise, high temperature->creative
    presence_penalty = 0.8, #higher value penaltizes the repeating words in conversation
    frequency_penalty=0.9,#higher value penaltizes the repeating words in response
) 

# Extract response from  API result
reply = response.choices[0].message.content.strip()

# Display the results
print("Query:", prompt)
print("Answer:", reply)