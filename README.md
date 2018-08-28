# AWS SageMaker PlanesNet TFLearn Bring Your Own Container

This example shows how to package the [TFLearn][tfl] Machine Learning Library for use with SageMaker. We have also chosen the [PlanesNet][planesnet] planesnet-detector project implementation which uses TFLearn to detect aircraft in an image and highlighted with a bounding box.

## References

Using Your Own Algorithms with Amazon SageMaker  
https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html

planesnet-detector  
https://github.com/rhammell/planesnet-detector

Building your own algorithm container  
https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb

[tfl]: http://tflearn.org/
[planesnet]: https://github.com/rhammell/planesnet-detector
