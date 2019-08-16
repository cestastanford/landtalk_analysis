rm -R scriptOutput
mkdir scriptOutput
mkdir scriptOutput/conversationResults
python3 ./python-stuff/load_conversation_files.py
bin/mallet import-dir --input scriptOutput/conversationResults --output scriptOutput/mytrans.mallet --keep-sequence --stoplist-file stoplists/all-stops.txt
for i in 1
do
KEYS="topic_keys_$i.txt"
STATE="topic_state_$i.gz"
COMP="transcript_composition_$i.txt"
bin/mallet train-topics --input scriptOutput/mytrans.mallet --num-topics 50 --output-state scriptOutput/$STATE --output-topic-keys scriptOutput/$KEYS --output-doc-topics all-out/$COMP --random-seed 1
done
python3 ./python-stuff/load_composition_files.py