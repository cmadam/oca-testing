from kestrel.session import Session

def before_feature(context, feature):
    if feature.name == 'Elastic Connector Maturity Test':
        context.session = Session()
        context.index_name = 'bh22'
        hunt_statement = f"procs = GET process FROM stixshifter://{context.index_name} WHERE pid > 0 START 2022-07-01T00:00:00Z STOP 2022-08-01T00:00:00Z"
        context.results = context.session.execute(hunt_statement)
        context.procs = context.session.get_variable('procs')