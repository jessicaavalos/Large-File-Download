"""
Author: Jessica Avalos
Description: This script facilitates downloading large files by managing the data transfer in segments, ensuring that any interruptions
in the download can be managed without starting over.
"""

import requests

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=32768):
                f.write(chunk)

if __name__ == '__main__':
    dataset_url = 'URL_HERE'
    local_filename = 'dataset_####.zip'

    download_file(dataset_url, local_filename)
