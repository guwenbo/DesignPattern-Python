#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    装饰器模式 (基于类)
"""


class Component(object):

    def operate(self):
        pass


class ConcreteComponent(Component):

    def operate(self):
        print("Do something ...")


class Decorator(Component):

    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operate(self):
        self.component.operate()


class ConcreteDecorator(Decorator):

    def __init__(self, component):
        super().__init__(component)

    def decorate(self):
        print("Decorate Component ...")

    def operate(self):
        self.decorate()
        super().operate()


if __name__ == '__main__':

    component = ConcreteComponent()

    decorator = ConcreteDecorator(component)

    decorator.operate()
