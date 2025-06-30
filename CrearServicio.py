import boto3

def lambda_handler(event, context):
    # Entrada (json)
    servicio = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('servicios')
    response = table.put_item(Item=servicio)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
