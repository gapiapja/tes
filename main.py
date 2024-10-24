import os

def make_commit(days: int):
     if days < 1:
        os.system('git push')
     else:
        dates = f'{days} days ago'
        
        with open('data.txt', 'a') as file:
            file.write(f'{days}\n')
            
        os.system('git add data.txt')
        
        os.system('git commit --data="'+dates+'" -m "First Commit"')
        
        return days * make_commit(days-1)
        
make_commit(360)