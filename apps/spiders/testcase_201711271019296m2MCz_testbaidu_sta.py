# coding=utf-8
import requests
import unittest
import json


class Test(unittest.TestCase):

    def testcase(self):
        name = "test baidu"
        url = "https://www.baidu.com/"
        method = "GET"
        headers = ""
        parameters = ''
        permission_confirm = "0"
        token_confirm = "0"
        response_confirm = "0"
        response_content = ''
        hash_id = "201711271019296m2MCz"
        status = "1"
        exec_status = "1"

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

