from kestrel.session import Session

@given(u'a Kestrel session')
def step_impl(context):
    context.session = Session()
    assert context.session is not None

@given(u'a huntbook named "kestrel-test.hf"')
def step_impl(context):
    context.huntbook_name = 'kestrel-test.hf'

@when(u'I read with Kestrel the huntbook "kestrel-test.hf"')
def step_impl(context):
    with open(context.huntbook_name, 'r') as hff:
        context.huntflow = hff.read()
    assert context.huntflow

@then(u'I should see the execution results')
def step_impl(context):
    displays = context.session.execute(context.huntflow)
    assert displays

@then(u'close the session')
def step_impl(context):
    context.session.close()
    
@given(u'a hunt statement')
def step_impl(context):
    # context.hunt_statement = "procs = GET process FROM stixshifter://bh22 WHERE name = 'powershell.exe'"
    context.hunt_statement = "procs = GET process FROM stixshifter://bh22 WHERE name = 'powershell.exe' START 2022-07-01T00:00:00Z STOP 2022-08-01T00:00:00Z"

@when(u'I execute the statement with Kestrel')
def step_impl(context):
    context.results = context.session.execute(context.hunt_statement)
    context.procs = context.session.get_variable('procs')
    assert context.procs

@then(u'I should see the statement execution results')
def step_impl(context):
    print(f"len(result) = {len(context.procs)}")
    assert len(context.procs) == 21


@given(u'a hunt flow')
def step_impl(context):
    context.hunt_flow =  "newvar = GET process FROM stixshifter://bh22 WHERE [process:name = 'cmd.exe'] START 2022-07-01T00:00:00Z STOP 2022-08-01T00:00:00Z"


@when(u'I execute the hunt flow with Kestrel')
def step_impl(context):
    context.session.execute(context.hunt_flow)


@then(u'I should export the Kestrem variable to python')
def step_impl(context):
    cmds = context.session.get_variable('newvar')
    assert cmds