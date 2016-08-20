import json

from .base import BaseTestCase


class TestUserGroup(BaseTestCase):

    uuid = "00000000-0000-0000-0000-000000000001"
    base_url = "/user_group"

    def test_00_get_all(self):

        content, status = self.send_request("GET", self.base_url)
        print(len(content))
        assert status == 200

    def test_01_get_no_exist(self):

        url = "{}/{}".format(self.base_url, self.uuid)

        content, status = self.send_request("GET", url)

        assert status == 200
        assert content == {}

    def test_02_create(self):

        data = {
            "uuid": self.uuid,
            "name": "unittest"
        }

        content, status = self.send_request(
            "PUT", self.base_url,
            data=json.dumps(data)
        )

        assert status == 200
        assert self.uuid in content

    def test_03_create_exist(self):

        data = {
            "uuid": self.uuid,
            "name": "unittest"
        }

        content, status = self.send_request(
            "PUT", self.base_url,
            data=json.dumps(data)
        )

        assert status == 409

    def test_04_get_one(self):

        url = "{}/{}".format(self.base_url, self.uuid)
        content, status = self.send_request("GET", url)

        assert status == 200
        assert self.uuid in content

    def test_05_search(self):
        query = {"name": "unittest"}
        url = "{}/search".format(self.base_url)
        content, status = self.send_request(
            "POST", url,
            data=json.dumps(query)
        )
        assert status == 200
        assert self.uuid in content

    def test_06_update(self):

        data = {
            "name": "unittest_update"
        }

        content, status = self.send_request(
            "POST", self.base_url, data=json.dumps({self.uuid: data}))

        assert status == 200
        assert self.uuid in content
        assert content[self.uuid]["name"] == data["name"]

    def test_07_delete(self):

        url = "{}/{}".format(self.base_url, self.uuid)

        content, status = self.send_request(
            "DELETE", url
        )

        assert status == 200
        assert self.uuid in content
