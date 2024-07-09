from typing import Any, Dict

class Config:

    capabilities: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'emulator-5554',
        'avd': 'Pixel_6_Pro_API_33',
        'appPackage': 'com.nse.project.nse_driver_flutter_app',
        'appActivity': 'com.example.nse_driver_flutter_app.MainActivity',
        'noReset': 'true',
    }

    appium_server_url = 'http://localhost:4723'

    # Implicit Wait Timeout (seconds)
    IMPLICIT_WAIT = 10

    # Explicit Wait Timeout (seconds)
    EXPLICIT_WAIT = 20
    
    # Controls the amount of detail included in the test results output. Note: 2 is the most details
    VERBOSITY = 2


