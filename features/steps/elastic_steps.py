from behave import given, when, then
from behave.model import Scenario


@then(u'the process entities should have a "{attribute}" attribute')
def step_impl(context, attribute):
    Scenario.continue_after_failed_step = True
    attribute_found = False
    for proc in context.procs:
        if attribute in proc:
            attribute_found = True
            break
    assert attribute_found, f'{attribute} attribute not found'


@given(u'an Elasticsearch index')
def step_impl(context):
    context.index_name = 'bh22'
    Scenario.continue_after_failed_step = True


@given(u'a list of all the processes retrieved from the index')
def step_impl(context):
    hunt_statement = f"procs = GET process FROM stixshifter://{context.index_name} WHERE pid > 0 START 2022-07-01T00:00:00Z STOP 2022-08-01T00:00:00Z"
    context.results = context.session.execute(hunt_statement)
    context.procs = context.session.get_variable('procs')
    assert context.procs


@when(u'I examine the list of processes')
def step_impl(context):
    assert context.procs