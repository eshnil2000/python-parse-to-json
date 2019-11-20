import ast
import astor
import os.path
save_path = '/output/'

with open('test2.py') as source:
	tree=ast.parse(source.read())

for statement in tree.body:
     print(ast.dump(statement))
     print("\n")

imports=[]
functions=[]
assignments=[]
function_calls=[]

for statement in tree.body:
	print(ast.dump(statement))
	if(isinstance(statement,ast.Import)):
		imports.append(statement)
	if(isinstance(statement,ast.FunctionDef)):
		functions.append(statement)
	if(isinstance(statement,ast.Assign)):
		assignments.append(statement)
	if(isinstance(statement,ast.Expr) or isinstance(statement,ast.Expr)):
		function_calls.append(statement)


i=0
for func_call in function_calls:
	print(function_calls)
	src_list=imports+functions+[func_call]
	src=astor.to_source(ast.Module(src_list))
	f= "file"+str(i)
	file_write=os.path.join(save_path, f)
	print(file_write)
	g=open(file_write,"w+")
	g.write(src)
	g.close()
	i+=1
