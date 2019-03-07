#!/usr/bin/env bash

PROJECT=`cat ./project.txt`
base=$PWD

gcloud config set project $PROJECT

gsutil iam ch allUsers:objectViewer gs://${PROJECT}
gsutil web set -m index.html -e 404.html gs://${PROJECT}
