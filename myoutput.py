import subprocess

def WriteMyOutput():
    with open('mypython_output.txt', 'w') as file:
        p = subprocess.run(['python', 'C:\\Users\\drpre\\OneDrive\\Desktop\\teams\\sem4\\mpr\\MPR\\interpreter_main.py'], stdout=file, stderr=file, text=True)





