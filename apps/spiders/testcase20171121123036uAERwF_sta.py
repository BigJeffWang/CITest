# coding=utf-8

import urllib
import urllib2
import json
import unittest


def spider():
    name = "usertest"
    url = "http://127.0.0.1:8080/user"
    method = "GET"
    headers = ""
    parameters = ''
    permission_confirm = "0"
    token_confirm = "0"
    response_confirm = "1"
    response_content = '{"data": [{"id": 10000002, "created_at": "2017-11-15 13:50:23", "update_at": null, "deleted": false, "deleted_at": null, "name": null, "user_mobile": "123213", "user_realname": null, "user_idcard": null, "user_gender": true, "user_level": 0, "status": 0}, {"id": 10000003, "created_at": "2017-11-15 13:52:25", "update_at": null, "deleted": false, "deleted_at": null, "name": null, "user_mobile": "18611440468", "user_realname": null, "user_idcard": null, "user_gender": true, "user_level": 0, "status": 0}]}'
    hash_id = "20171121123036uAERwF"

    if parameters:
        parameters_dict = json.loads(parameters)
        data = urllib.urlencode(parameters_dict)
        req = urllib2.Request(url, data)
    else:
        req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    response_request = response.read().strip()
    response_content.strip()
    if int(response_confirm):
        # assert response_request == response_content, "response 不匹配"
        if response_request == response_content:
            return True
        else:
            return False
    return True


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(spider(), True)


if __name__ == "__main__":
    unittest.main()
