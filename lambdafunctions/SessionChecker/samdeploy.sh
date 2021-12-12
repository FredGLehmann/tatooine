sam build
sam package --s3-bucket zbx-us-tmp --s3-prefix SessionCheckerFunction --output-template-file package.yaml --region us-east-1
sam deploy --stack-name tatooinelabs-sessionchecker --template-file package.yaml --region us-east-1 --parameter-overrides Stage=stagging --capabilities CAPABILITY_IAM
