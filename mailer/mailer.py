import os

import requests


class Mailer:

    def mail(self, device, receiver, subject, body):
        endpoint = str.format("https://api.mailgun.net/v3/{0}/messages",
                              os.environ.get('MAILGUN_DOMAIN'))
        api_key = os.environ.get('MAILGUN_API_KEY')
        sender = str.format("{0} <postmaster@{1}>",
                            device,
                            os.environ.get('MAILGUN_DOMAIN'))
        return requests.post(endpoint, auth=('api', api_key), data={
                             "from": sender,
                             "to": [receiver],
                             "subject": subject,
                             "text": body,
                             })
