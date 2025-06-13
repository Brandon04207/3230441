do
{
    Console.Write("ingrese primer numero entero:");
    var n1 = (Console.ReadLine());
    //aqui no le pedimos que lo convierta en entero

 bool num = true;
        //se hace una variable que sea verdadera o falsa

    if (int.TryParse(n1, out int n1Int))
        //convierta n1 en entero
     do
     { 
        Console.Write("ingrese segundo numero entero:");
        var n2 = (Console.ReadLine());
        if (int.TryParse(n2, out int n2Int))
        //convierta n2 en entero
        {
            if (n1Int % n2Int == 0)
            //mod 2 = % 
            {
                Console.WriteLine($"el numero: {n2}, es multiplo de: {n1}");
                num = true;
            }
            else
            {
                Console.WriteLine($"el numero: {n2},no es multiplo de: {n1}");
                num = true;
            }
        }
        else
        {
          Console.WriteLine("debes ingresar numero entero");
          num= false;

        }
     } while (num == false);
    // si el num es falso se repite hasta el segundo numero , si es verdadero se repite todo 

    else
    {
        Console.WriteLine("debes ingresar numero entero");
        //si no puede convertir en numero entero lo manda para aqui 
    }

} while (true);


