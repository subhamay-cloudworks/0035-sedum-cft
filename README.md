# Project Sedum: A Setp Function Demo

This is a simple demo of an AWS Step function using Lambda. The entire stack is created using CloudFormation.

## Description

This is a demo of a serverless application to automate handling of support tickets in a call center. While we could have one Lambda function call the other, managing all of those connections will become challenging as the call center application becomes more sophisticated. Plus, any change in the flow of the application will require changes in multiple places, and could end up writing the same code over and over again.
 
This challange can be solved using AWS Step Functions. Step Functions is a serverless orchestration service that lets you easily coordinate multiple Lambda functions into flexible workflows that are easy to debug and change. Step Functions will keep your Lambda functions free of additional logic by triggering and tracking each step of your application for you.

![Project Sedum - Design Diagram](https://subhamay-projects-repository-us-east-1.s3.amazonaws.com/0035-sedum/sedum-architecture-diagram.png)


### Installing

* Clone the repository.
* Create a S3 bucket and make it public.
* Create the folders - 0035-sedum/cft/nested-stacks, 0035-sedum/code/python
* Upload the following YAML templates to 0035-sedum/cft/nested-stacks
    * iam-role-stack.yaml
    * lambda-function-stack.yaml
* Upload the following YAML templates to 0035-sedum/cft/
    * sedum-root-stack.yaml
* Zip and Upload the Python files to 0035-sedum/code/python
* Create the entire using by using the root stack template sedum-root-stack.yaml by providing the required parameters 

### Executing program

* Go to the Step Function Console and use the sample input and start the execution
* Step-by-step bullets
```
{
  "CaseID": "263534"
}
```

## Help

Post message in my blog (https://blog.subhamay.com)

## Authors

Contributors names and contact info

Subhamay Bhattacharyya  - [subhamoyb@yahoo.com](https://blog.subhamay.com)

## Reference
https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/

## Version History

* 0.1
    * Initial Release

## License

None

## Acknowledgments

