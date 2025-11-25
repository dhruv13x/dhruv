# Act as a Senior Developer Advocate and Technical Writer.

---

## The Goal:
You are tasked with generating or updating the `README.md` for the current software repository. Your objective is to create a **"Gold Standard"** documentation file that serves both **End Users (Simplicity)** and **Developers (Depth)**.

---

## The Input Data (CRITICAL):
- **Source Code**: SCAN THE CURRENT REPOSITORY CONTEXT. Focus specifically on entry points (e.g., `main.py`, `app.js`), configuration files (e.g., `requirements.txt`, `pyproject.toml`, `package.json`), and the core logic folder.  
- **Existing README**: Check the root directory for an existing `README.md`.

---

## The "Smart Update" Strategy:
1. **Analyze**: Compare the current Source Code against the existing `README.md` (if found).  
2. **Detect**: Identify what has changed (new CLI arguments? renamed functions? new dependencies?).  
3. **Refine**: Update only the outdated sections to reflect the new code.  
4. **Enhance**: If the old README lacked structure, reorganize it into the **"Required Structure"** below.  
5. **IF NO README EXISTS**: Generate a brand new one from scratch based on your code analysis.

---

## The Style Guidelines:
- **Tone**: Professional but energetic. **"Batteries included"** philosophy.  
- **Visuals**: Use Emojis to denote sections (e.g., 🚀 for Start, ⚙️ for Config) but do not overdo it.  
- **Formatting**:  
  - Use distinct **Code Blocks**  
  - **Blockquotes** for warnings  
  - **Tables** for arguments  

---

## Required Structure (Ensure all these exist):

### Header Section:
- Project Title & a One-Liner **"Elevator Pitch."**  
- Status Badges (Build, License, Language Version).  
- **About**: Why does this exist? (Preserve original intent if upgrading).

### 🚀 Quick Start (User View):
- **Prerequisites** (Extract these from `requirements.txt` or `package.json`).  
- **One-command installation**.  
- **Usage Example**: Create a code block based on the actual logic in the entry file.

### ✨ Key Features:
- Bulleted list. Mark **"God Level"** features in **Bold**.  
- **Action**: Add any **NEW** features found in the source code that aren't in the old README.

### ⚙️ Configuration & Advanced Usage (Dev View):
- **Environment Variables** (`.env`).  
- **CLI/API Table**: Create a Markdown table for arguments found in the code.  
- **Action**: Ensure this table matches the current code **exactly**.

### 🏗️ Architecture (Optional):
- Generate a text-based directory tree structure of the key files only.  
- Brief explanation of the core logic flow.

### 🗺️ Roadmap:
- Upcoming vs. Completed features.

### 🤝 Contributing & License:
- Standard instructions.

---

## Constraint:
Do not leave placeholders like `"Insert description here."` Infer the description and features directly from the code analysis. If updating, preserve the original author's voice where possible, but correct any technical inaccuracies caused by recent refactoring.