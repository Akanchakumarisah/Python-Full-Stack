import logging
# Configure the logging
logging.basicConfig(
    filename='logfile.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
try:
    # Simulate a division by zero error
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Attempted to divide by zero", exc_info=True)
    print("An error occurred. Check logfile.log for details.")
else:   
    logging.info("Division successful, result: %s", result)
    print("Division successful, result:", result)
finally:
    logging.info("Execution completed.")
    print("Execution completed. Check logfile.log for details.")