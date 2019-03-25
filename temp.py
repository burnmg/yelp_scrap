from __future__ import print_function # Python 2/3 compatibility

import datetime

import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('yelp-restaurants')

with open("/Users/rl/PycharmProjects/yelp_scrap/data/yelp-restaurants.json", "r") as reader:
    data = json.loads(reader.read(), parse_float=decimal.Decimal)

    t = ""

