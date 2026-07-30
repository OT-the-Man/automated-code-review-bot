import os
from dotenv import load_dotenv
from google import genai
import requests

load_dotenv()

repo = os.environ["REPO"]
pr_number = os.environ["PR_NUMBER"]
github_token = os.environ["GITHUB_TOKEN"]
gemini_key = os.environ["GEMINI_API_KEY"]

# 1. Fetch the real PR diff from GitHub
diff_response = requests.get(
    f"https://api.github.com/repos/{repo}/pulls/{pr_number}",
    headers={
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3.diff"
    }
)
diff = diff_response.text

# 2. Send it to Gemini for review
client = genai.Client(api_key=gemini_key)

prompt = f"""You are reviewing a pull request. Below is the code diff (lines
starting with + are added, - are removed). Point out any bugs, potential
issues, or bad practices in the ADDED lines specifically. Be specific about
which line and why it's a problem. If nothing looks wrong, say so. Keep it
concise, formatted in Markdown.

Diff:
{diff}"""

review = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
).text

# 3. Post the review as a comment on the PR
requests.post(
    f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments",
    headers={
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json"
    },
    json={"body": f"### 🤖 AI Code Review\n\n{review}"}
)

print("Review posted.")