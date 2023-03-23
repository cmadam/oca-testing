from behave import given, when, then
from behave.model import Scenario

@given(u'an Elasticsearch index')
def step_impl(context):
    context.index_name = 'bh22'
    Scenario.continue_after_failed_step = True


@when(u'I retrieve all the processes from the index')
def step_impl(context):
    hunt_statement = f"procs = GET process FROM stixshifter://{context.index_name} WHERE pid > 0 START 2022-07-01T00:00:00Z STOP 2022-08-01T00:00:00Z"
    context.results = context.session.execute(hunt_statement)
    context.procs = context.session.get_variable('procs')
    assert context.procs


@then(u'the process entities should have a command_line attribute')
def step_impl(context):
    attribute_found = False
    for proc in context.procs:
        if 'command_line' in proc:
            attribute_found = True
            break
    assert attribute_found, 'command_line attribute not found'


@then(u'the process entities should have a stop_time attribute')
def step_impl(context):
    attribute_found = False
    for proc in context.procs:
        if 'stop_time' in proc:
            attribute_found = True
            break
    assert attribute_found, 'stop_time attribute not found'


@then(u'the process entities should have a ret_val attribute')
def step_impl(context):
    attribute_found = False
    for proc in context.procs:
        if 'ret_val' in proc:
            attribute_found = True
            break
    assert attribute_found, 'ret_val attribute not found'


@then(u'the process entities should have a is_hidden attribute')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the process entities should have a is_hidden attribute')


@then(u'the process entities should have a pid attribute')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the process entities should have a pid attribute')


@then(u'the process entities should have a created_time attribute')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the process entities should have a created_time attribute')


@then(u'the process entities should have a cwd attribute')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the process entities should have a cwd attribute')


@then(u'the process entities should have a environment_variables attribute')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the process entities should have a environment_variables attribute')

                    
