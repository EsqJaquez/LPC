
#!/bin/bash
function felizjueves {
for (( n=1; n<=nvar; n++ ))
do  
  echo echo "feliz jueves "
done
}

read -p "cuantas veces desea decir feliz jueves?: " nvar
felizjueves nvar
