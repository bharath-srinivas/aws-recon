import actions

__author__ = 'Bharath Srinivas'
created_on = '01-02-2017'


def list_all_instances(arg):
    return actions.list_instances(arg)


def state(arg):
    return actions.instance_state(arg)


def start(arg):
    return actions.start_instance(arg)


def stop(arg):
    return actions.stop_instance(arg)
