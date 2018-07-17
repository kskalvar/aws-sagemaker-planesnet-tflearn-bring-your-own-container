#!/bin/sh

machine="$(uname -s)"
image=$1

mkdir -p test_dir/model
mkdir -p test_dir/output

rm -f test_dir/model/*
rm -f test_dir/output/*

case $machine in
     *CYGWIN*)
         docker run -v /c/Users/$USER/git/aws-sagemaker-planesnet-tflearn-bring-your-own-container/container/local_test/test_dir:/opt/ml --rm ${image} train;;
     *)
         docker run -v $(pwd)/test_dir:/opt/ml --rm ${image} train;;
esac
