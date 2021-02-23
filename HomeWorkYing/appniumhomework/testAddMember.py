from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestMember:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:75555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"  #不清空本地缓存，启动app
        caps["ensureWebviewsHavePages"] = True
        caps["settings[waitForIdleTimeout]"] = 3  #设置页面等待空闲状态的时间为0s

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phonenumber"),
                             yaml.safe_load(open("addMem.ymal", encoding="utf-8")))
    def test_addMember(self, name, phonenumber):
        self.driver.find_element(MobileBy.XPATH, "//*[@text= '通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名' )]/../android.widget.EditText")\
            .send_keys(name)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fwi").send_keys(phonenumber)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/aj_").click()
        addsus = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert addsus == '添加成功'

    @pytest.mark.skip
    def test_yaml(self):
        print(yaml.safe_load(open("addMem.ymal", encoding="utf-8")))










