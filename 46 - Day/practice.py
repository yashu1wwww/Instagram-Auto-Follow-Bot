from dotenv import load_dotenv, dotenv_values
import os


load_dotenv()

config = dotenv_values("../.env")

print(config)


#   my code

print()
username = config['MY_USERNAME']
print(username)
