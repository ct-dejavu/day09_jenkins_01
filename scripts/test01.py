import allure
import pytest


class Test(object):
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title='执行登录')
    def test01(self):
        print('成功')

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title='执行退出登录')
    def test02(self):
        print('成功')

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test03(self):
        allure.attach('失败原因', '用户名错误')
        pass
