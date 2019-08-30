rm -R scriptOutput
mkdir scriptOutput
mkdir scriptOutput/conversationResults
python ./pyScripts/load_conversation_files.py
bin/mallet import-dir --input scriptOutput/conversationResults --output scriptOutput/mytrans.mallet --keep-sequence --stoplist-file stoplists/all-stops.txt
for i in 1
do
KEYS="topic_keys_$i.txt"
STATE="topic_state_$i.gz"
COMP="transcript_composition_$i.txt"
bin/mallet train-topics --input scriptOutput/mytrans.mallet --optimize-interval 10 --num-topics 50 --output-state scriptOutput/$STATE --output-topic-keys scriptOutput/$KEYS --output-doc-topics scriptOutput/$COMP --random-seed 1
done
python ./pyScripts/load_composition_files.py
python ./pyScripts/comp_data_analysis.py
