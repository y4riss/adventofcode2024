import sys
import os
import shutil

"""
script to generate boilerplate for a day x

"""
if __name__ == "__main__":

    n = len(sys.argv)
    assert(n == 2)
    assert(sys.argv[1].isnumeric())

    # mkdir dayX
    folder = f"day{sys.argv[1]}"
    os.mkdir(folder)
    
    #creating sample.txt and input.txt
    with open(f"./{folder}/input.txt", 'w') as fp:
        pass
    with open(f"./{folder}/sample.txt", 'w') as fp:
        pass

    solve_template_location = "./solve.py"
    shutil.copy2(solve_template_location, folder)

