*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalleo
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalleoo
    Set Password  kalle45
    Set Password Confirmation  kalle45
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  kalleoo
    Set Password  kalle456
    Set Password Confirmation  kalle457
    Submit Credentials
    Register Should Fail With Message  Nonmatching Password And Password Confirmation

Login After Successful Registration
    Set Username  kalleo
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Succeed

    Go To Login Page
    Set Username  kalleo
    Set Password  kalle456
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalleoo
    Set Password  kalle45
    Set Password Confirmation  kalle45
    Submit Credentials
    Register Should Fail With Message  Password too short

    Go To Login Page
    Set Username  kalleoo
    Set Password  kalle45
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open