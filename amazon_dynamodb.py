
import boto3
import pprint
from  botocore.exceptions import ClientError

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='Tweets',
        KeySchema=[
            {
                'AttributeName': '_id',
                'KeyType': 'HASH'  # Partition key
            },
            {'AttributeName': 'tweet' ,
             'KeyType':'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': '_id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'tweet',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status)