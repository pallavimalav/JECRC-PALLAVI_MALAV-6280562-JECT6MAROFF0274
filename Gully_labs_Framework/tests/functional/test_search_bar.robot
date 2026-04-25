*** Settings ***
Resource  ../../resources/pages/search_bar_page.robot
Resource  ../../resources/common_resources.robot

Test Setup  Open Application    https://gullylabs.com/
Test Teardown  Close Application

*** Test Cases ***
TC04 Search Product
    [Documentation]  this navigates to the home page

    Click Element    ${search_icon}
    Log    Clicking on the search bar

    Search Product In Application    pink