# from django.shortcuts import render
# from django.http import JsonResponse
# from django.middleware.csrf import get_token
# from datetime import datetime
# import json
# from django.views.decorators.csrf import csrf_exempt
# def index(request):
#     get_token(request)
#     return render(request, 'chatbot/chat.html')
# @csrf_exempt
# def chat(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         message = data.get('message', '').lower()
        
#         if 'user_name' not in request.session:
#             request.session['user_name'] = message
#             response = [
#                 f"Chatbot: Nice to meet you, {message}! How can I assist you today?",
#                 "Chatbot: You can ask me about 'weather', 'time', 'help','DOB' or say 'bye' to exit."
#             ]
#         else:
#             user_name = request.session['user_name']
#             if message in ["hi", "hello", "hey"]:
#                 response = ["Chatbot: Hello! How can I help you?"]
#             elif message == "weather":
#                 response = ["Chatbot: The weather is sunny with a temperature of 30°C."]
#             elif message == "time":
#                 current_time = datetime.now().strftime("%H:%M:%S")
#                 response = [f"Chatbot: The current time is {current_time}"]
#             elif message == "help":
#                 response = ["Chatbot: I can answer questions about weather, time, DOB and general help. Just ask!"]
#             elif message == "DOB":
#                 response = ["Chatbot:30th May,2001"]    
#             elif message == "bye":
#                 response = [f"Chatbot: Goodbye, {user_name}! Have a great day!"]
#                 del request.session['user_name']
#             else:
#                 response = ["Chatbot: Sorry, I didn't understand that. Can you ask something else?"]

#         return JsonResponse({'messages': response})
#     return JsonResponse({'error': 'Invalid request'}, status=400)


from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import json

# Constants
DOB = "30th May, 2001"
LOCATION = "Ekkatuthangal, Chennai"
ADDRESS = "Attur, Salem"

def index(request):
    """ Renders the chatbot HTML page """
    get_token(request)  # Ensure CSRF token is set
    return render(request, 'chatbot/index.html')

@csrf_exempt
def chat(request):
    """ Handles chatbot interactions """
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '').strip().lower()
        except (json.JSONDecodeError, AttributeError):
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        # Session handling
        if 'user_name' not in request.session:
            
            # First interaction - ask for the name
            if 'awaiting_name' not in request.session:
                request.session['awaiting_name'] = True
                response = [
                    "Chatbot: Hello! I am your virtual assistant.",
                    "Chatbot: What's your name? 😊"
                ]
            
            # Capture the user's name and start the conversation
            else:
                # Store the user's name in session
                request.session['user_name'] = message.capitalize()
                del request.session['awaiting_name']  # Remove flag
                user_name = request.session['user_name']

                response = [
                    f"Chatbot: Nice to meet you, {user_name}! How can I assist you today?",
                    "Chatbot: You can ask me about 'weather', 'time', 'help', 'DOB', 'location', 'address' or say 'bye' to exit."
                ]

        else:
            # Session already has the username
            user_name = request.session['user_name']

            # Dictionary of responses (standardized keys)
            responses = {
                "hi": [f"Chatbot: Hello {user_name}! How can I help you?"],
                "hello": [f"Chatbot: Hello {user_name}! How can I help you?"],
                "hey": [f"Chatbot: Hey {user_name}! How can I assist you?"],
                "weather": ["Chatbot: The weather is sunny with a temperature of 30°C."],
                "time": [f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}"],
                "help": [
                    "Chatbot: I can answer questions about weather, time, DOB, location, address, and general help. Just ask!"
                ],
                "dob": [f"Chatbot: {DOB}"],
                "location": [f"Chatbot: {LOCATION}"],
                "address": [f"Chatbot: {ADDRESS}"],
                "bye": [f"Chatbot: Goodbye, {user_name}! Have a great day!"]
            }

            # Check for valid messages
            if message in responses:
                response = responses[message]

                # End session on "bye"
                if message == "bye":
                    del request.session['user_name']
            else:
                response = [f"Chatbot: Sorry, {user_name}, I didn't understand that. Can you ask something else?"]

        return JsonResponse({'messages': response})

    return JsonResponse({'error': 'Invalid request'}, status=400)
