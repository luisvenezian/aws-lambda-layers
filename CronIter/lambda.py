import json
import logging
from croniter import croniter
from datetime import datetime



root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)
logger = logging.getLogger()



def lambda_handler(event, context):
    # TODO implement
    today = datetime.now()
    cron  = "0 0 * * wed"
    iter  = croniter(cron, today)  # Every wednesday
    
    # Check if a cron logic matches today
    if iter.get_prev(datetime).date() == today.date():
        logger.info(".... Triggered!") 
    else:
        logger.info(f"{cron} not triggered!")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
