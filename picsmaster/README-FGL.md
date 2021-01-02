# Creation de la clef KMS de cryptage
aws kms create-key --description "Encryption des photos" --key-usage "ENCRYPT_DECRYPT"
=> récupérer le champ "KeyId": "8a09ee3b-318f-4d0b-befb-288159a3c8c8"

# creation de la keypair CloudFront + download private key :
