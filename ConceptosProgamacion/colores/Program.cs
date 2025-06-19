do
{
   Console.WriteLine("hay 10 colores:");
    Console.WriteLine("1.magenta");
    Console.WriteLine("2.amarillo");
    Console.WriteLine("3.rojo");
    Console.WriteLine("4.violeta");
    Console.WriteLine("5.azul");
    Console.WriteLine("6.morado");
    Console.WriteLine("7.verde");
    Console.WriteLine("8.naranja");
    Console.WriteLine("9.negro");
    Console.WriteLine("10.blanco");
    Console.Write("elija uno de ellos:");


    var color = int.Parse(Console.ReadLine());
    Console.Write("ingrese su nombre:");
    var nombre = (Console.ReadLine());
    Console.Write("ingrese su documento:");
    var documento = int.Parse(Console.ReadLine());

    if (color == 1)

        {
        Console.WriteLine($"gracias {nombre} su color preferido es: magenta");
        Console.WriteLine("recibiras un premio!!!");
        }
    else if (color == 2)
        {
        Console.WriteLine($"gracias {nombre} su color preferido es:amarillo");
    }
    else if (color == 3)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:rojo");
    }
    else if (color == 4)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:violeta");
    }
    else if (color == 5)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:azul");
    }
    else if (color == 6)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:morado");
    }
    else if (color == 7)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:verde");
    }
    else if (color == 8)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:naranja");
    }
    else if (color == 9)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:negro");
    }
    else if (color == 10)
    {
        Console.WriteLine($"gracias {nombre} su color preferido es:blanco");
    }

    else
    {
        Console.WriteLine("no dijistaste correctamente el numero");
    }
} while (true);