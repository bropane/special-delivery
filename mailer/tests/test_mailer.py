import pytest

from ..mailer import Mailer


class TestMailer:

    def test_mail(self):
        mailer = Mailer()
        response = mailer.mail("penrose1",
                               "taylor.sloan2@gmail.com",
                               "Hello World",
                               "Test Email")
        assert response.status_code == 200, ("Should accept response from " +
                                             "Mailgun")
