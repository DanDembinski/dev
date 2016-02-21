<html>
	<body>
		<?php
			$dbhandle = new SQLite3('db/inventory.db');

			$option = $_POST['option'];
			$item = strtolower($_POST['item']);
			$quantity = $_POST['quantity'];
			$location = $_POST['location'];
			
			if($option == 'Add')
			{
				if($dbhandle->querySingle("SELECT EXISTS (SELECT * FROM $location WHERE item == '$item');") == 1)
				{
					echo "already on shelf, updating to new quantity";
					$newquantity = $dbhandle->querySingle("SELECT quantity FROM $location WHERE item == '$item';");
					$newquantity = $newquantity+$quantity;
					$dbhandle->exec("UPDATE $location SET quantity=$newquantity WHERE item == '$item';");
				}
				else
				{
					$dbhandle->exec("INSERT INTO $location(item, quantity) VALUES ('$item', $quantity);");
					echo "added to shelf";
				}
			}
			else
			{
				$newquantity = $dbhandle->querySingle("SELECT quantity FROM $location WHERE item == '$item';");
				$newquantity = $newquantity-$quantity;
				if($newquantity > 0)
				{
					$dbhandle->exec("UPDATE $location SET quantity=$newquantity WHERE item == '$item';");
					echo "updating quantity";
				}
				else
				{
					$dbhandle->exec("DELETE FROM $location WHERE item == '$item';");
					echo "removing";
				}
			}
		?>		
	</body>
</html>
