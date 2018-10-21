# -*- coding: utf-8 -*-
from collections import namedtuple

from consul import Consul
from consul.base import CB

from config import Config

ConsulService = namedtuple("ConsulService", [
    'service', 'nodes', "status", "apidoc"
])

ConsulServiceNode = namedtuple("ConsulServiceNode", [
    'id', 'address', 'port', 'meta', 'tags', 'status', 'checks'
])


def get_services_info():
    consul = Consul(host=Config.CONSUL_HOST, port=Config.CONSUL_PORT)
    services = list(set([s.get("Service") for s in consul.agent.services().values()]))
    services.sort()
    info = []

    for service in services:
        health = consul.health.service(service)[1]
        nodes = []

        for h in health:
            checks = h['Checks']
            not_passing = [c for c in checks if c["Status"] != "passing"]
            status = "passing" if len(not_passing) == 0 else "warning"
            nodes.append(ConsulServiceNode(
                id=h["Service"]["ID"],
                address=h['Service']['Address'],
                port=h['Service']['Port'],
                meta=h['Service']['Meta'],
                tags=h['Service']['Tags'],
                checks=h['Checks'],
                status=status
            ))

        service_node_passing = [n for n in nodes if n.status == 'passing']
        service_status = "passing" if len(service_node_passing) == len(nodes) else "warning"
        api_doc = f"http://{service_node_passing[0].address}:{service_node_passing[0].port}" \
                  f"{service_node_passing[0].meta.get('apidoc', '/apidocs') if service_node_passing[0].meta else '/apidocs'}" if len(
            service_node_passing) > 0 else ""
        info.append(ConsulService(service=service, nodes=nodes, status=service_status, apidoc=api_doc))
    return info


def deregister_service(service_id):
    consul = Consul(host=Config.CONSUL_HOST, port=Config.CONSUL_PORT)
    return consul.http.put(CB.bool(), '/v1/agent/service/deregister/%s' % service_id)