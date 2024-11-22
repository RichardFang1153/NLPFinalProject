import sys

if (len(sys.argv) != 4):
    print("Not enough arguments")
else:
    word_group = sys.argv[3]
    
    if (sys.argv[2] == 1):
        file = open(sys.argv[1], "r")
        t_output = open("training.POS-chunk", "w")
        

        
        for line in file:
            
            print("hello" , file=t_output)
            
        train_file.close()
        t_output.close()
    
        
    elif (sys.argv[2] == 2):
        
