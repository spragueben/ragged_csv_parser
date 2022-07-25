#%%
# Filename: code_converter.ipynb
# Author: Ben Sprague

import os
import csv
import platform
import subprocess
import pandas as pd
from tkinter import Tk
from datetime import datetime

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

file_path = os.getcwd()
paginator =    "\n---------------------------------------------------------------"
proceed_prompt = "------------------ Press <ENTER> to continue ------------------"
#%%

print('''
Ragged Array Parser
 ***** *  *   *  * 
*       **   * *  *
           *    *  
 *     *  *   *    
                *  
                   
     *             
    *            * 
                   
  **         *     
           *       
*       **     *  *

Welcome! Let's parse.''')

INPUT_FILE = None

while INPUT_FILE == None:
    file_selection_entry = input(f'''{paginator}\n
- To open a file browser and select a csv you would like to parse, press <ENTER>. 
- Alternatively, paste the absolute path to whichever csv you would like to use (then press <ENTER>)\n''')

    if file_selection_entry == '':
        try:
            from tkFileDialog import askopenfilenames
        except:
            from tkinter import filedialog

            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            filenames = filedialog.askopenfilenames() # show an "Open" dialog box and return the path to the selected file

            INPUT_FILE = filenames[0]
    else:
        INPUT_FILE = file_selection_entry
input(proceed_prompt)
#%%
acs_file = []

with open(INPUT_FILE, newline='') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in file_reader:
        acs_file.append(row)

#%%
separate_at = []

for i in range(len(acs_file)):
    if acs_file[i] == []:
        separate_at.append(i+1)

#%%
temp = []
for i in range(len(separate_at)-1):
    if separate_at[i+1]-separate_at[i] > 1:
        temp.append(separate_at[i])

temp.append(separate_at[-1])
separate_at = temp

#%%
sliced_lists = []

for i in range(1, len(separate_at)):
    sliced_lists.append(acs_file[separate_at[i-1]:separate_at[i]])

#%%
# Check this output for acceptable values for 'TABLE_NAME' variable
section_labels = []
for i in range(len(sliced_lists)):
    section_labels += sliced_lists[i][0]
    # print( sliced_lists[i][0])

TABLE_NAME = input(f'Please select a table name from the following list: {section_labels}\n') or section_labels[0]      #accepts one name, but need to know table names, outputted in second-to-last cell

timestamp = datetime.now().strftime('%Y.%m.%d-%H%Mh')
output_file = os.path.join(TABLE_NAME + ".csv")
if input(f'''\nThe default filename for this notebook will be '{output_file}'. Would you like to change it (y/[n])? ''').lower() in ['y', 'yes']:
    output_file = (input("\nGive your file a new name (we'll append the extension): ") or output_file).split(".csv")[0] + ".csv"

dir_selection_entry = input(f'''{paginator}\nYour current destination directory is {file_path}

- To keep this as your destination directory, press <ENTER>. 
- To open a file browser and select a different directory, type 'cd' (then <ENTER>). 
- Alternatively, you can paste the absolute path to whichever directory you would like to use (then press <ENTER>) ''')

if dir_selection_entry.lower() == 'cd':
    from tkinter import filedialog
    from tkinter import *
    Tk().withdraw()
    file_path = filedialog.askdirectory() or file_path
else:
    file_path = dir_selection_entry or file_path
print(paginator)

if input('Would you like have the current date and time prepended to your filename ([y]/n)? ').lower() in ["y","yes",""]:
    timestamp = datetime.now().strftime('%Y.%m.%d-%H%Mh')
    output_file = os.path.join(file_path,timestamp+"_"+output_file)
else:

    output_file = os.path.join(file_path,output_file)

input(f'''{paginator}\nYour selected filename is: {output_file}

Press enter to open your csv in the default application''')


#%%
table_to_display = sliced_lists[section_labels.index(TABLE_NAME)][1:]
df = pd.DataFrame(table_to_display)

#%% 
table_to_display = sliced_lists[section_labels.index(TABLE_NAME)][1:]
df = pd.DataFrame(table_to_display)

#%%
df = pd.DataFrame(table_to_display[1:])
df.to_csv(output_file, index=False, header=table_to_display[0])
open_file(output_file)