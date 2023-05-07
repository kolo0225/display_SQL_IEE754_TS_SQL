README.md
----------

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
6. "graph.py" creates a matplotlib plot
7. "main_SQlite_cleaner.py" executes the whole code

	
