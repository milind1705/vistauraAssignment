Feature: Contract for Login user
    Scenario Outline: Authentication for employee
        Given Type RequestBody
            | email    | (string) |
            | password | (string) |

        And value loginCredential from auth.spec

        And Type ResponseUser
            | name  | (string) |
            | email | (string) |

        And Type ResponseBody
            | data    | (ResponseUser) |
            | success | (boolean)      |
            | token   | (string)       |

        When POST /user/login
        And request-body (RequestBody)
        Then status 200
        And Response-body (ResponseBody)
        And export emp_token = response-body.token

        Examples:
            | email        | password        |
            | ($emp_email) | ($emp_password) |


    Scenario Outline: Authentication for admin
        Given Type RequestBody
            | email    | (string) |
            | password | (string) |

        And value loginCredential from auth.spec

        And Type ResponseUser
            | name  | (string) |
            | email | (string) |

        And Type ResponseBody
            | data    | (ResponseUser) |
            | success | (boolean)      |
            | token   | (string)       |

        When POST /user/login
        And request-body (RequestBody)
        Then status 200
        And Response-body (ResponseBody)
        And export admin_token = response-body.token

        Examples:
            |       email    |     password      |
            | ($admin_email) | ($admin_password) |