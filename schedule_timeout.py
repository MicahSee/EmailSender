import time
import signal
import schedule

class Timeout(object):
    class Timeout(Exception):
        pass

        def __init__(self,sec):
            self.sec = sec
        def __enter__(self):
            signal.signal(signal.SIGALRM, self.raise_timeout)
            signal.alarm(self.sec)
        def __exit__(self, *args):
            signal.alarm(0)
        def raise_timeout(self, *args):
            raise Timeout.Timeout()


class scheduler(object):
    def __init__(self,quantity,delay):
        self.quantity = int(quantity)
        self.delay = int(delay) * 60
    def schedule_email(self,email_object):
        while self.quantity > 0:
            try:
                with Timeout(30):
                    schedule.every(self.delay).minutes.do(email_object.send())
                    self.quantity -= 1
            except Timeout.Timeout:
                return "There was a timeout error"
            except:
                return "There was some other error"
