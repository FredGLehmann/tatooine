sam build
sam package --s3-bucket zbx-tmp --s3-prefix SessionManagerFunction --output-template-file package.yaml --region eu-west-3
sam deploy --stack-name tatooinelabs-sessionmanager --template-file package.yaml --region eu-west-3 --parameter-overrides Stage=stagging --capabilities CAPABILITY_NAMED_IAM
