using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleClientTPA15
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Entrez la temperature: ");
            string temperature = Console.ReadLine();

            Console.WriteLine("Entrez votre date de naissance: ");
            string dateNaissance = Console.ReadLine();

            await Service.GetActivite(Int32.Parse(temperature), dateNaissance);
        }
    }
}
