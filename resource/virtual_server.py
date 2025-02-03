from . import Resource


class VirtualServer(Resource):
    def list(self, query: dict = None):
        self.client.set_method("GET")
        self.client.set_path('/virtual-server/v2/virtual-servers')
        return self.client.call_api(query=query)

    def detail(self, virtual_server_id: str):
        self.client.set_method("GET")
        self.client.set_path('/virtual-server/v3/virtual-servers/{virtualServerId}'.format(virtualServerId=virtual_server_id))
        return self.client.call_api()

    def create(self, body: dict = None):
        self.client.set_method("POST")
        self.client.set_path('/virtual-server/v4/virtual-servers')
        return self.client.call_api(body=body)

    def delete(self, virtual_server_id: str):
        self.client.set_method("DELETE")
        self.client.set_path('/virtual-server/v2/virtual-servers/{virtualServerId}'.format(virtualServerId=virtual_server_id))
        return self.client.call_api()
