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
            try
            {
                HttpClient client = new HttpClient();

                // Étape 1: Obtenir un token
                HttpResponseMessage tokenResponse = await client.GetAsync("http://127.0.0.1:5000/signup");
                string token = await tokenResponse.Content.ReadAsStringAsync();
                if (!tokenResponse.IsSuccessStatusCode)
                {
                    Console.WriteLine($"Erreur lors de l'obtention du token : {tokenResponse.StatusCode.ToString()}");
                    return; // quittez la méthode
                }
                var username = Environment.UserName;
                var hostname = Dns.GetHostName();

                // Étape 2: Utiliser ce token pour obtenir une suggestion d'activité


                string birthdateFormatted = birthdate.Replace("/", "-");
                string url = $"http://127.0.0.1:5000/activity-suggestions?temperature={temperature}&birthdate={birthdateFormatted}&username={username}&hostname={hostname}&token={token}";
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
            catch (Exception ex)
            {
                Console.WriteLine("Une erreur est survenue : " + ex.Message);
            }
        }
    }
}