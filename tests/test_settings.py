def test_settings(test_settings):
    print(test_settings)
    print(test_settings.test_service_name)
    print(test_settings.appium_host)
    print(test_settings.appium_port)
    print(test_settings.app)
    print(test_settings.device)
    assert test_settings is None
