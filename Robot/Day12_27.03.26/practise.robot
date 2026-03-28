*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkbox
    [Documentation]  testautomation checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  1s

    Click Element    xpath=(//input[@class="form-check-input"])[3]

    Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]
#    Page Should Contain Checkbox    id=sunday

    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s
    
    Click Button    id=female
    Sleep    2s
#    Click Button  xpath=(//input[@class="form-check-input"])[1]
#
#    Page Should Contain Button    xpath=(//input[@type="radio"])[1]
#
#    Select Radio Button    group_name    value
    Close Browser