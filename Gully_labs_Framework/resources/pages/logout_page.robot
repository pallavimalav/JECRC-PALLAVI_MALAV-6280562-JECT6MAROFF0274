*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/logout_page_locator.robot

*** Keywords ***
Log Out The Application
    [Documentation]  this logouts in the login page
    Click Element    ${logout_btn}