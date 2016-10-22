"""This is the entry point of the program."""



def create_box(height, width, character):
    box= ''
    if height < 1 or width < 1:
        return 'Error'
    for x in range(height):
        box+= character*width+'\n'
    return box


'''
def create_box(height, width, character):
    full_row = character * width
    edge_row = character + ' '*(width-2) + character
    interior = ''
    
    if height < 1 or width < 1:
        return 'Error'
    for x in range(1, height-1):
        interior += edge_row+'\n'
    
    box = (full_row+'\n') + (interior) + (full_row)
    
    return box
    
lebox=create_box(10, 3, '7')
print(lebox)
'''