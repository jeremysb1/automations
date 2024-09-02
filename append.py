additional_lines = ['yo mama so fat,\n', 'even her clothes has stretch marks.\n']

with open('poem.txt', 'a') as file:
   # file.write('this is the last line,\n')
    # file.write('jk, yo mama so fat, \n')
    file.writelines(additional_lines)