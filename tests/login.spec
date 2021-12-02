Feature: Contract for Login user


Scenario Outline: Authentication

Given Type RequestBody
|email|(string)|
|password|(string)|

And value loginCredential from auth.spec

And Type ResponseUser
|name|(string)|
|email|(string)|

And Type ResponseBody
|data|(ResponseUser)|
|success|(boolean)|
|token|(string)|

When POST /user/login
And request-body (RequestBody)
Then status 200
And Response-body (ResponseBody)
And export token = response-body

Examples:
            | email | password |
            |($email)  |($password)|