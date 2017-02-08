import boto3
import logging
import os

__author__ = 'Bharath Srinivas'
created_on = '01-02-2017'

region = os.popen('aws configure get region').read()

logging.basicConfig(filename='logging.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def list_instances(selector):
    instance_ids = []
    instance_names = []

    ec2 = boto3.resource('ec2')

    for i in ec2.instances.all():
        instance_ids.append(i.id)
        for tag in i.tags:
            if tag['Key'] == 'Name':
                instance_names.append(tag['Value'])

    def create_ordered_list(arg):
        instances = dict(enumerate(arg, 1))
        # lists = ('{}. {}'.format(key, value) for key, value in instances.items())
        # return lists
        for key, value in instances.items():
            print '{}) {}'.format(key, value)

    if selector is 'id':
        return create_ordered_list(instance_ids)
    elif selector is 'name':
        return create_ordered_list(instance_names)
    elif selector is '':
        return instance_ids


def create_list(arg):
    return dict(enumerate(arg, 1))


def max_instances(arg):
    selected_instance = create_list(list_instances(''))
    no_of_instances = len(selected_instance)
    if arg > no_of_instances:
        return True


def instance_state(selector):
    ec2 = boto3.resource('ec2')
    selected_instance = create_list(list_instances(''))
    if max_instances(selector):
        return 'The entered value exceeds the number of instances available.'
    for i in ec2.instances.all():
        if i.id == selected_instance.get(selector):
            return i.state['Name']


def start_instance(selector):
    ec2 = boto3.client('ec2', region_name=region)
    selected_instance = create_list(list_instances(''))
    if max_instances(selector):
        return 'The entered value exceeds the number of instances available.'
    elif instance_state(selector) == 'running':
        return 'The instance is already running.'
    else:
        try:
            response = ec2.start_instances(InstanceIds=[selected_instance.get(selector)], DryRun=True)
            state = response['StartingInstances']
            return '{} : Entered {} state.'.format(state[0]['InstanceId'], state[0]['CurrentState']['Name'])
        except Exception as e:
            logger.error(e)
            return 'Something went wrong. Please check the logs at ~/logging.log.'


def stop_instance(selector):
    ec2 = boto3.client('ec2', region_name=region)
    selected_instance = create_list(list_instances(''))
    if max_instances(selector):
        return 'The entered value exceeds the number of instances available.'
    elif instance_state(selector) == 'stopped':
        return 'The instance is already stopped.'
    else:
        try:
            response = ec2.stop_instances(InstanceIds=[selected_instance.get(selector)], DryRun=True)
            state = response['StoppingInstances']
            return '{} : Entered {} state.'.format(state[0]['InstanceId'], state[0]['CurrentState']['Name'])
        except Exception as e:
            logger.error(e)
            return 'Something went wrong. Please check the logs at ~/logging.log.'
