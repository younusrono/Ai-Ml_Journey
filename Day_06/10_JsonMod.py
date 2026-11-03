# Java Script Notation

# loads and dumps in this last s means string(dict form)


# i) loads use in python object
# ii) dumps use in convert json string


# Use of loads___


# import json
# json_str='{"name": "Rono","Is_Teacher": true}'
# py_obj=json.loads(json_str)
# print(type(py_obj),py_obj)


# Use of Dumps____

# import json
# py_obj = {
#     "name": "Rono",
#     "IsTeacher": True
# }
# json_str=json.dumps(py_obj)
# print(type(json_str),json_str)

# null will convert in None


# load and dump is used for file types !!!

# i) json load use for file read
# ii) json dump use for file write


# Use of load ____


# import json
# with open("Day_6/10_data.json","r") as f :
#     py_obj=json.load(f)
#     print(type(py_obj),py_obj)


# use of dump_____

import json
data={
    "name":"Rono Ahmad",
    "age":27,
    "IsTeacher": True
}
with open("Day_6/10_data.json","w") as f:
    py_obj=json.dump(data,f)
    print(type(py_obj))