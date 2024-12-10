import json
import os
import pandas as pd

# Update below path as required 
directory_path = "C:/Users/github/Downloads/Output/"
output_data = []

for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        with open(os.path.join(directory_path, filename), 'r') as file:
            content = file.read()
            if content.strip():  
                try:
                    data = json.loads(content)
                    
                    # Parse the results
                    for result in data.get('results', []):
                        path = result.get('path')
                        line = result.get('start', {}).get('line', 'NA')
                        severity = result.get('severity', 'NA')
                        if severity in [None, '', 'NA']:
                            severity = result.get('extra', {}).get('severity', 'NA')
                        message = result.get('extra', {}).get('message', 'NA')
                        check_id = result.get('check_id', 'NA')
                        
                        impact = result.get('extra', {}).get('metadata', {}).get('impact', 'NA')
                        owasp = ', '.join(result.get('extra', {}).get('metadata', {}).get('owasp', [])) if result.get('extra', {}).get('metadata', {}).get('owasp') else 'NA'
                        cwe = ', '.join(result.get('extra', {}).get('metadata', {}).get('cwe', [])) if result.get('extra', {}).get('metadata', {}).get('cwe') else 'NA'
                        references = ', '.join(result.get('extra', {}).get('metadata', {}).get('references', [])) if result.get('extra', {}).get('metadata', {}).get('references') else 'NA'
                        lines = result.get('extra', {}).get('lines', 'NA')

                        # Store data in a row format
                        output_data.append({
                            'Path': path,
                            'Line': line,
                            'Code': lines, 
                            'Check ID': check_id,
                            'Message': message,
                            'Severity': severity,
                            'Impact': impact,
                            'OWASP': owasp,
                            'CWE': cwe,
                            'References': references

                        })
                
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {filename}: {e}")

df = pd.DataFrame(output_data)
output_excel_path = 'results.xlsx'
df.to_excel(output_excel_path, index=False)

print(f"Data saved to {output_excel_path}")
