#!/bin/bash

#Tramo de usuarios 1 hata 10


#for i in {1..10}
#do
#    python carga_usuarios.py $i >> logs/log_sence.txt &
#done

python carga_usuarios.py 16 2 >> logs/log_sence.txt &
python carga_usuarios.py 17 2 >> logs/log_sence.txt &
python carga_usuarios.py 18 2 >> logs/log_sence.txt &
python carga_usuarios.py 19 2 >> logs/log_sence.txt &
python carga_usuarios.py 20 2 >> logs/log_sence.txt &
