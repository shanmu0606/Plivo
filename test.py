import unittest
from base import BaseAPI
import random
import json


class TestAPI(unittest.TestCase):
    base = BaseAPI()
    #def test_create_channel(self):
        #url = 'https://api.slack.com/custom-integrations/legacy-tokens'
        #response = self.base.get(url)
        #print("res",response)

    def test_create(self):
        """
        create a channel
        :return:
        """
        #token = "Tivo"
        token = "xoxp-748478920679-740228929265-746648491872-ab13078641430917b85c21cf413d302a"
        name = random.random()
        url = "	https://slack.com/api/channels.create?token={}&name={}".format(token,name)
        response = self.base.post(url)
        json_response = json.loads(response)

        channel_name = json_response["channel"]["name"]
        return channel_name,token

    def test_join(self):
        """
        Join the channel
        :return:
        """
        token,channel_name = self.test_create()
        url = "	https://slack.com/api/channels.join?token={}&name={}".format(token, channel_name)
        response = self.base.post(url)
        json_response = json.loads(response)
        print("Response after joining channel",json_response)

    def test_rename(self):
        """
        Rename a channel
        :return:
        """

        token, channel_name = self.test_create()
        name = random.random()
        url = "	https://slack.com/api/channels.rename?token={}&channelname={}&name={}".format(token, channel_name,name)
        response = self.base.post(url)
        json_response = json.loads(response)
        print("Response after joining channel", json_response)


    def test_listchannel(self):
        """
        List all channels
        :return:
        """
        token, channel_name = self.test_create()
        url = "	https://slack.com/api/channels.rename?token={}".format(token)
        response = self.base.get(url)
        json_response = json.loads(response)
        print("response",response)














