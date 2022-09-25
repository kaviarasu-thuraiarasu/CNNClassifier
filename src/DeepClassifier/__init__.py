import os
import sys
import logging

logging_string = "[%(asctime)s:%(levelname)s:%(module)s] : %(message)s"
log_dir = "logs"
log_path = os.path.join(log_dir,"Running_logs.log")
os.makedirs(log_path,exist_ok=True)

logging.basicConfig(level=logging.info,format=logging_string,handler=[logging.StreamHandler(sys.stdout),logging.FileHandler(log_path)])

logger = logging.getLogger("CNNCLASSIFIERLOGGER")