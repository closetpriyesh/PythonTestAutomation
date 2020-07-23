Feature: Amazon search functionality

    Scenario: Search button works or not
        Given user is on home page
        When user enters "laptop"
        Then he navigates to page whose title contains "laptop"

    Scenario: Search gives expected results or not
        Given user is on home page
        When user enters "laptop"
        Then he navigates to page whose title contains "laptop"
        Then the searched text "laptop" is displayed in a different color
        and the first item name contains "laptop"


