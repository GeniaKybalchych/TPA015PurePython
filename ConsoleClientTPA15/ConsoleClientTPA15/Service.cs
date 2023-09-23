using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleClientTPA15
{
    internal class Service
    {
        public static async Task GetActivite(int temperature, string birthdate)
        {
            try { 
            HttpClient client = new HttpClient();

            var username = Environment.UserName;
            var hostname = Dns.GetHostName();

                string birthdateFormatted = birthdate.Replace("/", "-");
                string url = $"http://127.0.0.1:5000/suggest_activity/{temperature}/{birthdateFormatted}?username={username}&hostname={hostname}";
            HttpResponseMessage response = await client.GetAsync(url);

            if (response.IsSuccessStatusCode)
            {
                string resultat = await response.Content.ReadAsStringAsync();
                Console.WriteLine($"Activite :\n{resultat}");
            }

            else
            {
                Console.WriteLine($"Erreur : {response.StatusCode.ToString()}");

            }
            }
            catch ( Exception ex ) {    
                Console.WriteLine("Une erreur est survenue : " + ex.Message );
            }
        }
    }
}
