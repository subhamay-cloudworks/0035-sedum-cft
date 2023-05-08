import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # TODO implement
    
    case_id = event["CaseID"]
    status = event["Status"]
    message = message = event["Message"]
    logger.info(f"{context.function_name} :: case_id = {case_id}; status = {status}; message = {message}")
    message = f"{message} closed."
    
    return {
        'CaseID': case_id,
        'Status': status,
        'Message': json.dumps(message)
    }
