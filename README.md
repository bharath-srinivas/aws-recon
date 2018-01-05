# **AWS Recon**

AWS Recon is a command-line tool written entirely on python. It can be used to perform basic operations on AWS instances like listing all the available instances, showing the status of the instance, starting and stopping the instance.

It uses AWS API to perform the tasks.

## **Installation and Usage**

The program is installed and tested on Ubuntu 14.04 (Trusty) and Ubuntu 16.04 (Xenial). For other distributions, please test it on your own and update me.

The program can be installed either from the source (as a package) or using the debian installation file. Both methods are easy but it is recommended to use the debian package as it'll completely remove the application and its dependencies along with it.

### **Installing as debian package**

To install as debian package

1. Get the .deb file from the releases either by visiting `https://github.com/bharath-srinivas/aws-recon/releases` directly or by using the following command:
```bash
$ wget https://github.com/bharath-srinivas/aws-recon/releases/download/v0.3.0/aws-recon_0.3.0-1_all.deb
```

2. After downloading the deb file, run the following command to install it:
```bash
$ sudo dpkg -i aws-recon_0.3.0-1_all.deb
```

3. That's it you're good to go. Refer to the [usage](#usage) below to see the list of commands

### **Installing from the source**

To install from the source

1. Clone the repository into your local machine using the following commands
```bash
$ git clone https://github.com/bharath-srinivas/aws-recon.git
```

2. Then install the package using the following commands
```bash
$ cd aws-recon
$ sudo python setup.py install
```
You can perform the above command without `sudo` in a `virtualenv`. If you do so, you'll need to activate the `virtualenv` everytime to use the tool as its dependencies will be installed within the `virtualenv`.

3. Check whether the package has installed successfully
```bash
$ pip freeze
```
You should see something like below in the output
```
aws-recon==0.3.0
```

4. If you see the above output, then you're good to go. Check the [usage](#usage) section for the list of commands. Otherwise check whether you've all the dependencies installed. This program relies on modules like awscli and boto3. By default it will be installed along with the setup. If it fails to install, you've to install manually using `pip install`.

### **Usage**

This program is dependent on awscli and hence you have to configure your `AWS Access Key ID`, `AWS Secret Access Key` and `Default region name` (`Default output format` is optional) in the awscli. To do this run the following command
```bash
$ aws configure
```
Once the configuration is done, you can perform the following operations
```bash
usage: aws-recon [-h] [-v] command ...

The available commands are:
  list        Lists all the instances
  status      Shows the status of the specified instance
  show-ip     Shows the public and private IP address of an instance
  start       Starts the specified instance
  stop        Stops the specified instance
  lambda      Performs lambda related operations

positional arguments:
  command        sub-command to run

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  shows the version and exit
```

To check the help message of each command, you can run `aws-recon command -h` or `aws-recon command --help`. This will display the sub-commands or arguments that can be used with the command.
```bash
usage: aws-recon list [-h] [arg]

List description

positional arguments:
  arg         Use id/name to list all instances based on their ID or name

optional arguments:
  -h, --help  show this help message and exit
```

## **Uninstallation**

To uninstall the tool if you've installed it by following the steps in Installing as debian package, run the following command
```bash
$ sudo apt-get remove aws-recon
```
This will completely remove all the files installed during the setup process.