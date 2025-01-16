This project is a simple Django-based chat application that allows users to sign up, log in, and chat with a bot. The bot replies with a basic echo response, repeating whatever message the user sends.

Features:
User authentication (Sign Up, Log In, and Log Out)
Simple chatbot functionality (echoing the user's message)
Static file management for CSS and images
Basic routing and templates
Clone the repository:
git clone https://github.com/your-username/django-chat-project.git
Navigate to the project directory:
cd django-chat-project
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt
Run migrations to set up the database:
python manage.py migrate
Run the development server:
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/ to view the application.

