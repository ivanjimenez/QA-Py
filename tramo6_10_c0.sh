#!/bin/bash

#Tramo de usuarios 1 hata 10


#for i in {1..10}
#do
#    python carga_usuarios.py $i >> logs/log_sence.txt &
#done

python carga_usuarios.py 6 2 >> logs/log_sence.txt &
python carga_usuarios.py 7 2 >> logs/log_sence.txt &
python carga_usuarios.py 8 2 >> logs/log_sence.txt &
python carga_usuarios.py 9 2 >> logs/log_sence.txt &
python carga_usuarios.py 10 2 >> logs/log_sence.txt &
