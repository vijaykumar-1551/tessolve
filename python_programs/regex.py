import re

# Regex pattern to match the Event logs
regex_pattern = r'\d{2}/\d{2} \d{2}:\d{2}:\d{2} (EVENT|TRACE)\s+:(.*)'

# Open the input file
with open('input.log', 'r') as input_file:
    # Open the output file for writing
    with open('output.log', 'w') as output_file:
        # Iterate over each line in the input file
        for line in input_file:
            # print(line)  # Print the line for debugging
            # Apply the regex pattern to each line
            match = re.search(regex_pattern, line)
            if match:
                # Write the matched Event log to the output file
                output_file.write(match.group().strip() + '\n')
