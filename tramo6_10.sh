#!/bin/bash

#Tramo de usuarios 1 hata 10


#for i in {1..10}
#do
#    python carga_usuarios.py $i >> logs/log_sence.txt &
#done

python carga_usuarios.py 6 >> logs/log_sence.txt &
python carga_usuarios.py 7 >> logs/log_sence.txt &
python carga_usuarios.py 8 >> logs/log_sence.txt &
python carga_usuarios.py 9 >> logs/log_sence.txt &
python carga_usuarios.py 10 >> logs/log_sence.txt &
