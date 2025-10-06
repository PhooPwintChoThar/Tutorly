from services.tutor_service import TutorService


tutor_service = TutorService()


student_id = "student123"


session_id = tutor_service.create_session(student_id)
print(f"Tutoring session created with ID: {session_id}")

student_query = "In what year Rome burned down?"
print(f"Student Query: {student_query}")

try:
    ai_response = tutor_service.process_query(student_id, session_id, student_query)
    print(f"AI Response: {ai_response}")
except Exception as e:
    print(f"Error: {e}")



session2=tutor_service.create_session(student_id)

query2="In what year Korean became modern?"
print(f"session 2 Query: {query2}")

try:
    reply=tutor_service.process_query(student_id, session2, query2)
    print(f"session 2 reply: {reply}")
except Exception as e:
    print(f"Error: {e}")
