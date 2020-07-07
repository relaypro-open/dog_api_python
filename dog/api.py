from apiclient import APIClient, endpoint, paginated, retry_request
from apiclient import NoAuthentication,JsonResponseHandler,JsonRequestFormatter

# Define endpoints, using the provided decorator.
@endpoint(base_url="http://dog-ubuntu-server.lxd:7070/api")
class Endpoint:
    externals = "externals"
    external = "external/{id}"
    hosts = "hosts"
    host = "host/{id}"
    groups = "groups"
    group = "group/{id}"
    group_without_id = "group"
    links = "links"
    link = "link/{id}"
    profiles = "profiles"
    profile = "profile/{id}"
    profile_without_id = "profile"
    services = "services"
    service = "service/{id}"
    zones = "zones"
    zone = "zone/{id}"

# Extend the client for your API integration.
class DogClient(APIClient):
    #externals = "externals"
    #external = "external/{id}"
    def get_all_hosts(self) -> dict:
        return self.get(Endpoint.hosts)

    @retry_request
    def get_host(self, id: str) -> dict:
        url = Endpoint.host.format(id=id)
        return self.get(url)

    #group
    def get_all_groups(self) -> dict:
        return self.get(Endpoint.groups)

    @retry_request
    def get_group(self, id: str) -> dict:
        url = Endpoint.group.format(id=id)
        return self.get(url)

    def get_group_by_name(self, name: str) -> dict:
        url = Endpoint.group_without_id
        return self.get(url, params = {"name": name})

    def create_group(self, json) -> dict:
        url = Endpoint.group
        return self.post(url, data=json)

    def update_group(self, id: str, json) -> dict:
        url = Endpoint.group.format(id=id)
        return self.put(url, data=json)

    def delete_group(self, id: str) -> dict:
        url = Endpoint.group.format(id=id)
        return self.delete(url)

    #links = "links"
    #link = "link/{id}"

    #profiles
    def get_all_profiles(self) -> dict:
        return self.get(Endpoint.profiles)

    @retry_request
    def get_profile(self, id: str) -> dict:
        url = Endpoint.profile.format(id=id)
        return self.get(url)

    def get_profile_by_name(self, name: str) -> dict:
        url = Endpoint.profile_without_id
        return self.get(url, params = {"name": name})

    def create_profile(self, json) -> dict:
        url = Endpoint.profile
        return self.post(url, data=json)

    def update_profile(self, id: str, json) -> dict:
        url = Endpoint.profile.format(id=id)
        return self.put(url, data=json)

    def delete_profile(self, id: str) -> dict:
        url = Endpoint.profile.format(id=id)
        return self.delete(url)
    #services = "services"
    #service = "service/{id}"
    
    #zone
    def get_all_zones(self) -> dict:
        return self.get(Endpoint.zones)

    @retry_request
    def get_zone(self, id: str) -> dict:
        url = Endpoint.zone.format(id=id)
        return self.get(url)

    def get_zone_by_name(self, name: str) -> dict:
        url = Endpoint.zone_without_id
        return self.get(url, params = {"name": name})

    def create_zone(self, json) -> dict:
        url = Endpoint.zone
        return self.post(url, data=json)

    def update_zone(self, id: str, json) -> dict:
        url = Endpoint.zone.format(id=id)
        return self.put(url, data=json)

    def delete_zone(self, id: str) -> dict:
        url = Endpoint.zone.format(id=id)
        return self.delete(url)

def get_client():
    return DogClient(authentication_method=NoAuthentication(),
                   response_handler=JsonResponseHandler,
                       request_formatter=JsonRequestFormatter)
