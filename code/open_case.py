import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    
    case_id = event["CaseID"]
    logger.info(f"{context.function_name} :: case_id = {case_id}") 
    
    return {
        'CaseID': case_id,
        'Message': json.dumps(f'Case {case_id} : opened...')
    }

