import boto3
import logging
from os.path import expanduser

usr_home = expanduser('~')

logging.basicConfig(filename='{}/logging.log'.format(usr_home), format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
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
        for key, value in instances.items():
            print '{}) {}'.format(key, value)

    if selector is 'id':
        return create_ordered_list(instance_ids)
    elif selector is 'name':
        return create_ordered_list(instance_names)
    elif selector is 'instance_ids':
        return instance_ids


def create_list(arg):
    return dict(enumerate(arg, 1))


def max_instances(arg):
    selected_instance = create_list(list_instances('instance_ids'))
    no_of_instances = len(selected_instance)
    if arg > no_of_instances:
        return True


def instance_state(selector):
    ec2 = boto3.resource('ec2')
    selected_instance = create_list(list_instances('instance_ids'))
    if max_instances(selector):
        return 'The entered value exceeds the number of instances available.'
    for i in ec2.instances.all():
        if i.id == selected_instance.get(selector):
            return i.state['Name']


def start_instance(selector):
    ec2 = boto3.client('ec2')
    selected_instance = create_list(list_instances('instance_ids'))
    if max_instances(selector):
        return 'The entered value exceeds the number of instances available.'
    elif instance_state(selector) == 'running':
        return 'The instance is already running.'
    else:
        try:
            response = ec2.start_instances(InstanceIds=[selected_instance.get(selector)], DryRun=False)
            state = response['StartingInstances']
            return '{} : Entered {} state.'.format(state[0]['InstanceId'], state[0]['CurrentState']['Name'])
        except Exception as e:
            logger.error(e)
            return 'Something went wrong. Please check the logs at ~/logging.log.'


def stop_instance(selector):
    ec2 = boto3.client('ec2')
    selected_instance = create_list(list_instances('instance_ids'))
    if max_instances(selector):
        return 'The entered value exceeds the number of instances available.'
    elif instance_state(selector) == 'stopped':
        return 'The instance is already stopped.'
    else:
        try:
            response = ec2.stop_instances(InstanceIds=[selected_instance.get(selector)], DryRun=False)
            state = response['StoppingInstances']
            return '{} : Entered {} state.'.format(state[0]['InstanceId'], state[0]['CurrentState']['Name'])
        except Exception as e:
            logger.error(e)
            return 'Something went wrong. Please check the logs at ~/logging.log.'


def get_ip_address(selector):
    ec2 = boto3.client('ec2')
    selected_instance = create_list(list_instances('instance_ids'))
    if max_instances(selector):
        return 'The entered value exceeds the number of instances available.'
    try:
        response = ec2.describe_instances(InstanceIds=[selected_instance.get(selector)])
        public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        private_ip = response['Reservations'][0]['Instances'][0]['PrivateIpAddress']
        return 'Public IP ({}): '.format(selected_instance.get(selector)) + public_ip + \
               '\nPrivate IP ({}): '.format(selected_instance.get(selector)) + private_ip
    except Exception as e:
        logger.error(e)
        return 'Something went wrong. Please check the logs at ~/logging.log.'


def list_lambdas(selector=0):
    aws_lambda = boto3.client('lambda')
    try:
        function_list = aws_lambda.list_functions()
        function_names = []
        for functions in function_list['Functions']:
            function_names.append(functions['FunctionName'])
        function_obj = create_list(function_names)
        if not selector:
            for key, val in function_obj.items():
                print '{}) {}'.format(key, val)
            return
        return function_obj.get(selector)
    except Exception as e:
        logger.error(e)
        return 'Something went wrong. Please check the logs at ~/logging.log.'


def invoke_lambda(selector):
    aws_lambda = boto3.client('lambda')
    try:
        response = aws_lambda.invoke(FunctionName=list_lambdas(selector))
        status_code = response['StatusCode']
        request_id = response['ResponseMetadata']['RequestId']
        return 'Status Code: {}'.format(status_code) + '\nRequest ID: {}'.format(request_id)
    except Exception as e:
        logger.error(e)
        return 'Something went wrong. Please check the logs at ~/logging.log.'
