import os # importing OS module
import urllib.request # importing the library for url retrieves

print(os.getcwd()) # Outputs current working directory
print(os.listdir()) # Lists out the cwd's files
print(os.listdir('.')) #relative path
print(os.listdir('/Users/Manish/Desktop/ZerotoPandas/Jovian_Zero_to_Pandas')) # Absolute path

# print(help(os.listdir())) # documentation for the function

os.makedirs("./data", exist_ok=True)

print(os.listdir())

url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

urllib.request.urlretrieve(url1,'./data/loans1.txt')
urllib.request.urlretrieve(url2, './data/loans2.txt')
urllib.request.urlretrieve(url3, './data/loans3.txt')


