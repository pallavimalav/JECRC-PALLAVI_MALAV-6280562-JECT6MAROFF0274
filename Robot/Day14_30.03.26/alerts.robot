*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Button    xpath=//button[@onclick="jsAlert()"]

    Sleep  3s
    Handle Alert

    Sleep    3s
    Close Browser

Confirmation Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Button    xpath=//button[@onclick="jsConfirm()"]

    Sleep  3s
    Handle Alert  action=DISMISS

    Sleep    3s
    Close Browser

Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Button    xpath=//button[@onclick="jsPrompt()"]

    Sleep  3s
    Input Text Into Alert    Capybara  action=DISMISS

    Sleep    3s
    Close Browser


