Feature: User API

    Background:
        Given value login from login.spec
    Scenario: Get emp route

        When GET /auth/emp

        And request-header Authorization (string)
        Then status 200
        And response-body (string)
        And value login from login.spec
        Examples:
            | Authorization  |
            | ($login.emp_token) |

    Scenario: Get emp route

        When GET /auth/admin

        And request-header Authorization (string)
        Then status 200
        And response-body (string)
        And value login from login.spec
        Examples:
            | Authorization  |
            | ($login.admin_token) |