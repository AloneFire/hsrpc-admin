# -*- coding: utf-8 -*-
import builtins


class Extlist(list):
    def length(self):
        return self.__len__()

    def first(self, default_value=None):
        return self[0] if self else default_value

    def where(self, condition):
        return Extlist(filter(condition, self))

    def select(self, condition=lambda x: x):
        return Extlist(map(condition, self))

    def order_by(self, sorted_func=None, sorted_key_func=None, reverse=False):
        return Extlist(sorted(self, cmp=sorted_func, key=sorted_key_func, reverse=reverse))

    def group_by(self, keyfunc):
        rel = {}
        for item in self:
            if keyfunc(item) not in rel:
                rel[keyfunc(item)] = []

            rel[keyfunc(item)].append(item)
        return rel

    @staticmethod
    def use_extlist():
        builtins.list = Extlist
