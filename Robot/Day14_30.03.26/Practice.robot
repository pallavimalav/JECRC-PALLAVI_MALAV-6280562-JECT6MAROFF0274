*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling nested iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    3s

     Click Element    xpath=//a[@href="#Multiple"]
     Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
     Select Frame    xpath=//iframe[@src="SingleFrame.html"]

      Input Text    xpath=//input[@type="text"]    capybara

    Sleep    3s
    Close Browser

