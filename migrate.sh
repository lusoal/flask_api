#!/bin/bash

#Variaveis para realizar o migrate da estrutura do banco
echo 'Digite as informacoes do banco para realizar o migrate'

read -p 'hostname: ' HOST_DB
read -p 'username: ' USER_DB
read -sp 'password: ' PASS_DB

MYSQL_PATH=$(which mysql)

echo ${MYSQL_PATH}

$MYSQL_PATH -h ${HOST_DB} -u ${USER_DB} -p${PASS_DB} < ./deploy_structure.sql