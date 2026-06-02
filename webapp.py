
#pip install gradio
#pip install groq

import gradio as gr
from groq import Groq

#groq api key
api_key = "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"

Client= Groq(api_key=api_key)

# Gradio and groq Ai Based Multi pages websites Generator application

def generate_website(prompt):
    try:
        response = Client.chat.completions.create(
            model ="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": """ 
                   You are a senior web developer  UI/UX Designer  
                   and Frontend Developer with expertise in HTML, CSS,
                   JavaScript, and modern web development frameworks.
                   Your task is to create a multi-page website based on 
                   the user's prompt.
                   The website should be visually appealing, user-friendly,
                   and responsive across different devices.

                   Generate a COMPLETE MULTI-PAGE WEBSITE in 
                   ONE HTML file with embedded CSS and JavaScript
                   using  internal  navigation.
                   
                   STRICT RULES:
                   - must be a full html document 
                   (DOCTYPE, html. head, style, script, body, div)
                   - Must include NAVBAR with links:
                    Home, About, Services, Contact
                    - Each section must behave like a page using anchors (#home, #about, etc.)
                    - Must NOT be white background
                    - Use modern dark or gradient theme
                    - Must include:
                      Hero section (Home)
                      About section
                      Services section (cards)
                      Contact section (form UI)
                    - Must look like a REAL startup website (Stripe / Notion style)
                    - Add hover effects and spacing
                    - Fully responsive design
                   - all css and js must be embedded in the same file
                   - use internal navigation (no external links)
                   - the website should have at least 3 pages (home, about, contact)
                   - the website should be visually appealing and user-friendly
                   - the website should be responsive across different devices
                   - the website should be based on the user's prompt and should include relevant content and images (use placeholders for images)

Return ONLY clean HTML code. """ 
                },
                {
                    "role": "user", 
                    "content": f"""
Create a professional multi-page with style  website 
for a startup based on the following prompt:
{prompt}
make sure to follow the strict rules mentioned in the system prompt and generate a complete HTML file with embedded CSS and JavaScript.
make it modern, beautiful,  and responsive. 
Use placeholders for images and ensure the content is relevant to the startup's theme.
production ready code, no comments, no explanations, no markdown, just clean HTML code.

""" 
                }
            ],
            temperature=0.8
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"<h2 style='color: red;'>An error occurred: {str(e)}</h2>"

app = gr.Blocks(title="AI-Based Multi-Page Website Generator")

with app:
    gr.Markdown("AI-Based Multi-Page Website Generator")
    gr.Markdown("Generate Full Website with Multiple sections (home, About, Services, Contact)")
    prompt = gr.Textbox(
        label="Enter a prompt for your startup website",
        placeholder="e.g., A tech startup that provides AI solutions for businesses.",   
        lines=4
    )
    btn = gr.Button("Generate Website")
    output = gr.HTML()
    btn.click(
        fn=generate_website,
        inputs=prompt,
        outputs=output
    )
app.launch(share=True)
