*** Settings ***
Resource  ../../resources/pages/invalid_credentials_page.robot
Resource  ../../resources/common_resources.robot

*** Variables ***
Test Setup  Open Application    https://gullylabs.com/
Test Teardown  Close Application

*** Test Cases ***
TC03 Invalid Credentials
    [Documentation]  check for invalid credentials
    [Tags]  functional

    Log In With Invalid Credentials    capybara@gmail.com    3capybara