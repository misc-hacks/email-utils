from typing import Callable, List

import smtplib
import traceback


class Server(object):
    """
    Server wraps around an SMTP SSL server.

    Args:
        user: str, the user to access the SMTP SSL server.
        token: str, the user token to access the SMTP SSL server.
        host: str, the SMTP SSL server (e.g., smtp.gmail.com).
        port: int, the SMTP SSL server port.
    """

    def __init__(self, user: str, token: str, host: str, port: int = 465) -> None:
        super().__init__()
        self._server = smtplib.SMTP_SSL(host, port)
        self._server.login(user, token)

    def close(self) -> None:
        """close closes the connection to the SMTP SSL server."""
        self._server.close()

    def _try(self, fn: Callable[[], None]) -> bool:
        """_try runs the given fn in a try-except block."""
        try:
            fn()
            return True
        except Exception:
            traceback.print_exc()
            return False

    def send_plain(self, sender: str, recipients: List[str], subject: str, text: str) -> bool:
        """send_plain sends an email in plain text.
        
        Args:
            sender: str, the email address of the sender.
            recipients: List[str], the email addresses of the recipients.
            subject: str, the email subject/title.
            text: str, the email text/body.

        Returns:
            a flag indicating whether the email has been sent successfully.
        """
        return self._try(lambda: self._send_plain(sender, recipients, subject, text))

    def _send_plain(self, sender: str, recipients: List[str], subject: str, text: str) -> None:
        """_send_plain implements send_plain."""
        message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (
            sender, ", ".join(recipients), subject, text)
        self._server.sendmail(sender, recipients, message)
