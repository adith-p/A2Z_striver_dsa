for i in range(2,22):
    with open(f'pattern{i}.py','w') as file:
        line = f'#pattern{i}'
        
        file.write(line)
    