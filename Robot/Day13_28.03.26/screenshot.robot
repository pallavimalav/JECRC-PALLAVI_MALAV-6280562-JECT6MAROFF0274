*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots 
    Set Screenshot Directory    ${CURDIR}/Screenshots
    
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    5s
    
    Capture Page Screenshot  fullpage.png
    Sleep    3s
    Scroll Element Into View    xpath=//div[text()="Project Hail Mary"]
    Capture Element Screenshot    xpath=//img[@alt="Project Hail Mary"]  Mary.png
    Sleep    3s

    Close Browser