using System.Numerics;

do
{
Console.WriteLine("ingrese primer numero entero:");
var n1 = int.Parse(Console.ReadLine());
Console.WriteLine("ingrese segundo numero entero:");
var n2 = int.Parse(Console.ReadLine());
Console.WriteLine("ingrese tercer numero entero:");
var n3 = int.Parse(Console.ReadLine());


    if (n1 > n2 & n2 > n3)
    {
        Console.WriteLine($"el numero mayor es:{n1}");
        Console.WriteLine($"el numero del medio es:{n2}");
        Console.WriteLine($"el numero menor es:{n3}");
    }
    else if (n1 > n3 & n3 > n2)
    {
        Console.WriteLine($"el numero mayor es:{n1}");
        Console.WriteLine($"el numero del medio es:{n3}");
        Console.WriteLine($"el numero menor es:{n2}");
    }

    else if (n2 > n1 & n1 > n3)
    {
        Console.WriteLine($"el numero mayor es:{n2}");
        Console.WriteLine($"el numero del medio es:{n1}");
        Console.WriteLine($"el numero menor es:{n3}");
    }
    else if (n2 > n3 & n3 > n1)
    {
        Console.WriteLine($"el numero mayor es:{n2}");
        Console.WriteLine($"el numero del medio es:{n3}");
        Console.WriteLine($"el numero del medio es:{n1}");
    }
    else if (n3 > n2 & n2 > n1)
    {
        Console.WriteLine($"el numero mayor es:{n3}");
        Console.WriteLine($"el numero del medio es:{n2}");
        Console.WriteLine($"el numero menor es:{n1}");
    }
    else
    {
        Console.WriteLine($"el numero mayor es:{n3}");
        Console.WriteLine($"el numero del medio es:{n1}"); 
        Console.WriteLine($"el numero del medio es:{n2}");
    }
} while (true);



