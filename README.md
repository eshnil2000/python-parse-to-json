# Break Python Source code into separate code modules

###-----
### STEP #1 Use ast module to convert code to ast
```
import ast
with open('testsmall.py') as source:
     tree=ast.parse(source.read())
```
### STEP #2 Split statements of ast, convert to ast Module, then convert to python code
```
for statement in tree.body:
     y=ast.Module([statement])
     astor.to_source(y)
```

### STEP #3 Identify as imports
```
for statement in tree.body:
     if(isinstance(statement,ast.Import)):
             print(statement)
 
```

### STEP #4 Identify functions
```
for statement in tree.body:
     if(isinstance(statement,ast.FunctionDef)):
             print(statement)
```
### STEP 5 Identify Expressions 
```
for statement in tree.body:
     if(isinstance(statement,ast.Expr)):
             print(statement)
```

### STEP 6 Identify Assignments (example: g=add(4,5))
```
for statement in tree.body:
     if(isinstance(statement,ast.Assign)):
             print(statement)
```

### STEP 7 Identify Function calls (example: print(g)) 
```
for statement in tree.body:
     if(isinstance(statement,ast.Expr)):
             if(isinstance(statement.value,ast.Call)):
                     print(statement)
```

### STEP 7 Identify Comments/ strings
```
for statement in tree.body:
     if(isinstance(statement,ast.Expr)):
             if(isinstance(statement.value,ast.Str)):
                     print(statement)
```

### STEP 8: WRITE SOURCE CODE to separate files
```
i=0
for statement in tree.body:
     y=ast.Module([statement])
     z=astor.to_source(y)
     f= "file"+str(i)
     g=open(f,"w+")
     g.write(z)
     g.close()
     i+=1
```

### STEP 9: Find which functions are called in each of the Assignment statements

```
for statement in tree.body:
     if(isinstance(statement,ast.Assign)):
             print(statement.value.func.id)
```
### STEP 10: Match functions that are called in assignment statements
```
for statement in tree.body:
	if(isinstance(statement,ast.Assign)):
			print(statement.value.func.id)
			match=statement.value.func.id
			for statement in tree.body:
				if(isinstance(statement,ast.FunctionDef)):
					if(match==statement.name):
						print(statement.name)
```                              
###-----

# python-parse-to-json

Parse Python code to an AST in JSON format, based upon https://github.com/m-labs/pythonparser/

Created on 2017-01-20 by Philip Guo

15-minute tutorial video: https://www.youtube.com/watch?v=wK_VVajpolI

---

### Use Python2
```python parse_python_to_json.py --pyfile=testsmall.py >testsmall.json```

### ast tutorial https://greentreesnakes.readthedocs.io/en/latest/nodes.html
```
>>> tree = ast.parse("print('hello world')")
>>> tree
<_ast.Module object at 0x9e3df6c>
>>> exec(compile(tree, filename="<ast>", mode="exec"))
hello world
```
### In python:
```
import json
with open('testsmall.json') as json_file:
   data = json.load(json_file) 
# To access json entries: 
data['body'][0]['name']
#returns 'Add'
data['body'][0]['args']['args'][0]['arg']
#returns 'x'
data['body'][0]['args']['args'][1]['arg']
# returns  'y'
data['body'][0]['body'][0]['value']['_fields']
#returns ['left', 'op', 'right']
data['body'][0]['body'][0]['value']['type']
#returns 'BinOp'
data['body'][0]['body'][0]['value']['op']['type']
#returns 'Add'

```
# Contents of testsmall.py:
```
def add(x, y):
    return x + y
```

### To get source from AST, Use Astor module
```
import ast
import astor
example = """def add(x, y):
...     return x + y"""
tree = ast.parse(example)
ast.dump(tree)
for statement in tree.body:
...     print(ast.dump(statement), '\n')
print(astor.to_source(tree))
```

### Astor to convert source to AST, extract functions https://suhas.org/function-call-ast-python/
```
import ast
import astor
x=astor.parse_file("testsmall.py")
print(x)
for statement in x.body:
     print(ast.dump(statement))

```
### Extract statements from ast: x contains list of lists
```
>>> x=[]
>>> y=0
>>> for statement in tree.body:
...     x.append([ast.dump(statement)])
...     print(y)
...     y+=1
```

### Find instance of:
```
for statement in tree.body:
...     if isinstance(statement,ast.Expr):
...             print(statement)
```

### Get function names:
```
for statement in tree.body:
...     if isinstance(statement,ast.FunctionDef):
...             print(statement.name)
... 
```
### Count number of functions
```
import ast

with open(filename) as f:
    tree = ast.parse(f.read())
    sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)
```

Forked the HEAD of https://github.com/m-labs/pythonparser/ on 2017-01-20 into here and simplified it.

hello!

Example usage:

```
$ python parse_python_to_json.py --pp '
> def foo(a, b, *c):
>   y = a + (b - c)
>   return y
> '
{
  "body": [
    {
      "body": [
        {
          "loc": {
            "start": {
              "column": 2,
              "line": 3
            },
            "end": {
              "column": 16,
              "line": 3
            }
          },
          "_fields": [
            "targets",
            "value"
          ],
          "type": "Assign",
          "targets": [
            {
              "ctx": null,
              "loc": {
                "start": {
                  "column": 2,
                  "line": 3
                },
                "end": {
                  "column": 3,
                  "line": 3
                }
              },
              "_fields": [
                "id",
                "ctx"
              ],
              "type": "Name",
              "id": "y"
            }
          ],
          "value": {
            "loc": {
              "start": {
                "column": 6,
                "line": 3
              },
              "end": {
                "column": 16,
                "line": 3
              }
            },
            "right": {
              "loc": {
                "start": {
                  "column": 11,
                  "line": 3
                },
                "end": {
                  "column": 16,
                  "line": 3
                }
              },
              "right": {
                "ctx": null,
                "loc": {
                  "start": {
                    "column": 15,
                    "line": 3
                  },
                  "end": {
                    "column": 16,
                    "line": 3
                  }
                },
                "_fields": [
                  "id",
                  "ctx"
                ],
                "type": "Name",
                "id": "c"
              },
              "left": {
                "ctx": null,
                "loc": {
                  "start": {
                    "column": 11,
                    "line": 3
                  },
                  "end": {
                    "column": 12,
                    "line": 3
                  }
                },
                "_fields": [
                  "id",
                  "ctx"
                ],
                "type": "Name",
                "id": "b"
              },
              "_fields": [
                "left",
                "op",
                "right"
              ],
              "type": "BinOp",
              "op": {
                "loc": {
                  "start": {
                    "column": 13,
                    "line": 3
                  },
                  "end": {
                    "column": 14,
                    "line": 3
                  }
                },
                "_fields": [],
                "type": "Sub"
              }
            },
            "left": {
              "ctx": null,
              "loc": {
                "start": {
                  "column": 6,
                  "line": 3
                },
                "end": {
                  "column": 7,
                  "line": 3
                }
              },
              "_fields": [
                "id",
                "ctx"
              ],
              "type": "Name",
              "id": "a"
            },
            "_fields": [
              "left",
              "op",
              "right"
            ],
            "type": "BinOp",
            "op": {
              "loc": {
                "start": {
                  "column": 8,
                  "line": 3
                },
                "end": {
                  "column": 9,
                  "line": 3
                }
              },
              "_fields": [],
              "type": "Add"
            }
          }
        },
        {
          "loc": {
            "start": {
              "column": 2,
              "line": 4
            },
            "end": {
              "column": 10,
              "line": 4
            }
          },
          "_fields": [
            "value"
          ],
          "type": "Return",
          "value": {
            "ctx": null,
            "loc": {
              "start": {
                "column": 9,
                "line": 4
              },
              "end": {
                "column": 10,
                "line": 4
              }
            },
            "_fields": [
              "id",
              "ctx"
            ],
            "type": "Name",
            "id": "y"
          }
        }
      ],
      "loc": {
        "start": {
          "column": 0,
          "line": 2
        },
        "end": {
          "column": 10,
          "line": 4
        }
      },
      "name": "foo",
      "args": {
        "loc": {
          "start": {
            "column": 8,
            "line": 2
          },
          "end": {
            "column": 16,
            "line": 2
          }
        },
        "vararg": {
          "loc": {
            "start": {
              "column": 15,
              "line": 2
            },
            "end": {
              "column": 16,
              "line": 2
            }
          },
          "_fields": [
            "arg",
            "annotation"
          ],
          "type": "arg",
          "annotation": null,
          "arg": "c"
        },
        "args": [
          {
            "loc": {
              "start": {
                "column": 8,
                "line": 2
              },
              "end": {
                "column": 9,
                "line": 2
              }
            },
            "_fields": [
              "arg",
              "annotation"
            ],
            "type": "arg",
            "annotation": null,
            "arg": "a"
          },
          {
            "loc": {
              "start": {
                "column": 11,
                "line": 2
              },
              "end": {
                "column": 12,
                "line": 2
              }
            },
            "_fields": [
              "arg",
              "annotation"
            ],
            "type": "arg",
            "annotation": null,
            "arg": "b"
          }
        ],
        "kwarg": null,
        "defaults": [],
        "kw_defaults": [],
        "kwonlyargs": [],
        "_fields": [
          "args",
          "vararg",
          "kwonlyargs",
          "kwarg",
          "defaults",
          "kw_defaults"
        ],
        "type": "arguments"
      },
      "returns": null,
      "_fields": [
        "name",
        "args",
        "returns",
        "body",
        "decorator_list"
      ],
      "type": "FunctionDef",
      "decorator_list": []
    }
  ],
  "loc": {
    "start": {
      "column": 0,
      "line": 2
    },
    "end": {
      "column": 10,
      "line": 4
    }
  },
  "_fields": [
    "body"
  ],
  "type": "Module"
}
```
