Project is coded in python3.7
It requires spacy 2.1.0, neuralcoref, nltk, networkx, pycorenlp libraries

To run the programs, use following commands

for task1
python task1.py <text_file_name>

for BUY_template(additonal optional argument for neuralcoref)
python BUY_template.py <text_file_name>
with coref
python BUY_template.py <text_file_name> c

for WORK_template(additonal optional argument for neuralcoref)
python WORK_template.py <text_file_name>
with coref
python WORK_template.py <text_file_name> c

for PART_template(this uses networkx library)
(takes directory path of all wikipedia articles and generates results in JSON directory which needs to be created)
python PART_template <directory_folder>

