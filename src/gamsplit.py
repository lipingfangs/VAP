import json
import sys
import os 
def extract_node_id(filename):
    nodelist = []
    node_ids = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            json_object = json.loads(line)
            mappings = json_object.get('path', {}).get('mapping', [])
            name =  json_object.get('name')
            node_ids = [name]
            for mapping in mappings:
                node_ids.append(mapping.get('position', {}).get('node_id'))
          #  print(node_ids)
            count = 2
            if len(node_ids) > 2:
                for i in node_ids[1:-1]:
                   # print()
                    if abs(int(node_ids[count]) - int(i)) > 10:
                        nodelist.append([node_ids[0],node_ids[count],i])
                        break 
                    count +=1
            node_ids = []
            #print()
    return nodelist

filename = sys.argv[1]
node_ids = extract_node_id(filename)
