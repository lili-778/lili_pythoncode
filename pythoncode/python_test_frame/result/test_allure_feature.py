import allure


@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    @allure.title("测试用例1")
    @allure.issue("14033",name="测试用例管理平台")
    @allure.severity(allure.severity_level.MINOR)
    def test_case1(self):
        print("case1")

    @allure.story("搜索成功")
    @allure.title("测试用例2")
    @allure.link("https://www.baidu.com",name="百度地址")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_case2(self):
        print("case2")
@allure.feature("登录模块")
class  TestLogin():
    @allure.story("登陆成功")
    @allure.title("测试用例3")
    def test_login_success(self):
        with allure.step("11"):
            print("打开应用")
        with allure.step("步骤2：登陆页面"):
            print("登录页面")
        with allure.step("步骤3：输入用户信息"):
            assert 1==2
            print("输入用户名和密码")
        with allure.step("步骤4：进入成功页面"):
            print("这是登录：测试用例11，登陆成功")

    @allure.story("登陆成功")
    def test_login_success_a(self):
        print("这是登录：测试用例12，登陆成功")

    @allure.story("登陆成功")
    def test_login_success_b(self):
        print("用户名缺失")

    @allure.story("登陆失败")
    def test_login_failure(self):
        print("输入用户名")
        assert "1"==1
        print('登录失败')

    @allure.story("登陆失败")
    def test_login_failure_a(self):
        print("这是登录测试用例，登录失败")

