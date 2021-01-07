## Principe de fonctionnment

1/ Navigateur web utiisateur

2/ Cloudfront
  - default behavior : HTTP -> HTTPS + lambda function Sessionchecker

3/ Lambda Sessionchecker

## Déploiement

# Prerequis :
  Nom DNS pour Cloudfront + certificat

# CF tatooine.yml :
  template :
    Params : 
    Resources :
      bucket source
      bucket resized
      cognito user
      dynamodb
    Output :

# SAM SessionChecker
  template :
    Params :
    Resources :
      bucket web
      Serverless function SessionChecker
      cloudFront (insight : bucket web / SessionChecker)
    Output :
  code :
    Insight : pool cognito/table dynamodb

# SAM SessionManager
  template :
    Params :
    Resources :
      apiGateway
      Serverless function SessionManager
