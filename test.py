from openai import OpenAI
import uuid #generate unique identifier for each tutoring session

# Initialize the OpenAI client
client = OpenAI(api_key="deepseek_api_key", base_url="https://api.deepseek.com")

chat_sessions={}

system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}


def generate_chat_id():
    id=str(uuid.uuid4())
    chat_sessions[id]=[]
    chat_sessions[id].append(system_prompt)
    return id

def send_message(chat_id, user_message):
    if chat_id not in chat_sessions:
        raise ValueError("Chat session not found!")
    
   
    chat_sessions[chat_id].append({"role": "user", "content": user_message})
 
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=chat_sessions[chat_id]
    ).choices[0].message.content.strip()
 
    chat_sessions[chat_id].append({"role": "assistant", "content": response})
    
    return response


first_chat=generate_chat_id()

print("Response1 : ", send_message(first_chat, "What are the benefits of your product?"))

print("Response2 : ", send_message(first_chat, "Any other benefit?"))


second_chat=generate_chat_id()

print("Response1 : ", send_message(second_chat, "What are the cons of your product?"))

print("Response2 : ", send_message(first_chat, "Do you have solutions for them?"))

for s in chat_sessions:
    print(f"Session id : {s}")
    for m in chat_sessions[s]:
        print(m["role"], ":", m["content"])