## Principe de fonctionnment

1/ Navigateur web utiisateur

2/ Cloudfront
  - default behavior : HTTP -> HTTPS + lambda function Sessionchecker

3/ Lambda Sessionchecker

## Déploiement

# Prerequis :
  Nom DNS pour Cloudfront + certificat

# 1/  CF tatooine.yml :
      Params : stage
      Resources :
        bucket source                           ok
        bucket resized                          ok
        bucket web                              ok
        cloudFront (insight : bucket web)       ok
        cognito user pool/user domain/idp       ok
        dynamodb                                tbd
        Output :

# 2/ SAM SessionChecker (fonction à installer dans us-east-1 !!!)
        template :
        Params :
        Resources :
          Serverless function SessionChecker
        Output :
        Code :
          Insight : pool cognito/table dynamodb

# 3/ SAM SessionManager
        template :
        Params :
        Resources :
          apiGateway
          Serverless function SessionManager

# 4/ Manuellement
        Completer la config Cloudfront avec les infos sur la lambda@edge SessionChecker
        completer les infos dynamodb et cognito pool dans le code SessionChekcer ????

## on essaye une autre voie :
  - toutes les infras ensemble dans un seul template CF (tatooine.yml)
  - les fonctions dans les templates SAM
