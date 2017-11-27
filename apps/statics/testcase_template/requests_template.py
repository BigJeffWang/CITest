# coding=utf-8
import requests
import unittest
import json


class Test(unittest.TestCase):

    def testcase(self):
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

        if not headers:
            headers = {'content-type': "application/json"}

        if parameters:
            response = requests.request(method, url, data=parameters, headers=headers)
        else:
            response = requests.request(method, url, headers=headers)

        self.assertEqual(response.status_code, 200)

        if int(response_confirm):
            self.assertDictEqual(json.loads(response.text.encode('utf8')), json.loads(response_content))


if __name__ == "__main__":
    unittest.main()

