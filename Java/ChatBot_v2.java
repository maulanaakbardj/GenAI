import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

public class DalleChatbot {
    private static final String OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE";

    public static void main(String[] args) {
        try {
            // Read user input
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("You: ");
            String input = reader.readLine();

            // Send input to OpenAI API
            URL url = new URL("https://api.openai.com/v1/images/generations");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Authorization", "Bearer " + OPENAI_API_KEY);
            conn.setRequestProperty("Content-Type", "application/json");

            String data = "{\"model\": \"image-alpha-001\", \"prompt\": \"" + input + "\", \"num_images\": 1, \"size\": \"512x512\", \"response_format\": \"url\"}";
            conn.setDoOutput(true);
            conn.getOutputStream().write(data.getBytes("UTF-8"));

            // Read response from OpenAI API
            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String response = "";
            String line;
            while ((line = in.readLine()) != null) {
                response += line;
            }
            in.close();

            // Extract image URL from response
            int start = response.indexOf("\"url\": \"") + 8;
            int end = response.indexOf("\", \"width\":");
            String imageUrl = response.substring(start, end);

            // Display image URL to user
            System.out.println("DALL-E: " + imageUrl);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
