This is a report about my Prompt Injection Project. Citations and overview will be avaliable in this Report.

If you did want to run this project you will need your own OPENAI_API_KEY:

To run this project:

1. Install dependencies:
   pip install openai

2. Set your OpenAI API key:

   Windows:
   setx OPENAI_API_KEY "your-key-here"

   Mac/Linux:
   export OPENAI_API_KEY="your-key-here"

3. Run:
   python Prompt.py

How to use this project:
At the top of the program in Prompt.py you will see a value called MODE, there are two modes for this project. One being
"vulnerable", when ran we are able to explore attack via injection is this vulnerable AI state. The other being "guarded"
where these attacks will have preventions from attacking our AI model. Feel free to switch between the two and explore
on your own.

In this project I demonstrate prompt injection attacks, along with these attacks I will demonstrate and explain secuirty 
topics I used for the attacks. I will also explain how to safeguard such attacks. First of all I decided to use OpenAi's 
model in python as the specific topic I would like to demonstrate is prompt injection attack on AI as AI is found everywhere 
currently, such as Apps, wesbites and more. The 6 attacks I demonstrate are; Secure system design, User Authentications, 
Userinput (direct injection), Malious documentation input (indirect injection), Overloading/flooding, Functionalilty abuse.
Throughout the project I will use two system prompts for the AI; one which is a loose model that is vulnerable to such attacks,
while the other is a stronger model that would be more likely used for the fake banking app I represent within this project.

Secure System Design:
Having a secure system design is step one when it comes to preventing security attacks. For example in a poor design a developer
might accidentally give their AI model access to sensitive data or input sensitive data in incorrect spots. However some designs
require an AI to see some data which enforces why it is important to have a strong system prompt and not improperly place sensitive 
data. A good way to avoid this is to make sure a system's design is not vulnerable such as including sensitive data in random places.

User Authentication:
User authentication is important when it comes to any app/website. Ensuring certain roles can do certain actions. In the naive AI
prompt anyone who claims to be admin can see the secret value. A fix to this is to create user authentication making sure people who 
are only truly admin be able to view the secret value. (I do this by giving each role certain AI models).

UserInput (direct injection):
With a naive/weak system prompt user input can be powerful. For example someone might make the AI to ensure user happiness and fullfil
all their requests. However this can be vulnerable since they can ask the AI to ignore previous instructions. A fix would be to tell
the system prompt to never share sensitive data.

Malious documentation input (indirect injection):
Malious documentation can be dangerous to prompts that believe/trust a user, for example a malious document can change an entire
system prompt. A fix would be to construct a prompt that includes rules to never listen to rule changes or overrides.

Overloading:
Overloading can be harmful as it may cause drift, messy responses, and cost increases. A way to fix this is to set a reasonable
character limit to the your service. The pretend banking app questions are for general questions, so 800 chars in this example seems 
reasonable.

Functionality Abuse:
Since developers may want a content experience for their users, once again their prompt may be to listen to the user's prompts. This
can lead to vulnerability such as users changing/viewing sensitve data. A way to fix this is to ensure most user's cannot change
internal data.

Citations:
https://developers.openai.com/api/docs/guides/text
https://platform.openai.com/login
https://medium.com/@max.petrusenko/mcp-vs-cli-why-context-bloat-is-killing-ai-agent-performance-b4f421325da4
CSC 321 Lectures
    -Module 1 Computer Security Concepts
    -Module 4 User Authentication
    -Module 5 Access Control
    -Module 6 Malicious Software


