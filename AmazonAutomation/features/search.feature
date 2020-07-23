Feature: Amazon search functionality

    Scenario Outline: Search gives expected results or not
        Given user is on home page
        When user enters "<word>"
        Then he navigates to page whose title contains "<word>"
        Then the searched text "<word>" is displayed in a different color
        and the first item name contains "<word>"

    Examples:
        | word      |
        | laptop    |
        | chocolate |


