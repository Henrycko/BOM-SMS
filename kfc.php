<?php
include 'bomkfc.php';

/*
    https://github.com/thetermuxchoice/
    Modified By @thetermuxchoice
*/

$init = new Bom();

//Eksekusi Sms Boomber
echo "
+------------------------------------+
+                                    +
+    ...::[$ Spam SMS KFC $]::...    +
+    [ Coded By @thetermuxchoice ]   +
+                                    +
+------------------------------------+\n\n";
echo "Nomor Target\nInput : ";
$a = trim(fgets(STDIN));
$init->no = "$a";
echo "Jumlah Pesan\nInput : ";
$b = trim(fgets(STDIN));
$loop = "$b";
for ($i=0; $i < $loop; $i++) { 
    $init->Verif($init->no);
}

