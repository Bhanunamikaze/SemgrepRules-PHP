## SemgrepRules-PHP
Collection of Semgrep PHP rules - mostly from https://github.com/semgrep/semgrep-rules/tree/develop 

### Installation
pip install semgrep==1.54.3

### Download the rules
git clone https://github.com/Bhanunamikaze/SemgrepRules-PHP.git

### Use below script to run it; update the paths in the script 
```
#Download the below script to run multiple directories of semgrep rules and paths - output is saved into separate files for each rule  
wget https://raw.githubusercontent.com/Bhanunamikaze/PenTest-Scripts/refs/heads/main/semgrep_runner.py

#Parse the output from above script and convert it into a single CSV file with only important fields
wget https://raw.githubusercontent.com/Bhanunamikaze/SemgrepRules-PHP/refs/heads/main/Semgrep_JSONScanResult_Parser.py

```

