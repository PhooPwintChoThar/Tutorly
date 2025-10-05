from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="deepseek_api_key", base_url="https://api.deepseek.com")

# Define a simple user message
prompt = "Describe a sunset over the ocean"

# Get response with only model and messages parameters
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[{"role": "user", "content": prompt}]
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)