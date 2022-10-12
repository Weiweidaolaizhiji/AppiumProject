import logging


def handle_black(func):
    def wapper(*args,**kwargs):
        func(*args,**kwargs)
        logging.INFO(func.__name__)
        # print("装饰器")
    return wapper