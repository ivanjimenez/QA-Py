#!/bin/bash

#Tramo de usuarios 1 hata 10


#for i in {1..10}
#do
#    python carga_usuarios.py $i >> logs/log_sence.txt &
#done

python carga_usuarios.py 11 >> logs/log_sence.txt &
python carga_usuarios.py 12 >> logs/log_sence.txt &
python carga_usuarios.py 13 >> logs/log_sence.txt &
python carga_usuarios.py 14 >> logs/log_sence.txt &
python carga_usuarios.py 15 >> logs/log_sence.txt &
