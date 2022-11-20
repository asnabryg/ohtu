*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Input Register Credentials  mixu  tietokone1  tietokone1
    Register Should Succeed

Register With Too Short Username And Valid Password
    Input Register Credentials  m  tietokone1  tietokone1
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Input Register Credentials  mixu  tieto  tieto
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Input Register Credentials  mixu  tietokone1  tietokone
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Go To Login Page
    Input Text  username  mixu
    Input Text  password  tietokone1
    Click Button  Login
    Title Should Be  Ohtu Application main page

Login After Failed Registration
    Go To Login Page
    Input Text  username  m
    Input Text  password  tietokone1
    Click Button  Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password 

*** Keywords ***
Input Register Credentials
    [Arguments]  ${username}  ${password}  ${password confirmation}
    Input Text  username  ${username}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password confirmation}
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
