import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Expenses')

def lambda_handler(event, context):
    expense_id = event['pathParameters']['id']
    table.delete_item(Key={'id': expense_id})
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Expense deleted'})
    }
