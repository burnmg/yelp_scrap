import json
def read(file):

    with open(file, "r") as reader:
        str = reader.read()
        j = json.loads(str)
    return j

j1 = read("/Users/rl/PycharmProjects/yelp_scrap/data/Chinese")
j2 = read("/Users/rl/PycharmProjects/yelp_scrap/data/Italian")
j3 = read("/Users/rl/PycharmProjects/yelp_scrap/data/Western")
j4 = read("/Users/rl/PycharmProjects/yelp_scrap/data/Japanese")
j5 = read("/Users/rl/PycharmProjects/yelp_scrap/data/Mexico")

with open("/Users/rl/PycharmProjects/yelp_scrap/data/yelp-restaurants.json", "w") as writer:
    final_file = {}
    combined = []
    for item in j1:
        item["cuisine"] = "Chinese"
        combined.append(item)
    for item in j2:
        item["cuisine"] = "Italian"
        combined.append(item)
    for item in j3:
        item["cuisine"] = "Western"
        combined.append(item)
    for item in j4:
        item["cuisine"] = "Japanese"
        combined.append(item)
    for item in j5:
        item["cuisine"] = "Mexico"
        combined.append(item)

    output_dict = {}
    output_dict["yelp-restaurants"] = []
    for item in combined:
        output_dict["yelp-restaurants"].append(item)
    json.dump(output_dict, writer)

