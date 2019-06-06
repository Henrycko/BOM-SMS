#!/bin/bash
bom(){
    sleep 0.03
    echo "      _.-^^---....,,-- "
    sleep 0.03
    echo "  _--                  --_ "
    sleep 0.03
    echo " <                        >) "
    sleep 0.03
    echo " |                         | "
    sleep 0.03
    echo "  \._                   _./ "
    sleep 0.03
    echo "     '''--. . , ; .--'''    " 
    sleep 0.03
    echo "           | |   |           "
    sleep 0.03
    echo "        .-=||  | |=-.    "
    sleep 0.03
    echo "        '-=#$%&%$#=-'    "
    sleep 0.03
    echo "           | ;  :|      "
    sleep 0.03
    echo "  _____.,-#%&$@%#&#~,._____ "
    sleep 0.03
    echo "============================="
    sleep 2
    echo "==  Nako Coders Call BOM   =="
    sleep 0.7
    echo "============================="
}
load(){
    echo -e "\n"
    bar=" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    barlength=${#bar}
    i=0
    while((i<100)); do
        n=$((i*barlength / 100))
        printf "\e[00;32m\r[%-${barlength}s]\e[00m" "${bar:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.2
    done
}
clear
load
clear
bom
echo Selamat datang kak, Siapa nick kaka? #tulisan keluar
read nick #membaca yang ditulis
clear
load
clear
bom
echo Selamat datang $nick ":)"
get_url=$(curl -s https://0x.nakocoders.org/rest-api/lain-nya/api.php)
cek='curl -s '$get_url # check status
response=`curl -s -o /dev/null -w "%{http_code}" $cek`
if [[ $response = *sleeping* ]]; then
    echo
    echo "Website Offline/Restart untuk sementara"
else
    echo
    echo "Silahkan masukan nomor telp target"
    echo contoh 0812345678
    read target # masukin no telp
    echo
    echo "Berapa sms yang mau dikirim?"
    read paket
    echo
    echo Apakah nomor $target "dan SMS dikirim "$paket" sudah benar?"
    echo y/n?
    read confirm
    echo
    if [ $confirm = "y" ]; then
        load
        clear
        echo Melakukan spam SMS ke nomor $target
        echo
            echo "Jangan close aplikasi sebelum spam selesai"            
            echo "========================================"
            target_do=$get_url'/api.php?nomor='$target'&paket='$paket
            CURL_RESPONSE=`curl -s -o /dev/null -w "%{http_code}" $target_do`
            echo " Gunakan tools dengan bijak!"
            echo
            echo " Love u always "
            echo " -Henrycko"
            echo "======================================="
    else
        echo "Kesalahan"
    fi
fi
