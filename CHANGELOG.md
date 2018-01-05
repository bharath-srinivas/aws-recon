# **AWS Recon**

## v0.3.0 Beta release (2017-11-14)
### Features

- Added feature to list all the available lambda aws irrespective of region
- Added feature to invoke a lambda function synchronously in 'Request-Response' invocation type

### Improvements

- Modified the project architecture for improved performance
- Removed extra function calls to improve execution speed
- Updated README

### Build

- Changed the name officially from aws-recon to aws-recon

## v0.2.0 Beta release (2017-06-27)
### Features

- Added feature to show private and public IP address of the instance

### Build

- Changed the name of the tool to something meaningful
- Made some minor optimizations

## v0.1.0 Initial release (2017-02-13)
### Features

- List all the instances on a specific region based on their ID or name
- Display status of the instance
- Start the instance
- Stop the instance

### Build

- Optimized the code to perform some operations faster
- Optimized the code to handle all kind of errors and invalid values
- Made some improvements in the argparse to display better help message