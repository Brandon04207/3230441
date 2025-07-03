using shared;
using static System.Runtime.InteropServices.JavaScript.JSType;

Console.WriteLine("Ingrese Nombre:");
var nombre = Console.ReadLine();
Console.WriteLine("Ingrese Horas Diurnas trabajadas:");
var HD = int.Parse(Console.ReadLine());

Console.WriteLine("Ingrese Horas Dominicales trabajadas:");
var HDom = int.Parse(Console.ReadLine());

Console.WriteLine("Ingrese Horas festivas trabajadas:");
var HFest = int.Parse(Console.ReadLine());

Console.WriteLine("Ingrese Horas nocturnas trabajadas:");
var HNoc = int.Parse(Console.ReadLine());

Console.WriteLine("Ingrese el salario minimo:");
var smlv = int.Parse(Console.ReadLine());

var recargoDom= utilidades.calcularRecargoDominical(HDom, smlv);
//parametros= HDom, Smlv

var recargoNoc = utilidades.calcularRecargoNoc(HNoc, smlv);

utilidades.calcularNomina(nombre, smlv, HDom, HNoc, HD, HFest);


