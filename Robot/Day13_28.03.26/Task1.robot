*** Settings ***
Documentation  handling dropdowns
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handle dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//label[text()="Colors:"]
    Page Should Contain List    id=colors
    
    ${options}=  Get List Items    id=colors

    Log To Console    ${options}

    Select From List By Index  id=colors  2
    Select From List By Index  id=colors  3

    @{select_option}=  Get Selected List Labels    id=colors
    Log To Console    ${select_option}

    Sleep    3s
    Close Browser
