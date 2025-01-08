from apiclient import APIClient, retry_request
from apiclient import HeaderAuthentication
from apiclient import JsonResponseHandler
from apiclient import JsonRequestFormatter
from apiclient.error_handlers import BaseErrorHandler
from apiclient import exceptions
from apiclient.response import Response
import requests


# Extend the client for your API integration.
class DogClient(APIClient):
    def __init__(self,
                 base_url,
                 apitoken="",
                 request_timeout=300.0
                 ):
        authentication_method = HeaderAuthentication(
            token=apitoken
            )
        super().__init__(authentication_method=authentication_method,
                         response_handler=JsonResponseHandler,
                         request_formatter=JsonRequestFormatter)
        self.authentication_method = authentication_method
        self.apitoken = apitoken
        self.endpoint = self.Endpoint(base_url=base_url)
        self.set_request_timeout(request_timeout)

    # external
    def get_all_externals(self) -> dict:
        return self.get(self.endpoint.externals)

    @retry_request
    def get_external(self, id: str) -> dict:
        url = self.endpoint.external.format(id=id)
        return self.get(url)

    def get_external_by_name(self, name: str) -> dict:
        url = self.endpoint.external_without_id
        return self.get(url, params={"name": name})

    def create_external(self, json) -> dict:
        url = self.endpoint.external
        return self.post(url, data=json)

    def update_external(self, id: str, json) -> dict:
        url = self.endpoint.external.format(id=id)
        return self.put(url, data=json)

    def delete_external(self, id: str) -> dict:
        url = self.endpoint.external.format(id=id)
        return self.delete(url)

    # group
    def get_all_groups(self) -> dict:
        return self.get(self.endpoint.groups)

    @retry_request
    def get_group(self, id: str) -> dict:
        url = self.endpoint.group.format(id=id)
        return self.get(url)

    def get_group_by_name(self, name: str) -> dict:
        url = self.endpoint.group_without_id
        return self.get(url, params={"name": name})

    def create_group(self, json) -> dict:
        url = self.endpoint.group
        return self.post(url, data=json)

    def update_group(self, id: str, json) -> dict:
        url = self.endpoint.group.format(id=id)
        return self.put(url, data=json)

    def delete_group(self, id: str) -> dict:
        url = self.endpoint.group.format(id=id)
        return self.delete(url)

    # link
    def get_all_links(self) -> dict:
        return self.get(self.endpoint.links)

    @retry_request
    def get_link(self, id: str) -> dict:
        url = self.endpoint.link.format(id=id)
        return self.get(url)

    def get_link_by_name(self, name: str) -> dict:
        url = self.endpoint.link_without_id
        return self.get(url, params={"name": name})

    def create_link(self, json) -> dict:
        url = self.endpoint.link
        return self.post(url, data=json)

    def update_link(self, id: str, json) -> dict:
        url = self.endpoint.link.format(id=id)
        return self.put(url, data=json)

    def delete_link(self, id: str) -> dict:
        url = self.endpoint.link.format(id=id)
        return self.delete(url)

    # host
    def get_all_hosts(self) -> dict:
        return self.get(self.endpoint.hosts)
    
    def get_all_active_hosts(self) -> dict:
        return self.get(self.endpoint.hosts, params={"active":"true"})

    @retry_request
    def get_host(self, id: str) -> dict:
        url = self.endpoint.host.format(id=id)
        return self.get(url)

    def get_host_by_name(self, name: str) -> dict:
        url = self.endpoint.host_without_id
        return self.get(url, params={"name": name})

    def get_host_by_hostkey(self, hostkey: str) -> dict:
        url = self.endpoint.host_without_id
        return self.get(url, params={"hostkey": hostkey})

    def create_host(self, json) -> dict:
        url = self.endpoint.host
        return self.post(url, data=json)

    def update_host(self, id: str, json) -> dict:
        url = self.endpoint.host.format(id=id)
        return self.put(url, data=json)

    def delete_host(self, id: str) -> dict:
        url = self.endpoint.host.format(id=id)
        return self.delete(url)

    # profiles
    def get_all_profiles(self) -> dict:
        return self.get(self.endpoint.profiles)

    @retry_request
    def get_profile(self, id: str) -> dict:
        url = self.endpoint.profile.format(id=id)
        return self.get(url)

    def get_profile_by_name(self, name: str) -> dict:
        url = self.endpoint.profile_without_id
        return self.get(url, params={"name": name})

    def create_profile(self, json) -> dict:
        url = self.endpoint.profile
        return self.post(url, data=json)

    def update_profile(self, id: str, json) -> dict:
        url = self.endpoint.profile.format(id=id)
        return self.put(url, data=json)

    def delete_profile(self, id: str) -> dict:
        url = self.endpoint.profile.format(id=id)
        return self.delete(url)

    # service
    def get_all_services(self) -> dict:
        return self.get(self.endpoint.services)

    @retry_request
    def get_service(self, id: str) -> dict:
        url = self.endpoint.service.format(id=id)
        return self.get(url)

    def get_service_by_name(self, name: str) -> dict:
        url = self.endpoint.service_without_id
        return self.get(url, params={"name": name})

    def create_service(self, json) -> dict:
        url = self.endpoint.service
        return self.post(url, data=json)

    def update_service(self, id: str, json) -> dict:
        url = self.endpoint.service.format(id=id)
        return self.put(url, data=json)

    def delete_service(self, id: str) -> dict:
        url = self.endpoint.service.format(id=id)
        return self.delete(url)

    # zone
    def get_all_zones(self) -> dict:
        return self.get(self.endpoint.zones)

    @retry_request
    def get_zone(self, id: str) -> dict:
        url = self.endpoint.zone.format(id=id)
        return self.get(url)

    def get_zone_by_name(self, name: str) -> dict:
        url = self.endpoint.zone_without_id
        return self.get(url, params={"name": name})

    def create_zone(self, json) -> dict:
        url = self.endpoint.zone
        return self.post(url, data=json)

    def update_zone(self, id: str, json) -> dict:
        url = self.endpoint.zone.format(id=id)
        return self.put(url, data=json)

    def delete_zone(self, id: str) -> dict:
        url = self.endpoint.zone.format(id=id)
        return self.delete(url)

    # ruleset
    def get_all_rulesets(self) -> dict:
        return self.get(self.endpoint.rulesets)

    @retry_request
    def get_ruleset(self, id: str) -> dict:
        url = self.endpoint.ruleset.format(id=id)
        return self.get(url)

    def get_ruleset_by_name(self, name: str) -> dict:
        url = self.endpoint.ruleset_without_id
        return self.get(url, params={"name": name})

    def create_ruleset(self, json) -> dict:
        url = self.endpoint.ruleset
        return self.post(url, data=json)

    def update_ruleset(self, id: str, json) -> dict:
        url = self.endpoint.ruleset.format(id=id)
        return self.put(url, data=json)

    def delete_ruleset(self, id: str) -> dict:
        url = self.endpoint.ruleset.format(id=id)
        return self.delete(url)

    # fact
    def get_all_facts(self) -> dict:
        return self.get(self.endpoint.facts)

    @retry_request
    def get_fact(self, id: str) -> dict:
        url = self.endpoint.fact.format(id=id)
        return self.get(url)

    def get_fact_by_name(self, name: str) -> dict:
        url = self.endpoint.fact_without_id
        return self.get(url, params={"name": name})

    def create_fact(self, json) -> dict:
        url = self.endpoint.fact
        return self.post(url, data=json)

    def update_fact(self, id: str, json) -> dict:
        url = self.endpoint.fact.format(id=id)
        return self.put(url, data=json)

    def delete_fact(self, id: str) -> dict:
        url = self.endpoint.fact.format(id=id)
        return self.delete(url)

    # file_transfer
    # files dict {LocalFilePath:RemoteFilePath,...}
    def send_file(self, id: str, files: dict) -> str:
        url = self.endpoint.file_transfer.format(id=id)
        files_to_send = []
        for local_file_path, remote_file_path in files.items():
            files_to_send.append(
                ('file', (remote_file_path, open(local_file_path, 'rb'),
                          'application/octet-stream'))
                )
        body, content_type = requests.models.RequestEncodingMixin._encode_files(files_to_send, {})

        # this way you ensure having the same boundary defined in
        # the multipart/form-data contetn-type header
        # the form-data

        data = body
        headers = {
            "Content-Type": content_type,
            'Authorization': 'Bearer ' + self.apitoken,
            'Accept-Encoding': 'identity, deflate, compress, gzip'
        }
        response = requests.post(
            url,
            data=data,
            headers=headers
        )
        return response.text

    # file="/etc/hosts"
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
        try:
            url = self.endpoint.file_transfer.format(id=id)
            response = self.post(url, data=json)
            return response
        except ExecErrorHandler:
            return []

    class Endpoint():
        def __init__(self, base_url):
            self.base_url = base_url.rstrip("/") + "/"

            self.externals = self.base_url + "externals"
            self.external = self.base_url + "external/{id}"
            self.external_without_id = self.base_url + "external"
            self.hosts = self.base_url + "hosts"
            self.host = self.base_url + "host/{id}"
            self.host_without_id = self.base_url + "host"
            self.groups = self.base_url + "groups"
            self.group = self.base_url + "group/{id}"
            self.group_without_id = self.base_url + "group"
            self.links = self.base_url + "links"
            self.link = "self.base_url + link/{id}"
            self.link_without_id = self.base_url + "link"
            self.profiles = self.base_url + "profiles"
            self.profile = self.base_url + "profile/{id}"
            self.profile_without_id = self.base_url + "profile"
            self.services = self.base_url + "services"
            self.service = self.base_url + "service/{id}"
            self.service_without_id = self.base_url + "service"
            self.zones = self.base_url + "zones"
            self.zone = self.base_url + "zone/{id}"
            self.zone_without_id = self.base_url + "zone"
            self.file_transfer = self.base_url + "file_transfer/{id}"
            self.rulesets = self.base_url + "rulesets"
            self.ruleset = self.base_url + "ruleset/{id}"
            self.ruleset_without_id = self.base_url + "ruleset"
            self.facts = self.base_url + "facts"
            self.fact = self.base_url + "fact/{id}"
            self.fact_without_id = self.base_url + "fact"


class ExecErrorHandler(BaseErrorHandler):
    @staticmethod
    def get_exception(response: Response) -> exceptions.APIRequestError:
        """Parses client errors to extract bad request reasons."""
        if 400 <= response.get_status_code() < 500:
            # json = response.get_json()
            # return exceptions.ClientError(json["error"]["reason"])
            return response
        return exceptions.APIRequestError("something went wrong")
