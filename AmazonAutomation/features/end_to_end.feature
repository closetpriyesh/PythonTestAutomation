Feature: Amazon end-to-end functionality

    Scenario: end-to-end analysis
        Given user is on home page
        When user enters "laptop"
        Then he navigates to page whose title contains "laptop"
        And selects the first item
        Then user goes to child window
        Then buy now button and add to cart button are displayed with appropriate texts







