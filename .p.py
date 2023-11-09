import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Teacher"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "teacher the dout solver")

demo.launch(share=True)
