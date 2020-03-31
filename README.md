# to-do_2
Flask web application with storing tasks using SQLite. 

Difference between Postgers and SQLite:

When creating a table, use id integer primary key (integer instead of serial);
  SQL also creates implicit column called rowid (key). In case of primary key integer, this primary key column becomes an alias for the rowid column.
  
With python function fetchall() return tuple, not dictionary. Access it with indexation. 
