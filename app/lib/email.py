from app.config.settings import SMTP_SERVER, SERVER_EMAIL, SMTP_PORT, PASSWORD_EMAIL
from app.config.settings import logger
from app.models.payload import Payload
from email.message import EmailMessage
import smtplib
import ssl


class Email(object):

	def __init__(self, payload: Payload):
		self.payload = payload
		self.admin = SERVER_EMAIL
		self.password = PASSWORD_EMAIL
		self.msg = EmailMessage()
		self.logger = logger

	def send(self) -> bool | None:
		self.msg['From'] = self.payload.from_msg
		self.msg['To'] = ', '.join(self.payload.to_msg)
		self.msg['Subject'] = self.payload.subject

		self.msg.set_content(self.payload.body)
		safe = ssl.create_default_context()
		try:
			with smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT, context=safe) as smtp:
				smtp.login(self.admin, self.password)
				self.logger.debug("Login Sucessfully!")
				smtp.sendmail(
					from_addr=self.payload.from_msg,
					to_addrs=self.payload.to_msg,
					msg=self.msg.as_string()
				)
			self.logger.debug("Email Sent Sucessfully!")
			return True

		except Exception as e:
			self.logger.exception(f"Error: {str(e)}")
			raise


