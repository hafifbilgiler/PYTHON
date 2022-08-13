import yaml
import json

with open('./test.yaml', 'r') as file:#READ THE YAML FILES to CONVERT
    configuration = yaml.safe_load(file)
with open('test.json', 'w') as json_file: #OPEN THE JSON FILE WITH JSON FORMAT
    json.dump(configuration, json_file)

output = json.dumps(json.load(open('./test.json')), indent=2)
print(output)