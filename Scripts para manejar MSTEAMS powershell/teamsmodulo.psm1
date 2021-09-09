
function showteams
{
[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [String]$usuario
)
 Get-Team -User $usuario
}



function newteams
{
[CmdletBinding()]
param(

	[Parameter(Mandatory)]
 	[String]$nombre,
  	[String]$descripcion

)
 New-Team -DisplayName $nombre -Description $Descripcion
}



function newteampic 
{
[CmdletBinding()]
param(
	[Parameter(Mandatory)]
 	[String]$Team,
  	[String]$Rutafoto
)
Set-TeamPicture -GroupId $Team -ImagePath $Rutafoto
}


function removeteams 
{
[CmdletBinding()]
param(
	[Parameter(Mandatory)]
 	[String]$Team
)
	Remove-Team -GroupId $Team
}


function addteamember 
{
[CmdletBinding()]
param(
	[Parameter(Mandatory)]
 	[String]$Team,
  	[String]$nusuario
)
	
	Add-TeamUser -GroupId $Team -User $nusuario
}
	
function getreport {
[CmdletBinding()]
param(
	[Parameter(Mandatory)]
 	[String]$usuario,
  	[String]$ruta
)
	Get-Team -User $usuario | Select-Object -Property GroupId, DisplayName, MailNickName, Archived | Out-File -FilePath $ruta\equipos.txt
}