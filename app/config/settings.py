from dotenv import load_dotenv
from typing import Final
import os

SERVER_EMAIL: Final[str] = os.getenv('SERVER_EMAIL')
PASSWORD_EMAIL: Final[str] = os.getenv('PASSWORD_EMAIL')
SMTP_SERVER: Final[str] = os.getenv('SMTP_SERVER')
SMTP_PORT: Final[int] = os.getenv('SMTP_PORT')