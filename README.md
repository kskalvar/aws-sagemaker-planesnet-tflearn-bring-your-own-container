# AWS SageMaker PlanesNet TFLearn Bring Your Own Container

This example shows how to package the [TFLearn][tfl] Machine Learning Library for use with SageMaker. TFLearn is not supported by SageMaker currently so we'll need to build a container to support it.  This solution will use the SageMaker Python SDK to build a distributed service to train/deploy/detect.  We have also chosen the [PlanesNet][planesnet] planesnet-detector project which uses TFLearn to detect aircraft in an image and highlighted with a bounding box.

We'll start a Jupyter Notebook using AWS SageMaker.  We'll then use the Jupyter Notebook to process all the steps required to predict aircraft in the satellite imagery.

Steps:  
Create your AWS SageMaker Jupyter Notebook  
Open Jupyter Notebook Instance  
Checkout project from GitHub using Jupyter Notebook  
Run Jupyter Notebook Steps  

## Create your AWS SageMaker Jupyter Notebook
Use the AWS Console to configure a AWS SageMaker Notebook.  This is a step by step process.

### AWS SageMaker Console
Click on "Notebook instances"  
Click on "Create notebook instance"  
Notebook instance name: planesnet  
Notebook instance type: ml.t2.medium   
IAM Role: Create a new role  
```
S3 buckets you specify - optional:
Select "Any S3 Bucket"
Click on "Create role"
```
Click on "Create notebook instance"

### AWS IAM Console
Click on "Roles"    
Click on "AmazonSageMaker-ExecutionRole-```<timestamp>```"  
Click on "Permissions/Attach policies"  
Enter "EC2" in "Filter policies"
Select "AmazonEC2ContainerRegistryFullAccess"  
Click on "Attach policy"  

### Open Notebook instance
AWS SageMaker Console  
Click on Notebook/Notebook instances  
Name: planesnet  
Actions: Open  # it will show pending until it's ready to open

This will open the Jupyter Notebook in a new tab in your browser.

## Checkout project from GitHub using Jupyter Notebook
Click on "New" 
Select "terminal"  
cd SageMaker  
git clone https://github.com/kskalvar/aws-sagemaker-planesnet-tflearn-bring-your-own-container.git

Once the project is downloaded, go back to the Jupyter Notebook/Files  
Click on directory "aws-sagemaker-planesnet-tflearn-bring-your-own-container"  
Click on Jupyter Notebook to open it

## Run Jupyter Notebook Steps

## References

Using Your Own Algorithms with Amazon SageMaker  
https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html

planesnet-detector  
https://github.com/rhammell/planesnet-detector

Building your own algorithm container  
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb

[tfl]: http://tflearn.org/
[planesnet]: https://github.com/rhammell/planesnet-detector
