#program to write exception information to the log file
import logging
logging.basicConfig(filename="exceplog.txt",level=logging.INFO)
logging.info("A new request came:")
try:
    a=int(input("Enter a value::"))
    b=int(input("Enter b value:"))
    print(a/b)
except ZeroDivisionError as msg:
    print("We can not divide with zeor")
    logging.exception(msg)
except ValueError as msg:
    print("Enter only integer")
    logging.exception(msg)

logging.info("Request processing is completed:")
