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
    exec_status = "%(exec_status)s"
    data = ""

    if not headers:
        headers = {'Content-Type', 'application/json'}
    if parameters:
        parameters_dict = json.loads(parameters)
        data = urllib.urlencode(parameters_dict)

    if method == "GET":
        response = urllib2.urlopen(url)
    elif method == "POST":
        if parameters:
            request = urllib2.Request(url, data, headers)
        else:
            request = urllib2.Request(url)
        response = urllib2.urlopen(request)
    elif method == "PUT":
        if parameters:
            request = urllib2.Request(url, data, headers)
        else:
            request = urllib2.Request(url)
        request.get_method = lambda: 'PUT'
        response = urllib2.urlopen(request)
    elif method == "DELETE":
        if parameters:
            request = urllib2.Request(url, data, headers)
        else:
            request = urllib2.Request(url)
        request.get_method = lambda: 'DELETE'
        response = urllib2.urlopen(request)
    else:
        response = urllib2.urlopen(url)

    response_code = response.code
    if response_code == 200:
        if int(response_confirm):
            response_request = response.read().strip()
            response_content.strip()
            # assert response_request == response_content, "response 不匹配"
            if response_request == response_content:
                return True
            else:
                return False
        return True
    else:
        return False


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(spider(), True)


if __name__ == "__main__":
    unittest.main()
