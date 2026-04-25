*** Settings ***
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/common_resources.robot
Resource   ../../resources/pages/logout_page.robot

#Suite Setup  Load Environment
Test Setup  Open Application  https://gullylabs.com/
Test Teardown  Close Application

*** Test Cases ***
TC05 Logout Functionality
    [Documentation]    checking Log out
    Log In The Application    18lavi03@gmail.com  pallavi18@M
    Log Out The Application
