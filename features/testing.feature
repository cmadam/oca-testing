Feature: Kestrel STIX-Shifter Integration Testing
    As a Threat Hunter
    I need Kestrel, a threat hunting tool
    So that I can hunt for threats

Scenario: A non-interactive execution of a huntflow
    Given a Kestrel session
    and a huntbook named "kestrel-test.hf"
    When I read with Kestrel the huntbook "kestrel-test.hf"
    Then I should see the execution results
    And close the session

Scenario: An interactive composition and execution of a huntflow
    Given a Kestrel session
    and a hunt statement
    When I execute the statement with Kestrel
    Then I should see the statement execution results
    And close the session

Scenario: Export Kestrel variable to Python
    Given a Kestrel session
    and a hunt flow
    When I execute the hunt flow with Kestrel
    Then I should export the Kestrem variable to python
    And close the session