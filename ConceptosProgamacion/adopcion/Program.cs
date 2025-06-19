do
{
    Console.WriteLine("tenemos 5 aniamles para que adoptes");
    Console.WriteLine("1.perro");
    Console.WriteLine("2.gato");
    Console.WriteLine("3.conejo");
    Console.WriteLine("4.caballo");
    Console.WriteLine("5.loro");
    Console.Write("seleccione una opcion:");

    var animal = int.Parse(Console.ReadLine());

    if (animal==1)
    {
        Console.Write("ingrese el nombre de la persona:");
        var nombre =(Console.ReadLine());
        Console.Write("ingrese documento:");
        var documento = int.Parse(Console.ReadLine());

        Console.WriteLine($"gracias {nombre} por elegir un lindo perro");

    }
    else if (animal == 2)
    {
        Console.Write("ingrese el nombre de la persona:");
        var nombre = (Console.ReadLine());
        Console.Write("ingrese documento:");
        var documento = int.Parse(Console.ReadLine());

        Console.WriteLine($"gracias {nombre} por elegir un lindo gato");

    }
    else if (animal == 3)
    {
        Console.Write("ingrese el nombre de la persona:");
        var nombre = (Console.ReadLine());
        Console.Write("ingrese documento:");
        var documento = int.Parse(Console.ReadLine());

        Console.WriteLine($"gracias {nombre} por elegir un lindo conejo");

    }
    else if (animal == 4)
    {
        Console.Write("ingrese el nombre de la persona:");
        var nombre = (Console.ReadLine());
        Console.Write("ingrese documento:");
        var documento = int.Parse(Console.ReadLine());

        Console.WriteLine($"gracias {nombre} por elegir un lindo caballo");

    }
    else if (animal == 5)
    {
        Console.Write("ingrese el nombre de la persona:");
        var nombre = (Console.ReadLine());
        Console.Write("ingrese documento:");
        var documento = int.Parse(Console.ReadLine());

        Console.WriteLine($"gracias {nombre} por elegir un lindo loro");

    }
    else
    {
        Console.Write("ingresaste mal el numero del animal, vuelve a intentarlo");
    }



} while (true);