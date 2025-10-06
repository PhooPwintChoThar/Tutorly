import uuid
from services.tutor_service import TutorService


class TutorController:
    def __init__(self):
        self.tutor_service = TutorService()
        self.test_session = {}

    def ensure_student_session(self):
        """Ensure student has a session ID in the test session."""
        if 'student_id' not in self.test_session:
            self.test_session['student_id'] = str(uuid.uuid4())
        return self.test_session['student_id']
    
    def create_session(self):
        """Handle tutoring session creation request."""
        student_id = self.test_session.get('student_id')
        if not student_id:
            return {'error': 'Session expired'}, 401
        
        session_id = self.tutor_service.create_session(student_id)
        return {
            'session_id': session_id,
            'message': 'Tutoring session created successfully'
        }
    
 
    def send_query(self, session_id, student_query):
        
        student_id = self.test_session.get('student_id')
        if not student_id:
            return {'error': 'Session expired'}, 401
    
        if not session_id or not student_query:
            return {'error': 'invalid student_id or query'}, 400
            
        try:
        
            response=self.tutor_service.process_query(student_id, session_id, student_query)
            return {
            'response': response,
            'message': ' response processed successfully'
        }
        except Exception as e:
            return {'error': e}, 500
            
            
        
