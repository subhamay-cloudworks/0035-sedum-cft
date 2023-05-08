import json
import logging
from random import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    
    case_id = event["CaseID"]
    message = event["Message"]
    logger.info(f"{context.function_name} :: case_id = {case_id}; message = {message}")
    
    random_int = randint(1, 100)
    logger.info(f"random_int = {random_int}")
    
    case_status = random_int % 2
    if (case_status == 0):
        message = f"{message} resolved..."
    else:
        message = f"{message} unresolved..."
        
    return {
        'CaseID': case_id,
        'Status': case_status,
        'Message': json.dumps(message)
    }
