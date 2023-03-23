Feature: Elastic Connector Maturity Test
    As a Threat Hunter
    I need to evaluate connector ability to handle and process individual entity types, attributes, and relationships
    So that I can score its relevance to threat hunting and investigations

Scenario: Test high-priority process attributes
    Given a Kestrel session
    And a running instance of Elasticsearch
    And an Elasticsearch index
    When I retrieve all the processes from the index
    Then the process entities should have a command_line attribute
    And the process entities should have a stop_time attribute
    And the process entities should have a ret_val attribute

Scenario: Test medium-priority process attributes
    Given a Kestrel session
    And a running instance of Elasticsearch
    And an Elasticsearch index
    When I retrieve all the processes from the index
    And the process entities should have a is_hidden attribute
    And the process entities should have a pid attribute
    And the process entities should have a created_time attribute
    And the process entities should have a cwd attribute
    And the process entities should have a environment_variables attribute
