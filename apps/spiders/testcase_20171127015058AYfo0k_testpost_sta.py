# coding=utf-8
import requests
import unittest2
import json


class Test(unittest2.TestCase):
    u'''
    asdfasdfasdf
    '''



    def testcase(self):
        name = "test post"
        url = "http://127.0.0.1:5000/test"
        method = "POST"
        headers = ""
        parameters = ''
        permission_confirm = "0"
        token_confirm = "0"
        response_confirm = "1"
        response_content = '{  "success": "1POST1","success": "POST1"}'
        hash_id = "20171127015058AYfo0k"
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

