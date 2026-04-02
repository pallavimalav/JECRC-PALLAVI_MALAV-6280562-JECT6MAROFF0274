*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_downloaded}  D:\file.txt

*** Test Cases ***
Upload
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/upload"]
    Sleep    3s
    
    ${path}  Normalize Path  ${CURDIR}/sample.txt
    
    Choose File    id=file-upload    ${path}
    Sleep    3s

    Click Button    id=file-submit

    Sleep    3s
    Close Browser

Download
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/download"]
    Sleep    3s

    Click Element    xpath=//a[@href="download/file.txt"]

    Wait Until Created    ${check_downloaded}  timeout=10s

    File Should Exist    ${check_downloaded}

    Log To Console    file downloaded successfully!

    Close Browser

