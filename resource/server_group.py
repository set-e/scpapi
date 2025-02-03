from . import Resource


class ServerGroup(Resource):
    def list(self, query: dict = None):
        self.client.set_method("GET")
        self.client.set_path('/server-group/v2/server-groups')
        return self.client.call_api(query=query)

    def detail(self, server_group_id: str):
        self.client.set_method("GET")
        self.client.set_path('/server-group/v2/server-groups/{serverGroupId}'.format(serverGroupId=server_group_id))
        return self.client.call_api()

    def create(self, body: dict = None):
        self.client.set_method("POST")
        self.client.set_path('/server-group/v2/server-groups')
        return self.client.call_api(body=body)

    def delete(self, server_group_id: str):
        self.client.set_method("DELETE")
        self.client.set_path('/server-group/v2/server-groups/{serverGroupId}'.format(serverGroupId=server_group_id))
        return self.client.call_api()
