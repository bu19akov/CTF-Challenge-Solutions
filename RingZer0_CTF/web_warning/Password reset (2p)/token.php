<?php
$time = 'Sat, 24 Feb 2024 13:12:17 -0500';
$utime = DateTime::createFromFormat('D, d M Y H:i:s O',$time)->format('U');
srand($utime);
$token = rand(1000000000000000,9999999999999999);
print "$token\n";
?>