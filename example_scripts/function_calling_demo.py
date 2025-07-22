from solve_it.solve_it_library import KnowledgeBase
kb = KnowledgeBase('solve_it', 'solve-it.json')

technique = kb.get_technique("T1002")
print("====================")
print("The technique's object type is: " + str(type(technique)))
print("====================")
print("The content of the technique is: ")
print(technique)
print("====================")
print("Elements of the technique can be extracted as dictionary key/value pairs")
print(technique['id'])
print(technique['name'])

'''
Try other functions from the README in SOLVE-IT at: 
solve-it/solve_it_library/README.md
'''