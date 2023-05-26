"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
import openai

openai.api_key = "YOUR_API_KEY"
model = "gpt-3.5-turbo"
preprompt = [{"role": "system", "content": "你是阿彭巴巴電商的客服白白，為了降低成本提高效率，你會長話短說，每次回答字數不超過30個繁體中文字。"}]

class State(pc.State):
    """The app state."""
    prompt = ""
    result = ""
    def get_result(self):
        self.result = openai.ChatCompletion.create(
            model=model,
            messages=preprompt+[{"role": "user", "content": self.prompt}]
            ).choices[0].message.content
        print(self.result)

    # image_url = ""
    # image_processing = False
    # image_made = False

    # def process_image(self):
    #     """Set the image processing flag to true and indicate that the image has not been made yet."""
    #     self.image_made = False
    #     self.image_processing = True

    # def get_image(self):
    #     """Get the image from the prompt."""
    #     try:
    #         response = openai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
    #         self.image_url = response["data"][0]["url"]
    #         # Set the image processing flag to false and indicate that the image has been made.
    #         self.image_processing = False
    #         self.image_made = True
    #     except:
    #         self.image_processing = False
    #         return pc.window_alert("Error with OpenAI Execution.")


def index():
    return pc.center(
        pc.vstack(
            # pc.heading("Live Chat", font_size="1.5em"),
            pc.input(placeholder='請問...', on_blur=State.set_prompt),
            pc.button(
                "送出",
                on_click=[State.get_result],
                width="100%",
            ),
            pc.divider(),
            pc.image(src="https://x1001000-linebot-content.s3.ap-east-1.amazonaws.com/GPT-LightSPA/whitewhite.png", width="512px", height="auto"),
            # pc.cond(
            #     State.image_processing,
            #     pc.circular_progress(is_indeterminate=True),
            #     pc.cond(
            #         State.image_made,
            #         pc.image(
            #             src=State.image_url,
            #             height="25em",
            #             width="25em",
            #         ),
            #     ),
            # ),
            pc.text_area(
                default_value=State.result,
                # placeholder="GPT Result",
                width="100%",
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Live Streaming Demo")
app.compile()
