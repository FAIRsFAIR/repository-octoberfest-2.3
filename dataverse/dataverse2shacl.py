import sys
import csv
from collections import namedtuple
from itertools import tee

Property = namedtuple("Property", "datasetField, name, title, description, watermark, fieldType, displayOrder, displayFormat, advancedSearch, allowControlledVocabulary, allowmultiples, facetable, displayoncreation, required, parent, metadatablock_id, termURI")

fieldTypeMapping = {
    "text": "sh:Literal",
    "textbox": "sh:Literal",
    "date": "sh:Literal",
    "url": "sh:IRI"
}

skipHeaderRowCount = 3
skipCount = 0

shapes = {}

if len(sys.argv) < 2:
    print(f"Expected csv file parameter!")
    print(f"\tpython3 {sys.argv[0]} my-dataverse-schema.csv")
    sys.exit(1)

for p in map(Property._make, csv.reader(open(sys.argv[1], "r"))):
    if skipCount < skipHeaderRowCount:
        skipCount += 1
        continue

    if p.datasetField == '#controlledVocabulary':
        break
    
    if p.parent not in shapes:
        shapes[p.parent] = []

    shape = {
        "path": p.termURI,
        "name": p.title,
        "description": p.description,
        "minCount": 1 if p.required == 'TRUE' else None,
        "maxCount": None if p.allowmultiples == 'TRUE' else 1,
        "node": p.name + "Shape" if p.fieldType == 'none' else None,
        "nodeKind": fieldTypeMapping[p.fieldType] if p.fieldType in fieldTypeMapping else None
    }

    shapes[p.parent].append(shape)

print("@prefix sh: <http://www.w3.org/ns/shacl#> .")
print("@prefix : <http://example.com/> .")
print()

for name, propshapes in shapes.items():
    print(f":{name if name != '' else 'Citation'}Shape a sh:NodeShape ;")
    print(f"  #TODO sh target")

    for i, shape in enumerate(propshapes, start=1):
        print(f"  sh:property [")
        print(f"    sh:path <{shape['path']}> ;")
        print(f"    sh:name \"{shape['name']}\" ;")
        print(f"    sh:description \"{shape['description']}\" ;")
        if shape["minCount"]:
            print(f"    sh:minCount {shape['minCount']} ;")
        if shape["maxCount"]:
            print(f"    sh:maxCount {shape['maxCount']} ;")
        if shape["node"]:
            print(f"    sh:node :{shape['node']}Shape ;")
        if shape["nodeKind"]:
            print(f"    sh:nodeKind {shape['nodeKind']} ;")
        print(f"  ] {';' if i < len(propshapes) else '.'}")
    print() # newline for easier reading
