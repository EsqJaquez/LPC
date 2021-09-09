$rutamod = Read-Host -Prompt "Escriba la ruta donde está el modulo: "
Import-Module $rutamod\teamsmodulo.psm1

$val=1
while($val -eq 1)
{

	$dec = Read-Host -Prompt "Que desea hacer:
	1.-Mostrar equipos a los que perteneces
	2.-Crear un nuevo equipo
	3.-Cambiar foto de perfil de un equipo
	4.-Eliminar un equipo
	5.-Añadir un nuevo miembro a un equipo
	6.-Generar un reporte del estado de los equipos
	7.-Salir
	Decision: "

	switch ( $dec )
	{

		1 
		{
			$usuario = Read-Host -Prompt "escriba el correo del usuario: "
			showteams $usuario
			$val = Read-Host -Prompt "Desea realizar otra acción?: 1=Si 2=No "
		}
		2 
		{
			$nombre = Read-Host -Prompt "escriba el nombre del equipo: "
			$Descripcion = Read-Host -Prompt "escriba la descripcion del grupo: "	
			newteams $nombre $Descripcion
			$val = Read-Host -Prompt "Desea realizar otra acción?: 1=Si 2=No "
		}
		3 
		{	
			$Team = Read-Host -Prompt "escriba el identificador del equipo: "
			$Rutafoto = Read-Host -Prompt "escriba la ruta de la foto: "
			newteampic $Team $Rutafoto
			$val = Read-Host -Prompt "Desea realizar otra acción?: 1=Si 2=No "
		}
		4
		{
			$Team = Read-Host -Prompt "Escriba el identificador del equipo a borrar: "
			removeteams $Team
			$val = Read-Host -Prompt "Desea realizar otra acción?: 1=Si 2=No "
		}
		5
		{
			$Team = Read-Host -Prompt "Escriba el identificador del equipo al que desea agregar un nuevo miembro: "
			$nusuario = Read-Host -Prompt "Escriba el correo electronico de la persona a agregar: "
			addteamember $Team $nusuario
			$val = Read-Host -Prompt "Desea realizar otra acción?: 1=Si 2=No "
		}
		6
		{
			$usuario = Read-Host -Prompt "escriba el correo del usuario: "
			$ruta = Read-Host -Prompt "Escriba la ruta donde aparecera el reporte: "
			getreport $usuario $ruta	
			$val = Read-Host -Prompt "Desea realizar otra acción?: 1=Si 2=No "
		}
		7
		{
			$val++
		}
		
		default
		{
			'Vuelva a intentarlo'
			$val = Read-Host -Prompt "Desea realizar otra acción?: 1=Si 2=No "
		}
}






















}