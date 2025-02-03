from . import Resource


class FileStorage(Resource):
    def list(self, query: dict = None):
        self.client.set_method("GET")
        self.client.set_path('/file-storage/v3/storages')
        return self.client.call_api(query=query)

    def create(self, body: dict = None):
        self.client.set_method("POST")
        self.client.set_path('/file-storage/v4/storages')
        return self.client.call_api(body=body)

    def delete(self, file_storage_id: str):
        self.client.set_method("DELETE")
        self.client.set_path('/file-storage/v3/storages/{fileStorageId}'.format(fileStorageId=file_storage_id))
        return self.client.call_api()

    def link(self, file_storage_id: str, body: dict = None):
        self.client.set_method("PUT")
        self.client.set_path('/file-storage/v4/storages/{fileStorageId}/objects/link'.format(fileStorageId=file_storage_id))
        return self.client.call_api(body=body)
        