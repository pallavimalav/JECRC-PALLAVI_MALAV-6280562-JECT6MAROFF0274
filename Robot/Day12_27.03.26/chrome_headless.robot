*** Settings ***
# - imports
Documentation  Opening of browsers
Library  SeleniumLibrary

*** Variables ***
# - will be defining all the variables.
${url}  https://www.cricbuzz.com/
#scalar variables
#list variables
@{bikes}  ktm  kwasaki  honda  pulsar
#dict variables
&{cars}  nissan=gtr  honda=civic  bmw=m5

*** Test Cases ***
# - consists of test scripts.
Opening Chrome headless Browser
    [Documentation]  chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  ${url}  headlesschrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Sleep  3s

    Close Browser


Open cricbuzz in edge
    Open Edge Browser

*** Keywords ***
## - user defined keywords will be written in keyword section.
Open Edge Browser
    [Documentation]  chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke
    Open Browser  ${url}  headlesschrome
    Maximize Browser Window

    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep  3s

    Close Browser
