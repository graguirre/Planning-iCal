# sacar los datos del HTML y preparados para pasarlos al TXT

# horas complementarias (C), festivas (F), etc, no se discriminan y se incluyen en el calendario
# vacaciones (V, W) no se incluyen en el calendario
cat calendario.htm | grep td | grep center | grep -e '[A-Z]</td>$' | sed -e 's/[ ]\+//' | cut -d '>' -f 2 | cut -d '<' -f 1 | sed -e 's/[CFH]/X/' | sed -e 's/[VW]/M/' > horario.txt


# obtiene la primera semana
cat calendario.htm | grep dayname | head -n1 | cut -d '"' -f 6 | sed -e 's/[a-z]//g' > semana.txt
