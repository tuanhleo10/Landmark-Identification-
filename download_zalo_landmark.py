import os
import sys
import zipfile

from six.moves import urllib

_DATA_URL = 'https://dl.challenge.zalo.ai/landmark/train_val2018.zip'
_DATA_TEST_URL = 'https://dl.challenge.zalo.ai/landmark/public_test2018.zip'
_JSON_URL = 'https://dl.challenge.zalo.ai/landmark/train_val2018.json'
dataset_dir = './data'

def download_and_uncompress_zipball(zip_url, dataset_dir):
    filename = zip_url.split('/')[-1]
    filepath = os.path.join(dataset_dir, filename)

    def _progress(count, block_size, total_size):
        sys.stdout.write('\r>> Downloading %s %.1f%%' % (
            filename, float(count * block_size) / float(total_size) * 100.0))
        sys.stdout.flush()
    filepath, _ = urllib.request.urlretrieve(zip_url, filepath, _progress)
    print()
    statinfo = os.stat(filepath)
    print('Successfully downloaded', filename, statinfo.st_size, 'bytes.')
    zip_ref = zipfile.ZipFile(filepath, 'r')
    zip_ref.extractall(dataset_dir)
    zip_ref.close()

def download_json(json_url, dataset_dir):
    filename = json_url.split('/')[-1]
    filepath = os.path.join(dataset_dir, filename)
    
    def _progress(count, block_size, total_size):
        sys.stdout.write('\r>> Downloading %s %.1f%%' % (
            filename, float(count * block_size) / float(total_size) * 100.0))
        sys.stdout.flush()
    filepath, _ = urllib.request.urlretrieve(json_url, filepath, _progress)
    print()
    statinfo = os.stat(filepath)
    print('Successfully downloaded', filename, statinfo.st_size, 'bytes.')

if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

download_json(_JSON_URL, dataset_dir)
#download and unzip dataset
download_and_uncompress_zipball(_DATA_URL, dataset_dir)
download_and_uncompress_zipball(_DATA_TEST_URL, dataset_dir)

#Remove zip file
filename = _DATA_URL.split('/')[-1]
filepath = os.path.join(dataset_dir, filename)
os.remove(filepath)

filename = _DATA_TEST_URL.split('/')[-1]
filepath = os.path.join(dataset_dir, filename)
os.remove(filepath)





