# Mock any AWS service!
* [Localstack](https://docs.localstack.cloud/overview/) allows you to fully mock instances of AWS services locally using Docker.
*  The back-end of Localstack is based on [moto](https://pypi.org/project/moto/), the mocking library for [boto](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [Localstack's moto fork.](https://github.com/localstack/moto)

### Links
* [speadsheet with local stack support](https://docs.google.com/spreadsheets/d/1CiBcRvXMy6jSyrA5A7vOiZiFHQZUjw5ILA3ysU_FsFg/edit?usp=sharing)
* [localstack configuration](https://docs.localstack.cloud/localstack/configuration/)
* [speadsheet with local stack support](https://docs.google.com/spreadsheets/d/1CiBcRvXMy6jSyrA5A7vOiZiFHQZUjw5ILA3ysU_FsFg/edit?usp=sharing)

## Setup
1. Create a persistent volume in a directory of your choice. I used `/mnt/e/docker/volumes/localstack`.
```
$ docker volume create --driver local \
    --opt type=none \
    --opt device=/mnt/e/docker/volumes/localstack \
    --opt o=bind localstack-volume
```
2. Clone the project, cd into the `aws-local` directory, and start the container with docker compose.
```
$ git clone https://github.com/adamsiwiec1/stacks.git
$ cd aws-local
$ docker compose -f aws-compose.yml up -d
```
3. [Download the AWS CLI.](https://aws.amazon.com/cli/)

4. Test your connection with `s3-example.sh`.
```
$ bash examples/cli/s3-example.sh
```
