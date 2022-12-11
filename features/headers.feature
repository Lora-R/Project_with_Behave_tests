# Header icons - look Examples: header_icon
# Component that appear after click on an icon of the header - look Examples: component
Feature: Test the header icons functionality

  Scenario Outline: Click icon on header
    Given I load the website
    When I try click <header_icon>
    Then I see this component <component>
    Examples:
            | header_icon                                                  | component                                              |
#            |  mc-srh-box__tab-name |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div                           |
#            |  fi fi-flight |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/div[1]/div[3]/div[1]/div |
            |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/ul/li[3] |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div/div[3]/div[1]/input  |
            |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/ul/li[4] |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[3]/div[2]/div[3]/input                                   |
            |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/ul/li[5] |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[5]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/input       |
            |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/ul/li[6] |  /html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[6]/div/div[2]/div[1]/div[2]/div[2]/div/div       |


    Scenario: Search field
    Given I load the website
    When I write Spain in the search field
    Then I see this component /html/body/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div
    And I compare search text Spain with result /html/body/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div

    Scenario Outline: Find flight
    Given I load the website
    When I try click /html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/ul/li[2]
#    And Delete departure place information for light
    And Enter your conditions <from_where> <to_where>
    And Select dates <go_flight_date> <return_flight_data>
    And I try click /html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/div[2]
    Then I see this component /html/body/div[1]/div[2]/div/div/div[1]/div[2]/ul/li[2]/div[1]
      Examples:
            | from_where    | to_where   |  go_flight_date  | return_flight_data |
            | London        | Madrid     | 16-Fri           | 19-Mon             |
            | London        | Porto      | 22-Thu           | 29-Thu             |
            | Sofia         | Barcelona  | 30-Fri           | 31-Sat             |
