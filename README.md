This project's goal is to improve food safety and quality, by predicting possible future violations.
This project is comprised of 4 scripts:

1. downloader.py: Downloads all xls files from (https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/shokuhin/yunyu_kanshi/index_00017.html) concerning foor safety

2. dataset_creation.py: Combines the previous downloads to create a dataset (uncleaned_data.txt) 

3. dataset_cleaning.py: Cleans the data, turning it from string to numeric

4. create_model.py: Create a decision tree to understand / predict the cause of violation in a future similar dataset
