class PushException(Exception):
    pass


class PingError(PushException):
    def __init__(self, response):
        self.response = response
