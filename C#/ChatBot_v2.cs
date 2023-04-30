using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

public partial class _Default : Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }

    protected async void btnSubmit_Click(object sender, EventArgs e)
    {
        // Set up the OpenAI API credentials and endpoint
        string openaiKey = "YOUR_API_KEY";
        string openaiEndpoint = "https://api.openai.com/v1/engines/davinci-codex/completions";

        // Set up the prompt for the chatbot to respond to
        string prompt = txtMessage.Text;

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
        dynamic jsonResponse = JsonConvert.DeserializeObject(responseString);
        string responseText = jsonResponse.choices[0].text;

        // Output the response text to the chat window
        chatWindow.InnerHtml += "<div class=\"botMessage\">" + responseText + "</div>";

        // Clear the text box
        txtMessage.Text = "";
    }
}
