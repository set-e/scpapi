from . import Resource


class Subnet(Resource):
    def list(self, query: dict = None):
        self.client.set_method("GET")
        self.client.set_path('/subnet/v2/subnets')
        return self.client.call_api(query=query)

    def detail(self, subnet_id: str):
        self.client.set_method("GET")
        self.client.set_path('/subnet/v2/subnets/{subnetId}'.format(subnetId=subnet_id))
        return self.client.call_api()

    def create(self, body: dict = None):
        self.client.set_method("POST")
        self.client.set_path('/subnet/v2/subnets')
        return self.client.call_api(body=body)
