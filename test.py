import os
import nester
import pickle


os.chdir('HeadFirstPython/chapter3')
man = []
other = []
try:
    with open('sketch.txt') as data:    
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                else:
                    other.append(line_spoken)
            except:
                pass
except IOError:
    print('The datafile is missing')


try:
    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man, man_file)
    with open('other_data.txt', 'wb') as other_file:
        pickle.dump(other, other_file)
except IOError:
    print('File error')
except pickle.PickleError as perr:
    print("pickle.PickleError:" + str(perr))
