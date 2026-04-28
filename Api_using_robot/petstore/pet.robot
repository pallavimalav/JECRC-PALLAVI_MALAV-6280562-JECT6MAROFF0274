*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    Create Session    petapi    ${BASE_URL}    verify=True

    # for add pet
    ${payload}=  Load Json From File    ${CURDIR}/../data/add_pet.json

    ${response}=  POST On Session  petapi  /pet  json=${payload}
    
    Should Be Equal As Integers    ${response.status_code}    200
    
    Log To Console    ${response.json()}

Update Pet
    Create Session    petapi    ${BASE_URL}    verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/update_pet.json

    ${response}=  POST On Session  petapi  /pet  json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=  Set Variable    ${response.json()}
    Set Suite Variable    ${Pet_id}  ${body}[id]
    Log To Console    ${response.json()}
    Log To Console    ${Pet_id}

Find Pet by Pet Id
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/add_pet.json


    ${response}=  GET On Session    petapi    /pet/${Pet_id}  json=${payload}

    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}


Query Parameter
    Create Session    petapi    ${BASE_URL}    verify=True

    # for query parameter just one line extra
    ${qp} =  Create Dictionary    status=available

    # for add pet
    ${payload}=  Load Json From File    ${CURDIR}/../data/add_pet.json
                                                                  # to call query parameters
    ${response}=  POST On Session  petapi  /pet  json=${payload}  params=${qp}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Upload an Image
    Create Session    petapi    ${BASE_URL}  verify=True
    
    ${form_data}=  Create Dictionary    additionalMetadata=Tomatino's img
    ${file_path}=  Set Variable    ${CURDIR}/../data/tomatino.jpg
    ${file}=  Evaluate    {'file': open($file_path,'rb')}
    
    ${response}=  POST On Session  petapi  /pet/55/uploadImage
    ...  data=${form_data}
    ...  files=${file}

    Should Be Equal As Integers    ${response.status_code}  200

Update pet with form data
    [Documentation]    Update pet with form data
    Create Session    petapi    ${BASE_URL}   verify=True
    ${form_data}=    Create Dictionary   name=tomatino   status=sold
    ${response}=    POST On Session    petapi    /pet/${PET_ID}    data=${form_data}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}


Delete pet
    [Documentation]    Delete pet by ID
    Create Session    petapi    ${BASE_URL}   verify=True
    ${response}=    DELETE On Session    petapi    /pet/${PET_ID}
    Should Be Equal As Integers    ${response.status_code}    200

    

    

    

