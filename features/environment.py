from flitter.flitter import Flitter


def before_scenario(context, step):
    context.errorMessage = 'Unimplemented step. ' + \
                           'Please provide the implementation.'

    context.app = Flitter()
