import time
import signal
import schedule
from functools import wraps

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
    def schedule_email(self,function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            while self.quantity > 0:
                try:
                    with Timeout(30):
                        function()
                        self.quantity -= 1
                        time.sleep(self.delay)
                except Timeout.Timeout:
                    return "There was a timeout error"
                except:
                    return "There was some other error"
        return wrapper
