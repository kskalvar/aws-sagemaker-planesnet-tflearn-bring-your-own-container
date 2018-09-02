# AWS SageMaker PlanesNet TFLearn Bring Your Own Container

This example shows how to package the [TFLearn][tfl] Machine Learning Library for use with SageMaker. TFLearn is not supported by SageMaker currently so we'll need to build a container to support it.  This solution will use the SageMaker Python SDK to build a distributed service to train/deploy/detect.  We have also chosen the [PlanesNet][planesnet] planesnet-detector project implementation which uses TFLearn to detect aircraft in an image and highlighted with a bounding box.

This solution shows how to process satellite imagery using AWS SageMaker and PlanesNet to build an AI Model to predict aircraft. This readme updates an article "Detect airplanes in Planet imagery using machine learning" by Bob Hammell referenced below and provides a more basic step by step process.

We'll start a Jupyter Notebook using AWS SageMaker.  We can then use the Jupyter Notebook to process all the steps required to predict aircraft in the satellite imagery.

## Configure AWS SageMaker
Use the AWS Console to configure a SageMaker Instance for processing satellite data.  This is a step by step process.

### AWS SageMaker Dashboard
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

### AWS IAM Dashboard
Click on "Roles"    
Click on "AmazonSageMaker-ExecutionRole-<timestamp>"  
Click on "Permissions/Attach policies"  
Enter "EC2" in "Filter policies"
Select "AmazonEC2ContainerRegistryFullAccess"  
Click on "Attach policy"  

#### Display Notebook instances using the SageMaker Dashboard
Notebook/Notebook instances  
Name: planesnet  
Actions: Open  # it will show pending until it's ready to open

This will open the Jupyter Notebook in a new tab in your browser.

#### Upload aws-sagemaker-planesnet.ipynb using Jupyter Notebook
Click on "Upload" and Select "aws-sagemaker-planesnet.ipynb" from project jupyter-notebook directory 

Once the notebook is uploaded, click on "aws-sagemaker-planesnet.ipynb" to open it.  
Run each cell Step by Step

## References

Using Your Own Algorithms with Amazon SageMaker  
https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html

planesnet-detector  
https://github.com/rhammell/planesnet-detector

Building your own algorithm container  
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb

[tfl]: http://tflearn.org/
[planesnet]: https://github.com/rhammell/planesnet-detector
