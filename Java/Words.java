import java.util.Random;

public class TextGenerator {
    public static void main(String[] args) {
        // Words to combine into random sentences
        String[] words = {"Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"};

        // Create a Random object
        Random rand = new Random();

        // Membuat kalimat acak
        String sentence = "";
        for (int i = 0; i < 5; i++) {
            int index = rand.nextInt(words.length);
            sentence += words[index] + " ";
        }

        // Displays a random sentence
        System.out.println(sentence);
    }
}
