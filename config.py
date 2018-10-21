# -*- coding: utf-8 -*-
import os


class Config(object):
    CORS_ORIGINS = "*"

    CONSUL_HOST = "192.168.1.10"
    CONSUL_PORT = "8500"

    CONSUL_UI_PATH = "http://192.168.1.10:8500/ui"
