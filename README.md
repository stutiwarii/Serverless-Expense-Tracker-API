# Serverless-Expense-Tracker-API

# Serverless Expense Tracker API

A cloud-based REST API to automate personal expense tracking using serverless architecture.

## Features
- Add, update, delete, and view expenses.
- Secure, scalable API via AWS API Gateway.
- Real-time expense updates using AWS Lambda and DynamoDB.

## Tech Stack
- AWS Lambda
- AWS API Gateway
- DynamoDB
- Python (Flask optional)

## Usage
1. Deploy Lambda functions on AWS.
2. Configure API Gateway routes for each function.
3. Use POST/GET/PUT/DELETE requests to manage expenses.

## Example
```bash
# Add an expense
curl -X POST https://<api-gateway-url>/expenses \
-H "Content-Type: application/json" \
-d '{"title": "Groceries", "amount": 500, "date": "2025-10-12"}'

# Get all expenses
curl https://<api-gateway-url>/expenses
