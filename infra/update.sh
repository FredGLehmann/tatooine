aws cloudformation update-stack --stack-name tatooinelabs --template-body file://tatooine.yml --parameters ParameterKey=Stage,ParameterValue=stagging --capabilities CAPABILITY_AUTO_EXPAND
