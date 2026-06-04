# Automated Text File Summarization System

Automatically generate AI-powered summaries of text files and push them to GitHub using a post-commit Git hook.

## 🎯 Features

- ✅ **Automatic Detection**: Detects new `.txt` files added in commits
- ✅ **AI-Powered Summaries**: Uses OpenAI API to generate intelligent summaries
- ✅ **Organized Output**: Appends summaries to `summary.md` with timestamps
- ✅ **Git Integration**: Automatically commits and pushes summaries to GitHub
- ✅ **Zero Manual Work**: Runs automatically after each commit
- ✅ **Error Handling**: Graceful error handling that won't break your workflow

## 📋 Prerequisites

- Python 3.8 or higher
- Git 2.0 or higher
- OpenAI API account with API key
- GitHub repository with push access

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure OpenAI API Key

Create a `.env` file in the root directory:

```bash
# On Windows (PowerShell)
New-Item -Path .env -ItemType File

# On Linux/macOS
touch .env
```

Add your OpenAI API key to `.env`:

```
OPENAI_API_KEY=sk-proj-your-api-key-here
```

**Important**: Never commit the `.env` file to Git. It's already excluded via `.gitignore`.

### 4. Set Up Git Hook

#### On Windows (PowerShell):

```powershell
# Create the hooks directory if it doesn't exist
New-Item -Path .git\hooks -ItemType Directory -Force

# Copy the post-commit hook
Copy-Item scripts\post-commit.ps1 .git\hooks\post-commit
```

#### On Linux/macOS:

```bash
# Copy the post-commit hook
cp scripts/post-commit.sh .git/hooks/post-commit

# Make it executable
chmod +x .git/hooks/post-commit
```

### 5. Test the Setup

Create a test text file:

```bash
echo "This is a test file for the summarization system." > test.txt
git add test.txt
git commit -m "Add test file"
```

The system will automatically:
1. Detect `test.txt`
2. Generate a summary
3. Append it to `summary.md`
4. Commit and push the changes

Check `summary.md` to see the generated summary!

## 📖 How It Works

```mermaid
flowchart LR
    A[Add .txt file] --> B[git commit]
    B --> C[Post-commit hook]
    C --> D[Python script]
    D --> E[OpenAI API]
    E --> F[summary.md]
    F --> G[Auto commit & push]
```

1. **You commit** a new `.txt` file to the repository
2. **Git hook triggers** the Python script automatically
3. **Script detects** the new text file(s)
4. **OpenAI generates** an intelligent summary
5. **Summary appended** to `summary.md` with timestamp
6. **Changes committed** and pushed to GitHub

## 📁 Project Structure

```
repository/
├── .git/
│   └── hooks/
│       └── post-commit          # Git hook (auto-triggers script)
├── scripts/
│   ├── summarize_text.py        # Main Python script
│   ├── post-commit.sh           # Linux/macOS hook template
│   └── post-commit.ps1          # Windows hook template
├── .env                         # API key (DO NOT COMMIT)
├── .gitignore                   # Excludes .env and other files
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── IMPLEMENTATION_PLAN.md       # Detailed implementation guide
├── TECHNICAL_SPECIFICATION.md   # Technical details
└── summary.md                   # Generated summaries (auto-created)
```

## 🔧 Configuration

### Environment Variables

Edit `.env` to customize behavior:

```
# Required
OPENAI_API_KEY=sk-proj-your-api-key-here

# Optional (with defaults)
OPENAI_MODEL=gpt-3.5-turbo
MAX_TOKENS=150
TEMPERATURE=0.7
```

### Supported File Types

By default, only `.txt` files are processed. To support additional file types, edit `scripts/summarize_text.py`:

```python
# Find this line:
if file.endswith('.txt'):

# Change to:
if file.endswith(('.txt', '.md', '.log')):
```

## 📝 Summary Format

Summaries are appended to `summary.md` in this format:

```markdown
## [filename.txt] - 2026-06-04 13:10:25

This is the AI-generated summary of the file content. It provides
a concise overview of the main points and key information.

---
```

## 🐛 Troubleshooting

### Hook Not Triggering

**Problem**: Script doesn't run after commit

**Solutions**:
- Verify hook file exists: `.git/hooks/post-commit`
- Check if hook is executable (Linux/macOS): `ls -l .git/hooks/post-commit`
- Make it executable: `chmod +x .git/hooks/post-commit`
- Check Python path in hook script

### API Key Error

**Problem**: "OpenAI API key not found"

**Solutions**:
- Verify `.env` file exists in root directory
- Check API key format: `OPENAI_API_KEY=sk-proj-...`
- Ensure no spaces around the `=` sign
- Verify API key is valid on OpenAI platform

### Push Failures

**Problem**: Changes not pushed to GitHub

**Solutions**:
- Check Git remote is configured: `git remote -v`
- Verify you have push access to the repository
- Check your Git credentials are set up
- Try manual push: `git push origin main`

### No Summary Generated

**Problem**: `summary.md` not created or updated

**Solutions**:
- Check if file is actually a `.txt` file
- Verify file was added (not just modified)
- Check Python script logs for errors
- Test script manually: `python scripts/summarize_text.py`

## 💰 Cost Estimation

Using OpenAI GPT-3.5-turbo:

- **Per file**: ~$0.002 (for average 1000-word file)
- **100 files/month**: ~$0.20
- **1000 files/month**: ~$2.00

**Tip**: Set usage limits in your OpenAI account to control costs.

## 🔒 Security Best Practices

- ✅ Never commit `.env` file
- ✅ Use SSH keys for Git authentication
- ✅ Rotate API keys periodically
- ✅ Set OpenAI usage limits
- ✅ Review `.gitignore` before committing
- ✅ Use environment-specific API keys (dev/prod)

## 🧪 Testing

### Manual Test

```bash
# Create a test file
echo "The quick brown fox jumps over the lazy dog." > test_file.txt

# Commit it
git add test_file.txt
git commit -m "Test summarization"

# Check the result
cat summary.md
```

### Verify Automation

```bash
# Check if hook exists
ls -la .git/hooks/post-commit

# Check if Python script exists
ls -la scripts/summarize_text.py

# Test Python script directly
python scripts/summarize_text.py
```

## 📚 Additional Documentation

- [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md) - Detailed architecture and workflow
- [`TECHNICAL_SPECIFICATION.md`](TECHNICAL_SPECIFICATION.md) - Technical details and API specs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the logs in `logs/summarization.log`
3. Open an issue on GitHub with:
   - Error message
   - Steps to reproduce
   - Your environment (OS, Python version)

## 🎉 Success Indicators

You'll know it's working when:

- ✅ `summary.md` is created after committing a `.txt` file
- ✅ Summary contains AI-generated content
- ✅ Changes are automatically pushed to GitHub
- ✅ No errors appear in your terminal
- ✅ Process completes in 2-5 seconds

## 🔄 Workflow Example

```bash
# Day 1: Add meeting notes
echo "Meeting notes from project kickoff..." > meeting_notes.txt
git add meeting_notes.txt
git commit -m "Add meeting notes"
# ✅ Summary automatically generated and pushed

# Day 2: Add research findings
echo "Research findings on AI summarization..." > research.txt
git add research.txt
git commit -m "Add research findings"
# ✅ Another summary added to summary.md

# Check all summaries
cat summary.md
```

## 🚀 Next Steps

After setup:

1. ✅ Test with a sample file
2. ✅ Review generated summary quality
3. ✅ Adjust OpenAI parameters if needed
4. ✅ Start using it in your daily workflow
5. ✅ Monitor API usage and costs

---

**Happy Summarizing! 🎊**
