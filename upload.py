from __future__ import print_function # Python 2/3 compatibility

import datetime

import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('yelp-restaurants')

with open("/Users/rl/PycharmProjects/yelp_scrap/data/yelp-restaurants.json", "r") as reader:
    data = json.loads(reader.read(), parse_float=decimal.Decimal)

    # Loop through the JSON objects

    count = 1
    for item in data["yelp-restaurants"]:
        # resolve empty string

        for element in item["location"]:
            if not item["location"][element] or len(item["location"][element]) < 1:
                item["location"][element] = None

        table.put_item(Item={
            "insertedAtTimestamp": str(datetime.datetime.now().timestamp()),
            "Business ID": item["id"],
            "Name": item["name"],
            "Address": item["location"],
            "Coordinates": item["coordinates"],
            "Number of Reviews": item["review_count"],
            "Rating": item["name"],
            "Zip Code": item["location"]["zip_code"],
            "Cuisine": item["cuisine"]
        })
        print("insert:" + str(count))
        count += 1
