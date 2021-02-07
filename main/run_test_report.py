import unittest
# from lib.HTMLTestRunner import HTMLTestRunner
from lib.BeautifulReport.BeautifulReport import BeautifulReport
import os
import time

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_blog_case')
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py', top_level_dir=None)

    project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    report_dir = os.path.join(project_root, 'report')
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    # report_abspath = os.path.join(report_dir, "HTMLReport_{}.html".format(current_time))
    # with open(report_abspath, 'wb') as f:
    #     runner = HTMLTestRunner(stream=f,
    #                             title='自动化测试报告',
    #                             description='用例执行情况',
    #                             verbosity=2
    #                             )

    result = BeautifulReport(suite)
    result.report(filename=current_time +'自动化测试报告',
                                description='用例执行情况',
                                log_path=report_dir
                                )
    # runner.run(suite)


