import uuid
from openai import OpenAI
from models.session import SessionManager


class TutorService:
    def __init__(self):
        self.session_manager = SessionManager()
        self.client = OpenAI(
            api_key="Your API KEY"
, 
            base_url="AI MODEL",
            default_headers={
                "HTTP-Referer": "http://localhost:3000",  
                "Tutorly": "Your DSA Tutor", 
            }
        )
        self.system_prompt = self.load_system_prompt('data/system_prompt.txt')

    def load_system_prompt(self, file_path: str) -> str:
        """Load the system prompt from file."""
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Error loading system prompt: {e}")
            return "You are a helpful tutor."

    def create_session(self, student_id: str) -> str:
        """Create a new tutoring session."""
        session_id = str(uuid.uuid4())
        self.session_manager.create_session(student_id, session_id, self.system_prompt)
        return session_id
        
    def process_query(self, student_id: str, session_id: str, query: str) -> str:
        """Process a student query and get AI response."""
        session = self.session_manager.get_session(student_id, session_id)
        if not session:
            raise ValueError("Session not found")

        # Add student query
        self.session_manager.add_message(student_id, session_id, "user", query)

        try:
            # Get AI response
            conversation = self.session_manager.get_conversation(student_id, session_id)
            
            response = self.client.chat.completions.create(
                model="deepseek/deepseek-chat-v3.1:free",  
                messages=conversation,
                temperature=0.5,
                max_tokens=700
            )
            
            ai_message = response.choices[0].message.content
            
            # Add AI response to session history
            self.session_manager.add_message(student_id, session_id, "assistant", ai_message)
            
            return ai_message
            
        except Exception as e:
            raise RuntimeError(f"Error getting AI response: {str(e)}")
