Feature: User API

    Background:
        Given value login from login.spec
    Scenario: Get emp route

    When GET /auth/emp

    And request-header Authenticate (string)
    Then status 200
    And response-body (string)

Examples:
            | Authenticate | 
            |($login.token)|