from kafka import KafkaConsumer
import json
import boto3



def put_items(id , tweet  , dynamodb=None):
   if not  dynamodb :
     dynamodb = boto3.resource("dynamodb")

   table = dynamodb.Table("Tweets")
   response = table.put_item(Item={'_id': id , 'tweet': tweet})

   print(response)

topic_name ='firsttopic"'

consumer = KafkaConsumer("firsttopic",bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
 tweets = json.loads(json.dumps(message.value)) # convert json format to python object
 with open("kafka.json","a") as file:
  json.dump(tweets , file) # convert python object to json format
 put_items(int(tweets['id']),tweets['text'] )
 print(tweets['id'] , tweets['text'])