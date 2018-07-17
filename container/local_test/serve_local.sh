#!/bin/sh

machine="$(uname -s)"
image=$1

case $machine in
     *CYGWIN*)
         docker run --name ${image} -v /c/Users/$USER/git/aws-sagemaker-planesnet-tflearn-bring-your-own-container/container/local_test/test_dir:/opt/ml -p 8080:8080 --rm ${image} serve;;
     *)
         docker run --name ${image} -v $(pwd)/test_dir:/opt/ml -p 8080:8080 --rm ${image} serve;;
esac
