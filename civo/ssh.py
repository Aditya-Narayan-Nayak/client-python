import requests
from .utils import filter_list


class Ssh:
    """
    To manage the SSH keys for an account that are used for logging in to instances,
    there are a set of APIs for listing the SSH public keys currently stored,
    as well as adding and removing them by name.
    """

    def __init__(self, headers):
        self.headers = headers
        self.url = 'https://api.civo.com/v2/sshkeys'

    def create(self, name: str, public_key: str) -> object:
        """
        Function to uploading a SSH public key
        :param name: Name of the key
        :param public_key: Public key of the ssh
        :return: object json
        """
        payload = {'name': name, 'public_key': public_key}
        r = requests.post(self.url, headers=self.headers, params=payload)

        return r.json()

    def lists(self, filter: str = None) -> object:
        """
        Function to listing the SSH public keys
        :param filter: Filter json object the format is 'id:6224cd2b-d416-4e92-bdbb-db60521c8eb9',
                       you can filter by any object that is inside the json
        :return: object json
        """
        r = requests.get(self.url, headers=self.headers)

        if filter:
            data = r.json()
            return filter_list(data=data, filter=filter)

        return r.json()

    def retrieving(self, id: str) -> object:
        """
        Function to retrieving a SSH key
        :param id: id of the objects
        :return: object json
        """
        r = requests.get(self.url + '/{}'.format(id), headers=self.headers)

        return r.json()

    def updating(self, id: str, name: str) -> object:
        """
        Function to updating a SSH key
        :param id: id of the objects
        :param name: name to change
        :return: object json
        """
        payload = {'name': name}
        r = requests.put(self.url + '/{}'.format(id), headers=self.headers, params=payload)

        return r.json()

    def delete(self, id: str) -> object:
        """
        Function to removing a SSH key
        :return: object json
        """
        r = requests.delete(self.url + '/{}'.format(id), headers=self.headers)

        return r.json()