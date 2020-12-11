
Readme
=

# feedback-analyzer
This repository contains a script to create a csv out of a client log. Used to retrieve feedback. The script parser_analyzer.py can be use to convert a log with session information and reviews to csv

# Requirements
- pyhton3

# Usage
- From terminal run: 
     ```sh
    console$ python3 parser_analyzer.py "<path/to/thefile.log>""
    ```
- A filed called log.csv will be created with the following structure:  ['time','confname', 'meetingId', 'clientURL','comment', 'rating']



