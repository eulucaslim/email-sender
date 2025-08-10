from dotenv import load_dotenv
from typing import Final
import logging
import os

# Configure basic logging (optional, but good for quick starts)
logging.basicConfig(level=logging.INFO, format=(
    '%(asctime)s - %(levelname)s - %(message)s')
)
# Get a logger instance
logger = logging.getLogger(__name__)

load_dotenv()

SERVER_EMAIL: Final[str] = os.getenv('SERVER_EMAIL')
PASSWORD_EMAIL: Final[str] = os.getenv('PASSWORD_EMAIL')
SMTP_SERVER: Final[str] = os.getenv('SMTP_SERVER')
SMTP_PORT: Final[int] = os.getenv('SMTP_PORT')
EMAIL_PORT: Final[int] = os.getenv('EMAIL_PORT')
