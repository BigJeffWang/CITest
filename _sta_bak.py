# coding=utf-8
import requests
import unittest
import json


class Test(unittest.TestCase):

    def testcase(self):
        name = "test put"
        url = "http://127.0.0.1:5000/test"
        method = "PUT"
        headers = ""
        parameters = ''
        permission_confirm = "0"
        token_confirm = "0"
        response_confirm = "1"
        response_content = '{  "success": "PUT"}'
        hash_id = "20171127023442vRh0aB"
        status = "1"
        exec_status = "0"

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

