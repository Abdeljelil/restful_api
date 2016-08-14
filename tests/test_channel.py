from .base import BaseTestCase, BaseFakeModel

from backend.models.channel import ChannelModel
import json


class FakeChannelModel(BaseFakeModel):

    metaclass = ChannelModel

    fakedatadict = {}


class TestChannel(BaseTestCase):

    uuid = "00000000-0000-0000-0000-000000000001"

    def test_00_get_all(self):

        url = self.make_url("/channel")
        content, status = self.send_request("GET", url)

        assert status == 200

    def test_01_get_no_exist(self):

        url = self.make_url("/channel/{}".format(self.uuid))

        content, status = self.send_request("GET", url)

        assert status == 200
        assert content == {}

    def test_02_create(self):

        data = {
            "uuid": self.uuid,
            "name": "unitest_channel",
            "index": 15,
        }

        url = self.make_url("/channel")

        content, status = self.send_request(
            "PUT", url,
            data=json.dumps(data)
        )

        assert status == 200
        assert self.uuid in content

    def test_03_create_exist(self):

        data = {
            "uuid": self.uuid,
            "name": "unitest_channel",
            "index": 15,
        }

        url = self.make_url("/channel")

        content, status = self.send_request(
            "PUT", url,
            data=json.dumps(data)
        )

        assert status == 409

    def test_04_get_one(self):

        url = self.make_url("/channel/{}".format(self.uuid))
        content, status = self.send_request("GET", url)

        assert status == 200
        assert self.uuid in content

    def test_05_update(self):

        data = {
            "name": "unittest_channel_update"
        }

        url = self.make_url("/channel")

        content, status = self.send_request(
            "POST", url, data=json.dumps({self.uuid: data}))

        assert status == 200
        assert self.uuid in content
        assert content[self.uuid]["name"] == data["name"]

    def test_09_delete(self):

        url = self.make_url("/channel/{}".format(self.uuid))

        content, status = self.send_request(
            "DELETE", url
        )

        assert status == 200
        assert self.uuid in content
