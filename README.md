README.md
----------

To run this code:
------------------
	1. have all files provided in the same directory
	2. install all libraries used in the file
		libraries are found near the top
		of each file.py in the "import library_name" section
	3. run the "main_SQlite_cleaner.py" file
		**NO changes are needed**
		**This code is functional**

Python file used Explained:
--------------------------
1. starting from a SQLite data base with 
	IEEE754 way of display data 
		&
	TimeStamp in seconds+(six additional LSF)
	
2. "IEEE754_to_decimal.py" turns IEEE754 in to readable floats
3. "ImportSQliteDF.py"
	imports original SQL
	using pandas & "IEEE754_to_decimal.py"
	to change data in to readable float df
	          Timestamps in to readable datetime 
4. "DF_csv.py" -> creates a .csv
5. "DF_sql_table.py" creates a new readable .sqlite database and table
6. "graph_adjustments.py" assists with the graph display 
	a. turns string values in to a float & rounds
	b. reducing the x-axis entries for visibility
7. "graph.py" creates a matplotlib plot
7. "text_in_to_list.py" turns file.text in to a list
8. "paragraph_story_v3.py" this is the main 'Story' of the file.pdf
	a. paragraph style
	b. table of contents
        c. paragraph titles
	d. main text
	e. images	
9. "header_n_footer_v1.py" provides the header and footer of the file.pdf
10. "build_pdf_v4.py" bulds the file.pdf
11. "DirectoriesControl.py" 
	a. creates a directory with TimeStamp and all result files in it
	b. creates a zip of the result directory for easy transfering 
		of the test results
	c. opens up the file.pdf and test report.html upon test completion
	NOTE: this file is commented here 
		to prevent creation of multiple directories
		each time the code is run
		(feel free to uncomment it, if you wish to incorporated it 
		at your test)
12. "main_SQlite_cleaner.py" executes the whole code
	this is where changes in variable parameters (names, text font, color ...)
	can take place
	NOTE: This is the only file that you will need to execute 
		any variable/parameter adjustments if you wish

		

	
