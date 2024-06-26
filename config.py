from typing import Any, Dict

class Config:
    appName = 'com.nse.project.nse_driver_flutter_app'
    appActivity = '.MainActivity'

    capabilities: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': "UiAutomator2",
        'deviceName': 'emulator-5554',
        'appPackage': appName,
        'appActivity': appActivity,
        'noReset': 'true',
    }

    appium_server_url = 'http://localhost:4723'

    # Implicit Wait Timeout (seconds)
    IMPLICIT_WAIT = 10

    # Explicit Wait Timeout (seconds)
    EXPLICIT_WAIT = 20


