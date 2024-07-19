import sys
import pandas as pd
import logging

log_format = "[%(name)s][%(levelname)-6s] %(message)s"
logging.basicConfig(format=log_format)
logger = logging.getLogger("describe")
logger.setLevel(logging.error)

argument = sys.argv[-1]
logger.debug("processing input file: %s", argument)

try:
    df = pd.read_csv(argument)
    print(df.describe())
except Exception :
    logger.exception("had a problem trying to read the csv file")
    
logger.info("the program continues, without issue")
