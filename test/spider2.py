# coding=utf-8
import HTMLTestRunner
import requests
import unittest
import time

class Test(unittest.TestCase):

    def test_connect(self):
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

        url = "http://127.0.0.1:5000/test"
        parameters = '{"id":1, "name":"中文"}'
        headers = ""
        method = "POST"
        response_confirm = "0"
        if not headers:
            headers = {'content-type': "application/json"}

        # with self.assertRaises(TypeError):
        if parameters:
            response = requests.request(method, url, data=parameters, headers=headers)
        else:
            response = requests.request(method, url, headers=headers)

        self.assertEqual(response.status_code, 200)

        if int(response_confirm):
            self.assertEqual(response.text.encode('utf8').strip(), response_confirm.strip())


if __name__ == "__main__":
    # unittest.main()
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(Test("test_connect"))
    # 获取当前时间，这样便于下面的使用。
    # now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # # 打开一个文件，将result写入此file中
    # with open("/Users/licaifan/workspace/result" + now + ".html", 'wb') as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    #     runner.run(testunit)

