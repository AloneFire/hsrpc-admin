# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify
from config import Config
from ..common.consul_helper import get_services_info, deregister_service

ctl = Blueprint('ctl', __name__, template_folder='templates',
                static_folder="static")


@ctl.route("/")
def index():
    services = get_services_info()
    return render_template("index.html", services=services, consul_ui=Config.CONSUL_UI_PATH)


@ctl.route("/apidoc")
def apidoc():
    services = get_services_info()
    return render_template("apidoc.html", services=services)


@ctl.route("/service/<service_id>/deregister", methods=["POST"])
def deregister_service_node(service_id):
    rel = deregister_service(service_id)
    return jsonify({
        "status": "success" if rel else "failed"
    })
