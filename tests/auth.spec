Feature: Contract for signup user
    Scenario: Should be able to save employee user

        Given type RequestBody
            | name     | (string) |
            | email    | (string) |
            | password | (string) |

        And Type ResponseUser
            | name     | (string) |
            | email    | (string) |
            | password | (string) |
            | role     | (string) |
            | _id      | (string) |
            | __v      | (number) |

        And Type ResponseBody
            | success | (boolean)      |
            | data    | (ResponseUser) |
            | error   | (string?)      |


        When POST /user/signup
        And request-body (RequestBody)
        Then status 200
        And response-body (ResponseBody)
        Examples:
            | email    | name    | password    |role|
            | ($emp_user.email) | ($emp_user.name) | ($emp_user.password) |employee|

    Scenario: Should be able to save admin user

        Given type RequestBody
            | name     | (string) |
            | email    | (string) |
            | password | (string) |


        And Type ResponseUser
            | name     | (string) |
            | email    | (string) |
            | password | (string) |
            | role     | (string) |
            | _id      | (string) |
            | __v      | (number) |

        And Type ResponseBody
            | success | (boolean)      |
            | data    | (ResponseUser) |
            | error   | (string?)      |


        When POST /user/signup
        And request-body (RequestBody)
        Then status 200
        And response-body (ResponseBody)
        Examples:
            | email    | name    | password    |role|
            | ($admin_user.email) | ($admin_user.name) | ($admin_user.password) |admin|


