*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  mixu  tietokone123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  mixu  tietokone123
    Input New Command
    Input Credentials  mixu  tietokone123
    Output Should Contain  User with username mixu already exists

Register With Too Short Username And Valid Password
    Input Credentials  m  tietokone123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  mixu  tieto
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mixu  tietokone
    Output Should Contain  Password should also have numbers
    