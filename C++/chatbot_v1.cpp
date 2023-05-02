#include <iostream>
#include <cpprest/http_client.h>
#include <cpprest/json.h>

using namespace std;
using namespace web;
using namespace web::http;
using namespace web::http::client;

// set API key
const string api_key = "YOUR_API_KEY";

// define function to prompt OpenAI API
string ask_openai(string prompt, string model) {
    http_client client(U("https://api.openai.com/v1/"));

    // set API endpoint and parameters
    uri_builder builder(U("completions"));
    builder.append_query(U("engine"), U(model));
    builder.append_query(U("prompt"), U(prompt));
    builder.append_query(U("max_tokens"), U("100"));
    builder.append_query(U("n"), U("1"));
    builder.append_query(U("stop"), U("\n"));
    builder.append_query(U("temperature"), U("0.7"));

    // set HTTP request headers
    http_request request(methods::POST);
    request.set_request_uri(builder.to_uri());
    request.headers().add("Authorization", "Bearer " + api_key);
    request.headers().add("Content-Type", "application/json");

    // send HTTP request and receive response
    pplx::task<http_response> response = client.request(request);
    response.wait();

    // extract response content
    pplx::task<web::json::value> content = response.get().extract_json();
    content.wait();
    string message = content.get()["choices"][0]["text"].as_string();

    return message;
}

int main() {
    // prompt user for input and pass to OpenAI API
    while (true) {
        string user_input;
        cout << "You: ";
        getline(cin, user_input);

        string response = ask_openai(user_input, "davinci");

        // perform chatbot task based on user input
        if (user_input.find("hello") != string::npos) {
            response = "Hi there!";
        }
        else if (user_input.find("bye") != string::npos) {
            response = "Goodbye!";
            break;
        }

        cout << "Bot: " << response << endl;
    }

    return 0;
}
