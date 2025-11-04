do
{
    Console.WriteLine("usted como el buen profesor y el mejor, cual es la nota que me merezco");
    Console.Write("porfavor que sea del 1 al 5 (numero simple): ");
    var calificacion = Console.ReadLine();


    if (int.TryParse(calificacion, out int calificacionint))
    {
        
        if (calificacionint >= 1 && calificacionint <= 5)
        {
            Console.WriteLine($" su calificacion es: {calificacionint}");
        }
        else if (calificacionint >= 5)
        {
            Console.WriteLine("tu numero es mayor a 5, vuelve a digitar un numero");
        }
        else
        {
            Console.WriteLine("tu numero es menor a 1, vuelve a digitar un numero");
        }

    }
    else if (calificacion == "cinco"|| calificacion == "cuatro" || calificacion == "tres" || calificacion == "dos" || calificacion == "uno")
    {
        Console.WriteLine($"su calificacion es: {calificacion}");
    }

    else
    {
        Console.WriteLine("no has digitado correctamente lo que te pedi, porfavor digite lo pedido");
    }
} while (true);