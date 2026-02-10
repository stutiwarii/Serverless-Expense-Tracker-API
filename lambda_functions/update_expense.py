import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Expenses')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    expense_id = event['pathParameters']['id']
    update_expr = "SET title=:t, amount=:a, date=:d"
    expr_values = {
        ':t': data['title'],
        ':a': data['amount'],
        ':d': data['date']
    }
    table.update_item(
        Key={'id': expense_id},
        UpdateExpression=update_expr,
        ExpressionAttributeValues=expr_values
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Expense updated'})
    }
