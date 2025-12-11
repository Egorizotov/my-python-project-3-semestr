from contextlib import contextmanager
import time


@contextmanager
def cm_timer_1():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print("time = " + str(end - start))


class cm_timer_2:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print("time = " + str(self.end - self.start))
