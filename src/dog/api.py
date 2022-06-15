from apiclient import APIClient, endpoint, paginated, retry_request
from apiclient import HeaderAuthentication,JsonResponseHandler,JsonRequestFormatter
import requests

# Extend the client for your API integration.
class DogClient(APIClient):
    def __init__(self, 
                 base_url,
                 apikey=""
                 ):
        authentication_method=HeaderAuthentication(
            token=apikey,
            parameter="apikey",
            scheme=None
            )
        super().__init__(authentication_method=authentication_method,
                       response_handler=JsonResponseHandler,
                       request_formatter=JsonRequestFormatter)
        self.authentication_method = authentication_method
        self.apikey = apikey
        self.base_url = base_url
        self.endpoint = endpoint(self.Endpoint, base_url=self.base_url)

    #external
    def get_all_externals(self) -> dict:
        return self.get(self.endpoint.externals)

    @retry_request
    def get_external(self, id: str) -> dict:
        url = self.endpoint.external.format(id=id)
        return self.get(url)

    def get_external_by_name(self, name: str) -> dict:
        url = self.endpoint.external_without_id
        return self.get(url, params = {"name": name})

    def create_external(self, json) -> dict:
        url = self.endpoint.external
        return self.post(url, data=json)

    def update_external(self, id: str, json) -> dict:
        url = self.endpoint.external.format(id=id)
        return self.put(url, data=json)

    def delete_external(self, id: str) -> dict:
        url = self.endpoint.external.format(id=id)
        return self.delete(url)
    #group
    def get_all_groups(self) -> dict:
        return self.get(self.endpoint.groups)

    @retry_request
    def get_group(self, id: str) -> dict:
        url = self.endpoint.group.format(id=id)
        return self.get(url)

    def get_group_by_name(self, name: str) -> dict:
        url = self.endpoint.group_without_id
        return self.get(url, params = {"name": name})

    def create_group(self, json) -> dict:
        url = self.endpoint.group
        return self.post(url, data=json)

    def update_group(self, id: str, json) -> dict:
        url = self.endpoint.group.format(id=id)
        return self.put(url, data=json)

    def delete_group(self, id: str) -> dict:
        url = self.endpoint.group.format(id=id)
        return self.delete(url)

    #link
    def get_all_links(self) -> dict:
        return self.get(self.endpoint.links)

    @retry_request
    def get_link(self, id: str) -> dict:
        url = self.endpoint.link.format(id=id)
        return self.get(url)

    def get_link_by_name(self, name: str) -> dict:
        url = self.endpoint.link_without_id
        return self.get(url, params = {"name": name})

    def create_link(self, json) -> dict:
        url = self.endpoint.link
        return self.post(url, data=json)

    def update_link(self, id: str, json) -> dict:
        url = self.endpoint.link.format(id=id)
        return self.put(url, data=json)

    def delete_link(self, id: str) -> dict:
        url = self.endpoint.link.format(id=id)
        return self.delete(url)

    #host
    def get_all_hosts(self) -> dict:
        return self.get(self.endpoint.hosts)

    @retry_request
    def get_host(self, id: str) -> dict:
        url = self.endpoint.host.format(id=id)
        return self.get(url)

    def get_host_by_name(self, name: str) -> dict:
        url = self.endpoint.host_without_id
        return self.get(url, params = {"name": name})

    def create_host(self, json) -> dict:
        url = self.endpoint.host
        return self.post(url, data=json)

    def update_host(self, id: str, json) -> dict:
        url = self.endpoint.host.format(id=id)
        return self.put(url, data=json)

    def delete_host(self, id: str) -> dict:
        url = self.endpoint.host.format(id=id)
        return self.delete(url)


    #profiles
    def get_all_profiles(self) -> dict:
        return self.get(self.endpoint.profiles)

    @retry_request
    def get_profile(self, id: str) -> dict:
        url = self.endpoint.profile.format(id=id)
        return self.get(url)

    def get_profile_by_name(self, name: str) -> dict:
        url = self.endpoint.profile_without_id
        return self.get(url, params = {"name": name})

    def create_profile(self, json) -> dict:
        url = self.endpoint.profile
        return self.post(url, data=json)

    def update_profile(self, id: str, json) -> dict:
        url = self.endpoint.profile.format(id=id)
        return self.put(url, data=json)

    def delete_profile(self, id: str) -> dict:
        url = self.endpoint.profile.format(id=id)
        return self.delete(url)

    #service
    def get_all_services(self) -> dict:
        return self.get(self.endpoint.services)

    @retry_request
    def get_service(self, id: str) -> dict:
        url = self.endpoint.service.format(id=id)
        return self.get(url)

    def get_service_by_name(self, name: str) -> dict:
        url = self.endpoint.service_without_id
        return self.get(url, params = {"name": name})

    def create_service(self, json) -> dict:
        url = self.endpoint.service
        return self.post(url, data=json)

    def update_service(self, id: str, json) -> dict:
        url = self.endpoint.service.format(id=id)
        return self.put(url, data=json)

    def delete_service(self, id: str) -> dict:
        url = self.endpoint.service.format(id=id)
        return self.delete(url)
    
    #zone
    def get_all_zones(self) -> dict:
        return self.get(self.endpoint.zones)

    @retry_request
    def get_zone(self, id: str) -> dict:
        url = self.endpoint.zone.format(id=id)
        return self.get(url)

    def get_zone_by_name(self, name: str) -> dict:
        url = self.endpoint.zone_without_id
        return self.get(url, params = {"name": name})

    def create_zone(self, json) -> dict:
        url = self.endpoint.zone
        return self.post(url, data=json)

    def update_zone(self, id: str, json) -> dict:
        url = self.endpoint.zone.format(id=id)
        return self.put(url, data=json)

    def delete_zone(self, id: str) -> dict:
        url = self.endpoint.zone.format(id=id)
        return self.delete(url)

    #file_transfer
    #files dict {LocalFilePath:RemoteFilePath,...}
    def send_file(self, id: str, files: dict) -> str:
        url = self.endpoint.file_transfer.format(id=id)
        files_to_send = []
        for local_file_path, remote_file_path in files.items():
                files_to_send.append(
                        ('file', (remote_file_path, open(local_file_path, 'rb'), 'application/octet-stream'))
                        )
        body, content_type = requests.models.RequestEncodingMixin._encode_files(files_to_send, {})

        # this way you ensure having the same boundary defined in
        # the multipart/form-data contetn-type header
        # the form-data

        data = body
        headers = {
            "Content-Type": content_type,
            "apikey": self.apikey
        }
        response = requests.post(
            url,
            data=data,
            headers=headers
        )
        return response.text

    #file="/etc/hosts"
    def fetch_file(self, id: str, file: str) -> bytes:
        url = self.endpoint.file_transfer.format(id=id)
        payload = {'path': file}

        response = requests.get(url, params=payload)
        return response.content

    def delete_file(self, id: str, file: str) -> str:
        url = self.endpoint.file_transfer.format(id=id)
        payload = {'path': file}

        response = requests.delete(url, params=payload)
        return response.text

    def exec_command(self, id: str, json: dict) -> dict:
        url = self.endpoint.file_transfer.format(id=id)
        response = self.post(url, data=json)
        return response

    class Endpoint:
        externals = "externals"
        external = "external/{id}"
        external_without_id = "external"
        hosts = "hosts"
        host = "host/{id}"
        host_without_id = "host"
        groups = "groups"
        group = "group/{id}"
        group_without_id = "group"
        links = "links"
        link = "link/{id}"
        link_without_id = "link"
        profiles = "profiles"
        profile = "profile/{id}"
        profile_without_id = "profile"
        services = "services"
        service = "service/{id}"
        service_without_id = "service"
        zones = "zones"
        zone = "zone/{id}"
        zone_without_id = "zone"
        file_transfer = "file_transfer/{id}"
