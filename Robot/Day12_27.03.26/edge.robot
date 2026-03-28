*** Settings ***
# - imports
Documentation  Opening of browsers
Library  SeleniumLibrary

#*** Variables ***
# - will be defining all the variables.

*** Test Cases ***
# - consists of test scripts.
Opening Edge Browser
    [Documentation]  edge browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep  3s

    Close Browser