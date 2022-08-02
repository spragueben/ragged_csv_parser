## Usage
- This script is a python command line utility for parsing a sectioned csv and outputting any  section specified as a csv
- The script accepts any table name that matches the title of a parsed section, and generates a dataframe and csv file with all the data contained within that section.

## Assumptions
- The program logic assumes that the source csv sections are separated by one or more blank lines
- Section lables are assumed to be in the first non-blank line following one or more blank lines

## Dependencies
- Pandas

## Instructions
- Activate a virtual environment that has pandas installed, and type `python -m ./ragged_array_parser` in the command prompt. 
- The program will prompt you to choose a csv you would like to parse, either by pasting a its absolute path or browsing with a file dialog.
- After selecting a file, the program will ask which section to separate into its own csv.
- If an alternate filename is not provided, the default filname will match the table name
- If an alternate file location in not provided, the csv will be outputted to your current working directory.

## Future Improvements
- The parser will provide an option for bulk-generating csvs for all sections, or a selected subset