*** Settings ***
# - imports
Documentation  Opening of browsers
Library  SeleniumLibrary

*** Variables ***
# - will be defining all the variables.

*** Test Cases ***
# - consists of test scripts.
Opening Chrome Browser
    [Documentation]  chrome browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  chrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep  3s

    Close Browser


#*** Keywords ***
## - user defined keywords will be written in keyword section.
