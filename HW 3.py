import os
import shutil
from multiprocessing import Pool
import argparse

def copy_file(file_path, target_dir):
    filename = os.path.basename(file_path)
    target_path = os.path.join(target_dir, filename)
    shutil.copy2(file_path, target_path)

def process_directory(args):
    source_dir, target_dir = args
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            target_subdir = os.path.join(target_dir, ext[1:])
            os.makedirs(target_subdir, exist_ok=True)
            copy_file(file_path, target_subdir)

def main():
    parser = argparse.ArgumentParser(description='Process junk directory.')
    parser.add_argument('source_dir', type=str, help='Path to the source directory')
    parser.add_argument('target_dir', type=str, nargs='?', default='dist', help='Path to the target directory (default: dist)')
    args = parser.parse_args()

    source_dir = args.source_dir
    target_dir = args.target_dir

    os.makedirs(target_dir, exist_ok=True)

    num_processes = os.cpu_count()
    pool = Pool(processes=num_processes)

    pool.map(process_directory, [(source_dir, target_dir)])

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
    
    
