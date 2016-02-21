<?php
	$dbhandle = new SQLite3('db/inventory.db');

	$option = $_POST['option'];
	$name = $_POST['name'];

	if($option == 'Add')
	{
		echo "We'll create a new table in hur.";
		$dbhandle->exec("CREATE TABLE $name (id INTEGER PRIMARY KEY, item TEXT, quantity INTEGER);");

	}
	else
	{
		echo "Annnnd we'll delete the selected table here.";
		$dbhandle->exec("DROP TABLE $name;");
	}
?>	
