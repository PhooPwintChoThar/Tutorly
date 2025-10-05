from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="deepseek_api_key", base_url="https://api.deepseek.com")

# Define a simple query to test the AI's capabilities
prompt = "Can you tell me an engineering joke?"

# Create a tutoring session query request to get the AI's explanation
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[{"role": "user", "content": prompt}]
)

# Extract the tutor's response from the API result
reply = response.choices[0].message.content.strip()

# Display the query and the tutor's explanation
print("Query:", prompt)
print("Answer:", reply)