# config logger
import logging
import os
import sys
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)