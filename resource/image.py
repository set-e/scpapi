from . import Resource


class StandardImage(Resource):
    def list(self, query: dict = None):
        self.client.set_method("GET")
        self.client.set_path('/image/v2/standard-images')
        return self.client.call_api(query=query)
