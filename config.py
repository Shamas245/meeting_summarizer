# Configuration file for Meeting Summarizer
# Contains prompts and settings for AI models

# Model Configuration
WHISPER_MODEL = "tiny"  # Options: tiny.en, base.en, small.en, medium.en, large
GEMINI_MODEL = "gemini-1.5-flash"  # Gemini model version
MAX_FILE_SIZE_MB = 100  # Maximum file size in MB
MAX_TRANSCRIPT_LENGTH = 50000  # Maximum transcript length in characters

# Enhanced Summarization Prompt
SUMMARIZATION_PROMPT = """
You are an expert meeting analyst. Analyze the following meeting transcript and create a comprehensive summary.

TRANSCRIPT:
{transcript}

Please provide a well-structured summary that includes:

1. **Meeting Overview**: Brief context and purpose
2. **Key Discussion Points**: Main topics covered (3-5 bullet points)
3. **Decisions Made**: Any concrete decisions or agreements reached
4. **Important Information**: Critical details, numbers, dates, or commitments mentioned
5. **Next Steps**: Any mentioned follow-up activities or future meetings

Format your response in clear, professional language suitable for sharing with stakeholders who weren't present. Keep it concise but comprehensive (aim for 150-300 words).

Focus on actionable information and key takeaways rather than minute details of the conversation flow.
"""

# Enhanced Action Items Prompt
ACTION_ITEMS_PROMPT = """
You are a project management expert. Analyze the following meeting transcript and extract all action items, tasks, and commitments.

TRANSCRIPT:
{transcript}

Extract and format action items following these guidelines:

1. **Identify all actionable tasks**: Look for commitments, assignments, deadlines, and follow-up items
2. **Include responsible parties**: When mentioned, note who is responsible for each task
3. **Include deadlines**: When mentioned, note any specific timelines or due dates
4. **Be specific**: Make each action item clear and actionable

Format each action item as a bullet point starting with "-" and include:
- The specific task or action required
- Who is responsible (if mentioned)
- When it should be completed (if mentioned)
- Any relevant context or requirements

Example format:
- [Task description] - Assigned to [Person] by [Date/Timeline]
- [Task description] - [Additional context if needed]

If no clear action items are found, respond with:
- No specific action items identified in this meeting

Only include items that represent concrete actions to be taken, not general discussion points or informational statements.
"""

# Additional Configuration for Different Meeting Types
MEETING_TYPE_PROMPTS = {
    "standup": {
        "summary": """
        Analyze this standup/daily scrum meeting transcript:
        
        {transcript}
        
        Provide a summary covering:
        1. **Team Updates**: What each team member accomplished
        2. **Current Work**: What everyone is working on today
        3. **Blockers**: Any impediments or challenges mentioned
        4. **Sprint Progress**: Overall team progress toward goals
        
        Keep it concise and focused on status updates.
        """,
        
        "actions": """
        Extract action items from this standup meeting:
        
        {transcript}
        
        Focus on:
        - Tasks to unblock team members
        - Follow-up items mentioned
        - Issues that need resolution
        - Commitments for the day/sprint
        
        Format as bullet points with "-" prefix.
        """
    },
    
    "planning": {
        "summary": """
        Analyze this planning meeting transcript:
        
        {transcript}
        
        Summarize:
        1. **Planning Scope**: What period/project was planned
        2. **Goals & Objectives**: Main targets set
        3. **Resource Allocation**: People, time, budget decisions
        4. **Key Milestones**: Important dates and deliverables
        5. **Risks & Dependencies**: Challenges identified
        
        Focus on strategic decisions and commitments.
        """,
        
        "actions": """
        Extract planning-related action items:
        
        {transcript}
        
        Look for:
        - Tasks to prepare for upcoming work
        - Research or investigation items
        - Resource acquisition needs
        - Milestone preparation activities
        - Risk mitigation actions
        
        Format as bullet points with "-" prefix.
        """
    },
    
    "retrospective": {
        "summary": """
        Analyze this retrospective meeting transcript:
        
        {transcript}
        
        Summarize:
        1. **What Went Well**: Positive outcomes and successes
        2. **What Could Improve**: Areas for enhancement
        3. **Action Items**: Concrete steps for improvement
        4. **Team Insights**: Key learnings and observations
        
        Focus on improvement opportunities and team dynamics.
        """,
        
        "actions": """
        Extract improvement action items from this retrospective:
        
        {transcript}
        
        Focus on:
        - Process improvements to implement
        - Tools or practices to try
        - Training or skill development needs
        - Communication enhancements
        - Team building activities
        
        Format as bullet points with "-" prefix.
        """
    }
}

# Slack Message Configuration
SLACK_CONFIG = {
    "max_message_length": 3000,  # Slack's limit for block text
    "enable_threading": False,   # Whether to use threaded messages
    "mention_channel": False,    # Whether to @channel in messages
    "use_rich_formatting": True  # Whether to use Slack's rich text formatting
}

# File Processing Configuration
AUDIO_CONFIG = {
    "supported_video_formats": ["mp4", "webm", "avi", "mov"],
    "supported_audio_formats": ["mp3", "wav", "m4a", "flac"],
    "audio_quality": "medium",  # Options: low, medium, high
    "audio_sample_rate": 16000,  # Hz - Whisper works best with 16kHz
}

# Error Messages
ERROR_MESSAGES = {
    "file_too_large": "File size exceeds {max_size}MB limit. Please compress your file or use a shorter recording.",
    "no_audio": "No audio detected in the uploaded file. Please ensure your file contains audio content.",
    "transcription_failed": "Failed to transcribe audio. The audio quality may be too poor or the file may be corrupted.",
    "api_error": "AI service is temporarily unavailable. Please try again in a few moments.",
    "slack_error": "Failed to send message to Slack. Please check your webhook URL configuration.",
    "empty_transcript": "No meaningful content found in the transcript. Please provide a longer recording or text.",
    "invalid_file": "Invalid file format. Please upload a supported file type."
}

# Success Messages
SUCCESS_MESSAGES = {
    "processing_complete": "✅ Your meeting has been successfully processed!",
    "slack_sent": "📱 Summary sent to Slack successfully!",
    "file_uploaded": "📁 File uploaded successfully!",
    "transcription_complete": "🎤 Audio transcribed successfully!"
}

# UI Configuration
UI_CONFIG = {
    "theme_color": "#4ECDC4",
    "accent_color": "#FF6B6B", 
    "max_transcript_display": 1000,  # Characters to show in UI preview
    "enable_dark_mode": False,
    "show_processing_steps": True
}