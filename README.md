# Sqla-filters-json

![AzurePipeline](https://marc-aurele.visualstudio.com/sqla-filters/_apis/build/status/MarcAureleCoste.sqla-filters-json)

Add json parser to the sqla-filters package.

## Introduction 

This package 

## Installation

```bash
pip install sqla-filter-json
```

## Getting Started

### JSON format

```json
{
    "type": "and",
    "data": [
        {
            "type": "or",
            "data": [
                {
                    "type": "operator",
                    "data": {
                        "attribute": "name",
                        "operator": "eq",
                        "value": "toto"
                    }
                },
                {
                    "type": "operator",
                    "data":{
                        "attribute": "name",
                        "operator": "eq",
                        "value": "tata"
                    }
                }
            ]
        },
        {
            "type": "operator",
            "data": {
                "attribute": "age",
                "operator": "eq",
                "value": 21
            }
        }
    ]
}
```
:warning: Json format can change in the futur. :warning:



Create an instance of the JSONFilterParser with the json string.

Example:
```python
# Sqlalchemy setup ... + model definition

# Create a JSON parser instance
parser = JSONFiltersParser(raw_json_string)

# you now have a tree available as a property in the parser
print(parser.tree)

# You can finaly filter your query
query = session.query(Post)
filtered_query = parser.tree.filter(query)

# Get the results
query.all()
```

### Result tree

```
                                      +----------------------+
                                      |                      |
                                      |          and         |
                                      |                      |
                                      -----------------------+
                                                 ||
                                                 ||
                                                 ||
                    +----------------------+     ||     +----------------------+
                    |                      |     ||     |                      |
                    |          or          <------------>      age == 21       |
                    |                      |            |                      |
                    +----------------------+            +----------------------+
                               ||
                               ||
                               ||
+----------------------+       ||       +----------------------+
|                      |       ||       |                      |
|     name == toto     <---------------->     name == tata     |
|                      |                |                      |
+----------------------+                +----------------------+
```

# Contribute

Fork the repository and run the following command to install the dependencies and the dev dependencies.

`pip install -e '.[dev]'`
