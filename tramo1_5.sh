#!/bin/bash

#Tramo de usuarios 1 hata 10


#for i in {1..10}
#do
#    python carga_usuarios.py $i >> logs/log_sence.txt &
#done

python carga_usuarios.py 1 >> logs/log_sence.txt &
python carga_usuarios.py 2 >> logs/log_sence.txt &
python carga_usuarios.py 3 >> logs/log_sence.txt &
python carga_usuarios.py 4 >> logs/log_sence.txt &
python carga_usuarios.py 5 >> logs/log_sence.txt &
