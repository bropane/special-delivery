class FakeMailer:

    has_mail = False

    def mail(self, device, receiver, subject, body):
        self.has_mail = True
        return self.has_mail

    def has_mailed(self):
        return self.has_mail
