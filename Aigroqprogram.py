#Ai Agentic with Groq Ai Model
# pip install  groq
from groq import Groq
class AIGROQAgent:
    def __init__(self, api_key, model_name="llama-3.3-70b-versatile"):
        # Initialize Groq Client
        self.client = Groq(api_key=api_key)
        self.model_name = model_name
    # Generate AI Response
    def generate_response(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        return response.choices[0].message.content
    
    # Agent Task Execution Process
    def execute_task(self, task_details):
        task_prompt=f"""
        your are an autonomous Ai Agent.
        Task
        {task_details}
        provide the solve this task step-by-step.
        """
        return self.generate_response(task_prompt)
    
    #Learning /Reflection Process
    def learn_from_experience(self, experience_details):
        learning_prompt=f"""
        you are an autonomous Ai Agent.
        Analyze the following expreience  
        and provide insights for improvement.
        Experience
        {experience_details}
        Reflect on this experience and provide insights for improvement.
        """
        return self.generate_response(learning_prompt)


if __name__ == "__main__":
    while True:

        API_key = ## use a api key
        agent = AIGROQAgent(API_key)

        # prompt = input("Enter your prompt: ")
        # response = agent.generate_response(prompt)
        # print("AI Response:", response)

        # prompt1 ="provide thr top 3  Bike Compenys List with   details"
        # response1=agent.execute_task(prompt1)
        # print("AI Task Response:", response1)

        prompt2 =  input("Enter the Prompt") #"Students enjoyed hands-on AI demos but struggled with R Lang setup."
        if prompt2.lower() == "exit":
            print("Exiting the program.")
            break
        response2 = agent.learn_from_experience(prompt2)
        print("AI Learning Response:", response2)   
