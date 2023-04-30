using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace OpenAIChatbot
{
    class Program
    {
        static async Task Main(string[] args)
        {
            // Set up the OpenAI API credentials and endpoint
            string openaiKey = "YOUR_API_KEY";
            string openaiEndpoint = "https://api.openai.com/v1/engines/davinci-codex/completions";

            // Set up the prompt for the chatbot to respond to
            string prompt = "Hello, my name is John. What is your name?";

            // Set up the HTTP client and request headers
            HttpClient httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", openaiKey);
            httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

            // Set up the request content with the prompt and some additional parameters
            string requestBody = "{\"prompt\": \"" + prompt + "\", \"max_tokens\": 50, \"temperature\": 0.5}";
            StringContent content = new StringContent(requestBody, Encoding.UTF8, "application/json");

            // Send the request to the OpenAI API and retrieve the response
            HttpResponseMessage response = await httpClient.PostAsync(openaiEndpoint, content);
            string responseString = await response.Content.ReadAsStringAsync();

            // Extract the response text from the JSON response
            int startIndex = responseString.IndexOf("text\":") + 7;
            int endIndex = responseString.IndexOf("\"}", startIndex);
            string responseText = responseString.Substring(startIndex, endIndex - startIndex);

            // Print the response text to the console
            Console.WriteLine(responseText);
        }
    }
}
