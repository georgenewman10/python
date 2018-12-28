import subprocess

output = subprocess.getoutput('ls')
print output

num = output.count('d')
print num

