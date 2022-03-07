Feature: Test that pages have corrtect content
    Scenario: Blog page has a correct title
        Given I am on the blog page 
        Then There is a little shown on the pages
        And The title tag has content "This is the blog page"