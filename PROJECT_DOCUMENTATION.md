# Project Documentation


### Hypothesis

Students who attend higher ranked NSW high schools achieve higher NAPLAN Numeracy scores than their Reading and Writing scores, suggesting that these schools perform more strongly in mathematics than in literacy‑based subjects.

---

### Functional Requirement

The functional requirements for my NAPLAN Data analysis program describes what the system must be able to do with the school performance data that i got from myschool website. The program is supposed to load a CSV file containing naplan results and show an error if there is any type of problem in the thing. It must display the dataset in a table format so the user can view all school scores and extra stuff. The system also needs to generate a line graph comparing numeracy, reading, and writing scores across schools. For the analysis part, the program should calculate the average score for each subject and present the results clearly. It is also supposed display ranking lists for both naplan and hsc results so the user gets a better idea of the user interface. Finally, the program must provide a simple menu system so the user can easily navigate all the features in their experience.

---------

### Non-functional Requirement

- Usability  
  The program must be easy for the user to understand and operate. The menu should use simple wording so the user always knows what each option does. Output such as tables, averages, and graphs must be formatted clearly. The program should guide the user through each step without confusion, even if they have never used a data analysis tool before.

- Reliability  
  The system must run consistently without crashing. It should handle invalid input by showing helpful error messages instead of failing. The CSV file must load correctly each time, and the program should not corrupt or alter the data. Graphs and calculations must always produce accurate results.

---

### Phase 2: The researching and planning

Data Source:  
All NAPLAN and school performance data used in this project was obtained from the official Australian government education website:  
https://myschool.edu.au/

Planning and Research Steps:

- Identified the required data : School name, Numeracy, Reading, Writing, and Year.
- Chose the python library options for the data analysis:
  - I had used pandas for loading and processing CSV data  
  - I also used matplotlib for generating line graphs for the visual graph representation  
- Designed a user interface to allow users to:
  - View the dataset  
  - Generate a line graph  
  - Calculate subject averages  
  - View NAPLAN and HSC rankings  

- The different parts for my task:
  - `data_module.py` This is where all the functions are put so i can import them into the main py and would seperate them making them more neat.  
  - `main.py` This is where i import all my functions from my data module so it would print the main user interface


---

### SEEL/SEEC Paragraphs

**Statement:**  
The naplan data analysis program is designed to help users explore and understand school performance data through a simple and interactive menu system. The program provides multiple features such as viewing the dataset, generating graphs, calculating averages, and displaying school rankings. Each feature is separated into its own function, making the system easy to use and logically structured. An example i have is, the `show_datatable()` function prints the full dataset in a readable format, while `show_linegraph()` generates a visual comparison of Numeracy, Reading, and Writing scores using Matplotlib which was a very useful thing for my task. The `average_mean()` function calculates the mean score for each subject, and the ranking functions display NAPLAN and HSC performance lists. These features show that the program effectively supports users in analysing school performance data. By combining numerical results, visual graphs, and ranking lists, the system makes it easier to identify trends and compare schools, demonstrating that the program meets its intended purpose.

---

### Naplan Scores Data Dictionary

|  Field   | Datatype | Format for Display | Description | Example | Validation |
|----------|----------|--------------------|-------------|---------|------------|
|  School  | str      | XX...XX            |The name of the NSW school | North Sydney Boys | Must contain letters; may include spaces |
| Numeracy | int/float| NNN                | Year 9 NAPLAN Numeracy score | 675 | Must be a number between 0–1000 |
|  Reading | int/float| NNN                | Year 9 NAPLAN Reading score | 640 | Must be a number between 0–1000 |
|  Writing | int/float| NNN                | Year 9 NAPLAN Writing score | 610 | Must be a number between 0–1000 |
|   Year   | int      | YYYY               | Year the data was recorded | 2023 | Must be a valid year |
|   Rank   | int      | NN                 | Ranking based on performance | 1 | Must be a positive whole number |
