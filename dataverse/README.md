# dataverse2shacl.py

## requirements
- python3

## quickstart
Export a dataverse schema from google spreadsheet as a csv file, and invoke the script:

```bash
python3 dataverse2shacl.py my-dataverse-schema.csv > schema.ttl
```

## todo
- sheets other than `Citation` are missing the `termURI` column
- add missing predicates
  - some can be mapped based on the `metadatablock_id` column
