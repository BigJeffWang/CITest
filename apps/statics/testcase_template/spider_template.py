# coding=utf-8

import urllib
import urllib2
import json
import unittest


def spider():
    name = "%(name)s"
    url = "%(url)s"
    method = "%(method)s"
    headers = "%(headers)s"
    parameters = '%(parameters)s'
    permission_confirm = "%(permission_confirm)s"
    token_confirm = "%(token_confirm)s"
    response_confirm = "%(response_confirm)s"
    response_content = '%(response_content)s'
    hash_id = "%(hash_id)s"
    status = "%(status)s"

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
