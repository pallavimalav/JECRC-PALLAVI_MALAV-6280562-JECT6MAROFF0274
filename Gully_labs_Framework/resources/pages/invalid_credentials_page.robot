*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/login_page_locator.robot

*** Keywords ***
Log In With Invalid Credentials
    [Documentation]  this tests invalid credentials
    [Arguments]  ${email}  ${pwd}

    Click Element    ${account_link}
    Log    Clicking on the account link

    Input Text    ${email_label}    ${email}
    Log    Entering email

    Input Text    ${password_label}    ${pwd}
    Log    Entering password

    Click Element    ${sign_in_btn}
    Log    SIGNUP button
    Sleep    10s

    Page Should Contain Element    xpath=//div[@class="errors"]
    Page Should Contain    Incorrect email or password.

    Sleep    3s

    Close Browser
