import os
import shutil

def clear_pycache(directory='.'):
    for root, dirs, files in os.walk(directory):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            shutil.rmtree(pycache_path)
        for file in files:
            if file.endswith('.pyc'):
                pyc_file_path = os.path.join(root, file)
                os.remove(pyc_file_path)

if __name__ == "__main__":
    clear_pycache()
