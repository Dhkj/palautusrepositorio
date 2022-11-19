*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input  kaal
    Input  kaal1234
    Output Should Contain  New user registered

*** Keywords ***  
Input New Command And Create User
    Input New Command
    Create User  kal  kalle123