output "table_name" {
  value = aws_dynamodb_table.notes.name
}

output "function_name" {
  value = aws_lambda_function.api.function_name
}

output "api_url" {
  value = aws_apigatewayv2_api.notes.api_endpoint
}