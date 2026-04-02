# Task-1

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling popups
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s
    Click Element    xpath=//button[@id="PopUp"]
    Sleep    3s

     @{windows}  Get Window Handles
     @{titles}  Get Window Titles
     Log To Console    ${titles}
     
     Log To Console    ${titles}[-1]

      Switch Window  New
      Sleep    3s

      Switch Window  ${windows}[0]
      Log To Console    ${titles}[0]
      Page Should Contain  Automation Testing Practice
#     Page Should Contain Element    xpath=//h1[@class="title"]
#
#    Switch Window  ${windows}[0]

    Sleep    3s
    Close Browser
