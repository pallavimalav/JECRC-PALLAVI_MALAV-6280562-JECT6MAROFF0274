# Task - 2

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

    Click Button    xpath=//button[@id="alertBtn"]

    Sleep  3s
    Handle Alert

    Sleep    3s
    Close Browser

Confirmation alert-accepting
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    id=confirmBtn
    Click Button    id=confirmBtn
    Sleep    2s

    Handle Alert
    Sleep    3s

    Page Should Contain    You pressed OK!
    ${msg}  Get Text    id=demo

    Log To Console    ${msg}
    Close Browser

Confirmation alert-cancelling
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    id=confirmBtn
    Click Button    id=confirmBtn
    Sleep    2s

    Handle Alert  action=DISMISS
    Sleep    3s

    Page Should Contain    You pressed Cancel!
    ${msg}  Get Text    id=demo

    Log To Console    ${msg}
    Close Browser

Prompt alert-accepting
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    id=promptBtn
    Click Button    id=promptBtn
    Sleep    2s

    ${text}=  Set Variable  Capybara
    Input Text Into Alert    ${text}
    Page Should Contain    ${text}
    ${msg}  Get Text    id=demo

    Log To Console    ${msg}
    Close Browser

Prompt alert-cancelling
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    id=promptBtn
    Click Button    id=promptBtn
    Sleep    2s

    ${text}=  Set Variable  Capybara
    Input Text Into Alert    ${text}  action=DISMISS
    Page Should Contain    cancelled
    ${msg}  Get Text    id=demo

    Log To Console    ${msg}
    Close Browser

