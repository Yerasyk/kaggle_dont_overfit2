import zipfile

with zipfile.ZipFile('data/old.zip', 'r') as zip_ref:
    zip_ref.extractall('data/')

# kaggle competitions submit -c dont-overfit-ii -f knn_submission.csv -m "Message"