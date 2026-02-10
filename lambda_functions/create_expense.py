import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Expenses')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    expense_id = str(uuid.uuid4())
    item = {
        'id': expense_id,
        'title': data['title'],
        'amount': data['amount'],
        'date': data.get('date', str(datetime.now().date()))
    }
    table.put_item(Item=item)
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Expense added', 'id': expense_id})
    }
