from services.tutor_service import TutorService


tutor_service = TutorService()


student_id = "student123"


session_id = tutor_service.create_session(student_id)
print(f"Tutoring session created with ID: {session_id}")
from controllers.tutor_controller import TutorController

# Initialize the TutorController
tutor_controller = TutorController()

# Ensure a student session for testing
student_id = tutor_controller.ensure_student_session()

# Create a new tutoring session
session_response = tutor_controller.create_session()

# Handle session creation response
if 'error' in session_response:
    print(f"Error: {session_response['error']}")
else:
    # Extract session_id from the response
    session_id = session_response['session_id']
    
    # Example query handling
    student_query = "Can you explain the concept of inheritance in programming?"

    # TODO: Send the student query and get the response
    reply=tutor_controller.send_query(session_id, student_query)

    # TODO: Check if there is an error in the response
        # TODO: If there is an error, print the error message
    if isinstance(reply, tuple):
        print(reply[0].get('error')+" occured")
    # TODO: If there is no error, print the tutor's response
    else:
        print(reply.get('response'))
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
