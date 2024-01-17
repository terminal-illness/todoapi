*** Settings ***
Library     api_test.py
Library     api_test.TestApi   WITH NAME  TestApi

Documentation:  A test library for testing REST APIs

*** Variables ***
${url}=   http://localhost:8000

*** Keywords ***


*** Test Cases ***
Get Items
    [Tags]  get
    ${resp}=  TestApi.get_items
    Should Be Equal  ${resp.status_code}   ${200}
    Should Not Be Empty  ${resp.json()}
