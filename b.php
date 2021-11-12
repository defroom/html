<?php
	$ip1 = $_SERVER["REMOTE_ADDR"];
	$ip2 = $_SERVER["HTTP_CLIENT_IP"];
	$ip3 = $_SERVER["HTTP_X_FORWARDED_FOR"];

	echo "<h1>ip1:".$ip1."</h1>";
	echo "<h1>ip2:".$ip2."</h1>";
	echo "<h1>ip3:".$ip3."</h1>";
?>
