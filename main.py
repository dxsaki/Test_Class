import os
from dotenv import load_dotenv
load_dotenv()

# Load environment variables
API_KEY = os.getenv("API_KEY")
print(API_KEY)

# def main():
#     print("Hello, Git & GitHub!")
#     print(f"Your API Key is: {API_KEY}")

# if __name__ == "__main__":
#     main()
