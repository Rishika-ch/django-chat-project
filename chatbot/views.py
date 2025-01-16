from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def home(request):
    return render(request, 'chatbot/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'chatbot/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'chatbot/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chatbot/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# Improved chatbot function with dynamic responses
def chatbot_response(request):
    user_message = request.GET.get('message')

    if user_message:
        user_message = user_message.lower()

        if 'hello' in user_message:
            bot_response = "Hi there! How can I assist you today?"
        elif 'how are you' in user_message:
            bot_response = "I'm doing great, thank you for asking!"
        elif 'bye' in user_message:
            bot_response = "Goodbye! Have a great day ahead!"
        elif 'help' in user_message:
            bot_response = "Sure! How can I assist you? You can ask me about the services we offer."
        else:
            bot_response = f"You said: {user_message}. Let me know if you need any help."

        return JsonResponse({'response': bot_response})
    else:
        return JsonResponse({'response': "Sorry, I didn't catch that. Could you please repeat?"})
