import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')

db = dynamodb.Table('Music')

print(db)


allArtist = db.scan()
print(allArtist)