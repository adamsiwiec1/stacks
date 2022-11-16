rm -rf tmp
aws --endpoint-url=http://localhost:4566/ s3 ls
aws --endpoint-url=http://localhost:4566/ s3 mb s3://testing
aws --endpoint-url=http://localhost:4566/ s3 ls
aws --endpoint-url=http://localhost:4566/ s3 cp aws-compose.yml s3://testing
aws --endpoint-url=http://localhost:4566/ s3 ls s3://testing
aws --endpoint-url=http://localhost:4566/ s3 cp  s3://testing/aws-compose.yml tmp/