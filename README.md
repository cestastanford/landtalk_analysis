<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
</head>
<h1>Using Mallet to Model Landtalk Data</h1>
<h2>These Instructions will be updated as the scripts' purposes expand.</h2>
<p>(These instructions are distilled and made as specific as possible for the LandTalk project, but if these instructions are unclear or overly distilled, all the information can be found <a href= "https://programminghistorian.org/en/lessons/topic-modeling-and-mallet#your-first-topic-model)">here.</a> <em>Instructions differ slightly on windows (primarily backslashes instead of forward-slashes)</em></p>
<h2>Setting Up</h2>
<ul>
<li>If you have not done so already, download <a href = "http://mallet.cs.umass.edu/download.php"> MALLET </a> and the <a href="https://www.oracle.com/technetwork/java/javase/downloads/index.html"> Java Developer's Kit (JDK)</a>. Unzip Mallet somewhere you will find it (such as your desktop) and you will now have a directory called <kbd>mallet-2.0.8</kbd>. You should rename this folder <kbd>mallet-files</kbd> to avoid unecessary work changing the paths for the scripts to run.</li><br>
<li>At this point, open up your terminal and navigate to the <kbd>mallet-files</kbd> directory (using the <code>cd</code> command).</li><br>
<li>Type in <code>./bin/mallet</code> and if a list of commands appears, you've installed mallet correctly.</li><br>
</ul>

<h2>Producing a Topic Model</h2>
<ul>
<li> From the terminal, go to a directory you're comfortable working from (again, I suggest your desktop) and clone into <a href="https://github.com/cestastanford/landtalk_analysis.git">this repo</a> which contains all the necessary scripts and data needed to produce a helpful topic model.
</li><br>
<li> Once cloned in, move both the <kbd>pyScripts</kbd> folder and the <kbd>stoplists</kbd> folder into your <kbd>mallet-files</kbd> folder either through the command line or the GUI. </li><br>
<li> Again, either from the command line or the GUI, go into <kbd>pyScripts</kbd> and move <kbd>mallet-script.sh</kbd> up one level into the main <kbd>mallet-files</kbd> directory. </li> <br>
<li> If there are new transcripts available or an updated <kbd>scraped.xlsx</kbd> file available, be sure to replace the current ones with the updated ones to produce the most up-to-date results. </li>
<li> Type <code>chmod +x mallet-script.sh</code> into the command line from the main <kbd>mallet-files</kbd> folder to make this script executable, and you should now be able to type <code>./mallet-script.sh</code> to run the script which will run the data in <kbd>pyScripts/scraped.xlsx</kbd> through some python scripts and our MALLET tool and produce some useful topic model information. <b>NOTE:</b> This script may take 30s-1 min to complete.</li> <br>
<li><b>Some notes on the output files: </b><br>
<ul>
<li> Mallet Outputs: <br>
<ul>
<li>The <kbd>.gz</kbd> file will output every word in your corpus, the file it belongs to, and the topic it has been assigned to (topics are numbered 0-19 for 20 topics).</li><br>
<li>The <kbd>topic_keys_1.txt</kbd> file will show you the top key words in each topic. Each paragraph will correspond to a topic and all words in a paragraph will belong to that topic. It is up to you to look through these words and decide what the topic may have been about. This is where your humanistic inquiry brain should come in.</li><br>
<li>The third file, <kbd>transcript_composition_1.txt</kbd> is a text file that indicate the breakdown, by percentage, of each topic within each original text file you imported.</li><br>
<li> The <kbd>mytrans.mallet</kbd> file is just a compilation of all text files in a format that allows mallet to do its job. This file can be ignored. </li>
</ul></li><br>
<li> Other Outputs: 
<ul>
<li>The <kbd>conversationResults</kbd> file is a folder with all the text-file forms of the conversation data produced by <kbd>pyScripts/load_conversation_files.py</kbd> as well as all the conversation transcripts in the <kbd>pyScripts/Transcripts</kbd> folder. </li> <br>
<li> Finally, <kbd>compData.xlsx</kbd> is a spreadsheet containing all the data in <kbd>transcript_composition_1.txt.</kbd> and also includes a row at the bottom containing the sum of each column for easy use in later analysis. This file is produced by <kbd>load_composition_files.py</kbd> and modified by <kbd>comp_data_analysis.py</kbd> </li> <br>
<li>A folder called <kbd>__pycache__</kbd> will appear after the script is ran along with a couple other files with a leading dot. These files should all be removed before the folder is recommitted to the master repo. </li> <br>
</ul>
</li>
</ul>
</li>
<li> To recommit changes, the <kbd>mallet-script.sh</kbd> file should be moved back into the <kbd>pyScripts</kbd> folder both this and the <kbd>stoplists</kbd> folder should be moved back into the<kbd>Mallet-Topic-Modeling-Guide</kbd> folder for committing. </li> <br>
</ul>
<h2> Optimizing Parameters </h2><br>
<p> Although the current scripts are ready to be ran and worked with as is, I should note that there are some parameters that <a href="http://mallet.cs.umass.edu/download.php">the aforementioned tutorial</a> goes into detail about that can modify our results a bit. These are all parameters that should be modified in the <kbd>mallet-script.sh</kbd> file. Modifying these parameters can be a bit more of an art than a science. For example, setting the number of topics too large can have the effect of having too few words per topic while setting the number of topics too low can have too many words per topic, both of which reduce the quality and meaningfulness of our results. Another parameter is th e --optimize-interval parameter which turns on hyperparameter optimization or, in english, allows the model to better fit the data by allowing some topics to be more prominent than others. In general, including this parameter leads to better topics. Optimizing every 10 iterations (+/- 5) is generally reasonable. MALLET includes more of these parameters than I could hope to explain, but use of these parameters should be guided by a strong and focused research question more than blind trial and error. Optimizing or modifying our results will mean little to nothing without knowing first what kind of patterns we're searching for. </p>
<h2> What's Next? </h2><br>
<p> At this point, we can and must begin using humanistic inquiry to decide in which direction we want to go. Our results will be more accurate and meaningful as we collect more data, since less than 400 entries don't quite do justice to all the changes happening in the world right now, but this procedure should work even on an expanding corpus, provided it doesn't get reshaped in cruel and unusual ways. The outputs we have are now ready to be graphed as histograms or pie charts to view relative weights of topics, mapped according to the relevance of the locations associated with the topics, or just read-through to try to identify patterns in the way people are describing the particular changes or locations they're interacting with. </p>
</html>
