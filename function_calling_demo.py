from solve_it.solve_it_library import KnowledgeBase
kb = KnowledgeBase('solve_it', 'solve-it.json')

technique = kb.get_technique("T1002")
print("====================")
print("The technique's object type is: " + str(type(technique)))
print("====================")
print("The content of the technique is: ")
print(technique)

'''
Try other functions from the README in SOLVE-IT at: 
solve-it/solve_it_library/README.md
'''