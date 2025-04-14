import os
import openai
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AIDevAgent:
    def __init__(self, project_dir="Test"):
        self.project_dir = project_dir
        self.prompt_history = []
        os.makedirs(self.project_dir, exist_ok=True)

    def run(self):
        print("\n🧠 AI Dev Agent Ready. How can I help you today?")
        while True:
            try:
                user_input = input("\nYou: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("👋 Exiting. Goodbye!")
                    break
                self.prompt_history.append({"role": "user", "content": user_input})
                response = self.ask_openai()
                print("\n🤖 Agent:", response)
                self.execute_code(response)
            except KeyboardInterrupt:
                print("\n👋 Exiting. Goodbye!")
                break

    def ask_openai(self):
        messages = [{"role": "system", "content": "You are a terminal-based AI coding assistant that builds full-stack projects. Respond only with valid Python code wrapped in triple backticks if needed or command-line instructions starting with $ if applicable."}]
        messages.extend(self.prompt_history)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.4
        )
        reply = response.choices[0].message.content.strip()
        self.prompt_history.append({"role": "assistant", "content": reply})
        return reply

    def execute_code(self, response):
        lines = response.splitlines()
        for line in lines:
            if line.startswith("$ "):
                command = line[2:]
                print(f"\n🚀 Running command: {command}")
                result = subprocess.run(command, shell=True, cwd=self.project_dir)
                if result.returncode != 0:
                    print("❌ Command failed")

if __name__ == "__main__":
    agent = AIDevAgent()
    agent.run()
