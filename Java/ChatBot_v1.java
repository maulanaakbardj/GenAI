import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

public class Chatbot {
    public static void main(String[] args) {
        try {
            // URL to access the ChatGPT API
            String url = "https://api.openai.com/v1/engines/davinci-codex/completions";

            // API key from OpenAI
            String apiKey = "YOUR_API_KEY_HERE";

            // Create URL and HttpURLConnection objects
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();

            // Set the HTTP method and headers
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            con.setRequestProperty("Authorization", "Bearer " + apiKey);

            // Set the data to be sent to the ChatGPT API
            String prompt = "Hello, how are you?";
            String data = "{\n" +
                    "  \"prompt\": \"" + prompt + "\",\n" +
                    "  \"max_tokens\": 50,\n" +
                    "  \"temperature\": 0.5,\n" +
                    "  \"n\": 1,\n" +
                    "  \"stop\": \"\\n\"\n" +
                    "}";

            // Sending data to the ChatGPT API
            con.setDoOutput(true);
            con.getOutputStream().write(data.getBytes("UTF-8"));

            // Read the response from the ChatGPT API
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            // Fetch the reply text from the ChatGPT API response 
            String answer = response.toString().split("\"text\": \"")[1].split("\",")[0];

            // Displays the answer from the chatbot
            System.out.println("Chatbot: " + answer);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
