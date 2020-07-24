import boto3
import time
import logging
import uuid
from boto3.dynamodb.conditions import Key
def lambda_handler(event, context):
    message = event
    expiryTimestamp = int(time.time() +15*60)
    client = boto3.resource('dynamodb')
    table = client.Table("csye6225")
    username = event['Records'][0]['Sns']['MessageAttributes']['email']['Value']
    token = uuid.uuid1()
    try:
        response = table.scan()
        for x,y in response.items():
            if x=='Items':
                for a in y:
                    for c,d in a.items():
                        if c=='username' and d==username:
                            return 0
    except Exception as e:
        print(e)
    else:
        id=uuid.uuid1()
        table.put_item(Item= {'id':str(id) ,'username':  username , 'token':str(token) , 'TimeToExist': (expiryTimestamp) })
        SENDER = "support@prod.sapnapatel.me"
        RECIPIENT = username
        AWS_REGION = "us-east-1"
        SUBJECT = "Password Reset Link"
        BODY_TEXT = ("Your Link to Reset Password : prod.sapnapatel.me/?email={a}&token={b}".format(a=username,b=token))
        CHARSET = "UTF-8"
        emailclient = boto3.client('ses',region_name=AWS_REGION)
        response = emailclient.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    return(message)