*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/search_bar_locator.robot

*** Keywords ***
Search Product In Application
    [Documentation]  this searches for a product on search bar
    [Arguments]  ${product}

    Click Element    ${search_icon}
    Log    clicks on the search bar
    
    Click Element    ${search_bar}

    Input Text    ${search_bar}    ${product}
    Log    Entering product


    Sleep    3s
