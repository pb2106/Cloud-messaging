# Cloud Messaging Service

## Project Overview
The Cloud Messaging Service project is a chat messaging system built with Python and MongoDB. It provides a secure and user-friendly platform for real-time messaging, primarily designed for classroom communication. The system features user registration, login, text messaging, and an admin control panel for user and message management.

## Features
- User Registration and Login
- Real-time Text Messaging
- Admin Control Panel
- Secure MongoDB Cloud Database
- Graphical User Interface (GUI) using Tkinter

## Software and Hardware Requirements
### Software:
- Python 3.10.2
- MongoDB Cloud Database

### Hardware:
- Intel Core i5-1035G1 CPU @ 1.00GHz 1.20GHz
- 8GB RAM
- Windows 11 64-bit Operating System

## Libraries Used
- subprocess
- Tkinter
- Socket
- sys
- pymongo
- tabulate
- datetime
- time
- threading
- certifi

## Installation
1. Install Python 3.10.2 and ensure `pip` is installed.
2. Install the required libraries using the following command:
```bash
pip install pymongo tabulate certifi
```

## Running the Application
1. Clone the repository or download the project files.
2. Execute the main script to launch the application:
```bash
python main.py
```

## Application Structure
### Home Page:
- Register: Create a new user account.
- Login: Access the chat system with existing credentials.
- Exit: Close the application.

### Chat Window:
- Send and receive messages.
- Admin can access the control panel.

### Admin Control Panel:
- Create/Delete Collections
- View all data
- Block/Unblock users
- Delete messages

## Future Development Areas
- Implement message encryption.
- Add message editing functionality.
- Introduce online user status.
- Enhance censorship and safety features.

## References
- [Stack Overflow](https://stackoverflow.com/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/python-gui-tkinter/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)
- [Python Tkinter Documentation](https://docs.python.org/3/library/tk.html)

## Acknowledgements
Special thanks to our teachers, principal, parents, and classmates for their support and guidance.

