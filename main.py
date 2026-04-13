print('hello my guest')
from datetime import datetime

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("The current date and time is:")
print(f"Exact date and time: {formatted}")
