#!/usr/bin/env bash

gcloud config set project signature-builder-224020
base=$PWD

# Update functions
cd functions && zip -r functions.zip . && mv functions.zip $base/static/
cd $base

# Update bucket
gsutil -m cp -r static/* gs://notbinary-signature-builder
rm static/functions.zip

# Deploy functions
# TODO: deploy from a source repo?
region="--region=europe-west1"
options="--runtime=python37 --source=gs://notbinary-signature-builder/functions.zip --memory=128MB --trigger-http"
gcloud functions deploy plain          ${region} ${options} --entry-point=plain
gcloud functions deploy now-soon-later ${region} ${options} --entry-point=now_soon_later
gcloud functions deploy with-strapline ${region} ${options} --entry-point=with_strapline
