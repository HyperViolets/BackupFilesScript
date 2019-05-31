# imports the 'os' module: miscellaneous operating system interfaces
import os
import tarfile
import datetime
import hashlib

# strings can be single, double, or triple quote
# triple quote strings can span multiple lines
# variable names can be camelCase, PascalCase, or snake_case
# lists contain multiple items and list size can change - use square brackets '[ ]'
# tuples contain multiple items, but can't be changed - use parenthesis '( )'
# dictionary uses a key and value scheme - format: room = {"Emma": 309, "Jacob": 582, "Olivia": 764}
paths = ('/home/juan/Pictures', '/home/juan/Downloads', '/home/juan/Documents', '/home/juan/Music')
today = datetime.date.today()
counter = 0
total_size = 0
tar_name = '/home/juan/Adam/MediaHDD/Ubuntu/violets_backup' + str(today) + '.tar'

# os.walk searches the directory it is given
# it can return directory paths, directory names, and file names
for backup_path in paths:
    for (dir_path, dir_name, file_name) in os.walk(backup_path):
        for fn in file_name:
            path = os.path.join(dir_path, fn)
            size = os.stat(path).st_size
            counter += 1
            total_size += size
            # print(fn + '    ' + str(size))


def convert_bytes(my_bytes, target_unit, byte_size=1000):
    # method/function that takes in three parameters
    # one parameter is given a default value
    """convert bytes to megabytes, etc.
       sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))
       sample output:
           mb= 300002347.946
    """
    # dictionary (key value pair)
    units = {'kilo_byte': 1, 'mega_byte': 2, 'giga_byte': 3, 'terra_byte': 4, 'peta_byte': 5, 'exa_byte': 6}
    # changing an integer to a float with 'float()'
    result = float(my_bytes)
    # range returns a sequence of numbers
    # continually divides the bytes by 1024 for the desired unit
    for i in range(units[target_unit]):
        result = result / byte_size
    return result


def make_tarfile(output_filename, input_dir):
    with tarfile.open(output_filename, "w") as tar:
        for directory in input_dir:
            print('Archiving: ' + directory)
            tar.add(directory, arcname=os.path.basename(directory))


make_tarfile(tar_name, paths)

with open(tar_name, "rb") as f:
    tar_bytes = f.read()  # read entire file as bytes
    sha256_hash = hashlib.sha256(tar_bytes).hexdigest()
    sha1_hash = hashlib.sha1(tar_bytes).hexdigest()
    md5_hash = hashlib.md5(tar_bytes).hexdigest()
    hash_file = open('/home/juan/Adam/MediaHDD/Ubuntu/BackupHashes.txt', 'a')
    hash_file.write(tar_name + '\nSHA256: ' + sha256_hash + '\nSHA1: ' + sha1_hash + '\nMD5: ' + md5_hash + '\n\n')
    hash_file.close()

print('Total Files Found: ' + str(counter))
print('Total Size: ' + str(convert_bytes(total_size, 'giga_byte')) + ' GB')
print('DONE')


