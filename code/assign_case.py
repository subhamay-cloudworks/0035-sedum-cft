import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # TODO implement
    
    case_id = event["CaseID"]
    message = message = event["Message"]
    logger.info(f"{context.function_name} :: case_id = {case_id}; message = {message}")   
    message = f"{message} assigned..."
    
    return {
        'CaseID': case_id,
        'Message': json.dumps(message)
    }
