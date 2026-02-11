---
trigger: always_on
---

---
description: Smart Workflow: Think -> Search -> Comprehend -> Plan -> Execute.
---

This workflow ensures Agent Gemini follows a strict protocol for complex tasks:

1. **Thinking Phase**
   - Analyze the user request deeply to identify core requirements and constraints.
   - List key search terms and concepts that need clarification.

2. **Research Phase**
   - Use the `search_web` tool to find relevant documentation, tutorials, or examples.
   - Select the most promising URLs and read their content using `read_url_content` or `read_browser_page`.

3. **Comprehension Phase**
   - Summarize the gathered information.
   - Identify best practices and potential pitfalls.

4. **Planning Phase**
   - Create a detailed step-by-step plan based on the research.
   - Ensure the plan addresses all user requirements.

5. **Execution Phase**
   - Execute the plan step-by-step.
   - Verify the results after each step.
