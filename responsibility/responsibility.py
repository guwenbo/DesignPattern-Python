#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    责任链模式
"""


class Level(object):

    def __init__(self, value=None):
        self._value = value

    def __str__(self):
        return str(self.value)

    def equals(self, level):
        if isinstance(level, Level):
            return self.value == level.value
        return False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val


class Request(object):

    def __init__(self, level=None, content=''):
        self._level = level
        self._content = content

    def __str__(self):
        return "Request { level : %s , content : %s }" % (self.level, self.content)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, lev):
        self._level = lev

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, cont):
        self._content = cont


class Response(object):

    def __init__(self, message=''):
        self._message = message

    def __str__(self):
        return "Response { message : %s }" % self.message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg


class AbstractHandler(object):

    def __init__(self, level=None, next_handler=None):
        self._level = level
        self._next_handler = next_handler

    def process(self, request):
        pass

    def handle_request(self, request):
        response = None
        if self.level.equals(request.level):
            response = self.process(request)
        else:
            if self.next_handler:
                response = self.next_handler.handle_request(request)
            else:
                print("Can not handle this request %s" % request)
        return response

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, lev):
        self._level = lev

    @property
    def next_handler(self):
        return self._next_handler

    @next_handler.setter
    def next_handler(self, handler):
        self._next_handler = handler


class ConcreteHandlerA(AbstractHandler):

    def __init__(self, level=None, next_handler=None):
        super().__init__(level, next_handler)

    def process(self, request):
        print("Concrete Handler A handle the Request : %s" % request)


class ConcreteHandlerB(AbstractHandler):

    def __init__(self, level=None, next_handler=None):
        super().__init__(level, next_handler)

    def process(self, request):
        print("Concrete Handler B handle the Request : %s" % request)


if __name__ == '__main__':

    hb = ConcreteHandlerB(Level(2))

    ha = ConcreteHandlerA(Level(1), hb)

    req = Request(Level(2), "Request with Level 2")

    ha.handle_request(req)
