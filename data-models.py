import json, yaml, xmltodict, xml.dom.minidom
from pprint import pprint

"""

First is JSON to Dictionary, then print out first Myerscough Family name. This is Change B - the mightest Change!

"""

with open('data.json', 'r') as fj:
    json_data = fj.read()

json_dict = json.loads(json_data)

# pprint(json_dict)

print(json_dict['Family']['Myerscough'][0]['Name'])


"""

Second is to open XML and put into dictionary. XML minidom topretty xml is used to display the XML nicely
Should return 'My Name is Neal'
updated - Also a change B change here!!!

"""

with open('data.xml', 'r') as fx:
    xml_data = fx.read()

xml_dict = xmltodict.parse(xml_data)

# x = xml.dom.minidom.parse('data.xml').toprettyxml()
#
# print(x)

pprint(xml_dict)

print('My name is {}'.format(xml_dict['Family']['Myerscough']['Member'][0]['Name']))


"""

Lastly, creating a dictionary out of a YAML file
adding something else to YAML

"""

with open('data.yaml', 'r') as fy:
    yaml_data = fy.read()

# yaml_text = yaml.dump(json_dict)
# print(yaml_text)

yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)

print(yaml_dict['Family']['Myerscough'][1]['Name'])

