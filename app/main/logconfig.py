import logging
from logging.config import dictConfig
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class LogSetup(object):
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app):
        debug = app.debug

        logging_config = dict(
            version=1,
            disable_existing_loggers=True,
            filters = {
                "InfoDebugOnly": {
                    "()": "app.main.logconfig.InfoDebugOnlyFilter"
                }
            },
            formatters={
                "default": {
                    "format": "[%(asctime)19s] %(name)-9s %(levelname)-8s : %(message)s (%(filename)s: %(lineno)s)",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
            },

            handlers = {
                "console": {
                    "level": "INFO",
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                },
                "email": {
                    "level": "WARNING",
                    "class": "app.main.logconfig.TlsSMTPHandler",
                    "formatter": "default",
                    "mailhost": app.config['LOG_EMAIL_MAILHOST'],
                    "fromaddr": app.config['LOG_EMAIL_FROMADDR'],
                    "toaddrs": app.config['LOG_EMAIL_TOADDRS'],
                    "subject": app.config['LOG_EMAIL_SUBJECT']
                },
                "error_file": {
                    "level": "WARNING",
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "formatter": "default",
                    "filename": app.config['LOG_FILE_PATH'] + app.config['LOG_ERROR_NAME'],
                    "when": app.config['LOG_WHEN'],
                    'interval': app.config['LOG_INTERVAL'],
                    "backupCount": app.config['LOG_BACKUP_COUNT'],
                    "delay": "True"
                },
                "info_file": {
                    "level": "DEBUG",
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "formatter": "default",
                    "filename": app.config['LOG_FILE_PATH'] + app.config['LOG_ERROR_NAME'],
                    "when": app.config['LOG_WHEN'],
                    'interval': app.config['LOG_INTERVAL'],
                    "backupCount": app.config['LOG_BACKUP_COUNT'],
                    "delay": "True"
                }
            },
            root = {
                "level": "INFO",
                "handlers": ['info_file', 'error_file', 'email'],
                "propagate":False
            },
        )

        dictConfig(logging_config)

# Gmail Support
# Might need slight adjustments for Outlook
class TlsSMTPHandler(logging.handlers.SMTPHandler): # pragma: no cover
    def emit(self, record):
        """
        Emit a record.
 
        Format the record and send it to the specified addressees.
        """
        msg = MIMEMultipart()

        msg['Subject'] = self.getSubject(record)
        msg['From'] = self.fromaddr
        toaddrs = self.toaddrs
        msg['To'] = ', '.join(toaddrs)

        text =  MIMEText(self.format(record))
        msg.attach(text)

        email = self.fromaddr
        pas = self.password
        smtp = self.mailhost
        port = self.mailport

        server = smtplib.SMTP(smtp, port)
        # Starting the server
        server.ehlo()
        server.starttls()
        server.ehlo()
        # Now we need to login
        server.login(email, pas)
        
        # sends to all recipients
        server.sendmail(email, toaddrs, msg.as_string())

        # quit the server
        server.quit()

class InfoDebugOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno <= logging.INFO