import boto3

def lambda_handler(event, context):
    # Entrada (json)
    servicio_id = event['body']['servicio_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('servicios')
    response = table.delete_item(
        Key={
            'servicio_id': servicio_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
