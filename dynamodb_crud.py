
# get all items
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name="eu-west-3")

table = dynamodb.Table('my-table')

response = table.scan()
data = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])



# get item

import boto3
dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')

table = dynamodb.Table('my-table')

response = table.get_item(Key={
    '_id': "ID-1",
  'name': "SORT_2"
})


# put item

import boto3
dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')

table = dynamodb.Table('my-table')

response = table.put_item(
    Item={
        'id': 1,
        'title': 'my-document-title',
        'content': 'some-content',
    }
)

# query for items

import boto3
dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')

table = dynamodb.Table('my-table')

response = table.query(
    KeyConditionExpression=Key('id').eq(1)
)

for i in response['Items']:
    print(i['title'], ":", i['description'])




# update item
import boto3
dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')

table = dynamodb.Table('my-table')

response = table.update_item(
    Key={
        'id': '894673'
    },
    UpdateExpression='SET country = :newCountry',
    ExpressionAttributeValues={
        ':newCountry': "Canada"
    },
    ReturnValues="UPDATED_NEW"
)


# delete item


import boto3
dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')

table = dynamodb.Table('my-table')

response = table.table.delete_item(Key={
    'primaryKeyName': 'primaryKeyValue'
})




# delete all items


import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-3')
table = dynamodb.Table('my-table')

with table.batch_writer() as batch:
     # Iterate through table until it's fully scanned
    while scan is None or 'LastEvaluatedKey' in scan:
        if scan is not None and 'LastEvaluatedKey' in scan:
            scan = table.scan(
                ProjectionExpression='yourPrimaryKey', # Replace with your actual Primary Key
                ExclusiveStartKey=scan['LastEvaluatedKey'],
            )
        else:
            scan = table.scan(ProjectionExpression='yourPrimaryKey')

        for item in scan['Items']:
            batch.delete_item(Key={'yourPrimaryKey': item['yourPrimaryKey']})