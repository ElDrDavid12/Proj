pwd

ls

cd /home/david/

mkdir prueba

touch among_us.txt

echo "No se lo que estoy haciendo"

echo "Voy a borrar este archivo" > among_us.txt
echo "soy muysigma" >> among_us.txt

ls | grep "among_us.txt"

nombre = "Victor"
echo $nombre

if [$nombre == "Victor"]; then
    echo "Victor, ponte a hacer platzi"
else
    echo "Me vale todo lo que digas"
fi

for i in {1..5}
do
    echo "Numero $i"
    
saludar() {
    echo "hola, $1"
}

salduar "Carlos"