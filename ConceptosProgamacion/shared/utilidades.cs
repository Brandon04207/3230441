using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.Versioning;
using System.Text;
using System.Threading.Tasks;

namespace shared
{
    public static class utilidades
    //internal = esta cerrado
    //public = esta abierta 
    {
        //funcion
        public static double calcularRecargoDominical(int HDom, int Smlv)
        //calcularRecargo es un metodo
        {
            var Vh = Smlv / 192;
            var RecargoDom = 0.75 * Vh;
            return RecargoDom;
        }
        public static double calcularRecargoNoc(int HNoc, int Smlv)
        //calcularRecargo es un metodo
        {
           var Vh = Smlv / 192;
           var RecargoNoc = 0.35 * Vh;
           return RecargoNoc;
        }
        public static double calcularRecargofestivo(int HFest, int Smlv)
        //calcularRecargo es un metodo
        {
            var Vh = Smlv / 192;
            var Recargofestivo = 0.2 * Vh;
            return Recargofestivo;
        }
        public static void calcularNomina(string nombre, int smlv, int HDom, int HNoc, int HD,int HFest)
        //void tira lo que tenga ahi
        {
            var Vh = smlv / 192;
            var recargoDom = utilidades.calcularRecargoDominical(HDom, smlv);
            var recargonoc = utilidades.calcularRecargoNoc(HNoc, smlv);
            var recargofest = utilidades.calcularRecargofestivo(HFest, smlv);

            var totalHorasNocturnas = HD * (Vh + recargonoc);
            var totalHorasDominicales = HD * (Vh + recargoDom);
            var totalHorasFestivas = HD * (Vh + recargofest);


            var totalHorasDiurnas = Vh * (HD);
            var devengado = totalHorasNocturnas + totalHorasDominicales + totalHorasDiurnas + totalHorasFestivas;

            Console.WriteLine($"nomina para el fulano:{nombre}");
            Console.WriteLine($"total devengado HN:{totalHorasNocturnas}");
            Console.WriteLine($"total devengado HD:{totalHorasDiurnas}");
            Console.WriteLine($"total devengado HD:{totalHorasFestivas}");
            Console.WriteLine($"total a pagar:{devengado}");





        }

    }
}
