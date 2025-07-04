import logging
class LogingError(Exception):
    """Custom exception for logging errors."""
    pass    
logging.basicConfig(filename='custom_logfile.log',level=logging.ERROR)
username=input("Enter your username: ")
if username != "admin":
    error =LogingError("Invalid username provided.")
    logging.error("An error occurred: %s", error)
    raise error
else:
    print("Welcome, admin!")