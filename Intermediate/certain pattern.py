def draw_grid():
    horizontal_line = "+ - - - - + - - - - +"
    vertical_line = "|         |         |"
    
    for _ in range(2):
        print(horizontal_line)
        for _ in range(4):
            print(vertical_line)
            
    print(horizontal_line)

draw_grid()