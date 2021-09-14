## Principe de fonctionnment

1/ Navigateur web utiisateur

2/ Cloudfront
  - default behavior : HTTP -> HTTPS + lambda function Sessionchecker

3/ Lambda Sessionchecker

## Déploiement

# Prerequis :
  Nom DNS pour Cloudfront + certificat

# 1/  CF tatooine.yml :
      template :
      Params :
      Resources :
        bucket source
        bucket resized
        bucket web
        cloudFront (insight : bucket web)
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
          cognito user pool
          cognito user pool Domain
          cognito user pool Client
          dynamodb
          apiGateway
          Serverless function SessionManager

# 4/ Manuellement
        Completer la config Cloudfront avec les infos sur la lambda@edge SessionChecker
        completer les infos dynamodb et cognito pool dans le code SessionChekcer ????

## on essaye une autre voie :
  - toutes les infras ensemble dans un seul template CF (tatooine.yml)
  - les fonctions dans les templates SAM

# Pré-requis
  - domaine DNS :
    auth.tatooine.net :
      tatooinelabs.auth.tatooine.net CNAME (alias donné par cognito)
      tatooine.auth.tatooine.net CNAME (alias donné par cognito)
  - certificat :
    cloudfront :        tatooinelabs.zoubix.net/tatooine.zoubix.net                 us-east-1
    cognito domain :    tatooinelabs.auth.zoubix.net/tatooine.auth.zoubix.net   us-east-1
