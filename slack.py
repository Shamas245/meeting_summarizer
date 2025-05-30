import requests
import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

def send_to_slack(summary: str, action_items: str, webhook_url: str) -> bool:
    """
    Send meeting summary and action items to Slack using webhook
    
    Args:
        summary: Meeting summary text
        action_items: Action items as formatted string
        webhook_url: Slack webhook URL
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if not webhook_url or not webhook_url.startswith('https://hooks.slack.com/'):
            logger.error("Invalid Slack webhook URL")
            return False
        
        if not summary.strip() and not action_items.strip():
            logger.error("No content to send to Slack")
            return False
        
        # Format action items for better display
        formatted_action_items = ""
        if action_items.strip():
            items = [item.strip() for item in action_items.split('\n') if item.strip()]
            formatted_action_items = "\n".join([f"• {item.lstrip('- •*')}" for item in items])
        
        # Create Slack message with proper block structure
        slack_message = {
            "blocks": [  # Fixed: was "blocks exposition" - should be "blocks"
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text", 
                        "text": f"📝 Meeting Summary - {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*📋 Summary:*\n{summary}"
                    }
                }
            ]
        }
        
        # Add action items section if they exist
        if formatted_action_items:
            slack_message["blocks"].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*✅ Action Items:*\n{formatted_action_items}"
                }
            })
        
        # Add footer
        slack_message["blocks"].extend([
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"Generated by Meeting Summarizer | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    }
                ]
            }
        ])
        
        # Send the message
        response = requests.post(
            webhook_url, 
            json=slack_message,
            timeout=30,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            logger.info("Slack message sent successfully")
            return True
        else:
            logger.error(f"Slack API error {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        logger.error("Slack request timed out")
        return False
    except requests.exceptions.ConnectionError:
        logger.error("Failed to connect to Slack")
        return False
    except Exception as e:
        logger.error(f"Slack send error: {str(e)}")
        return False

def validate_webhook_url(webhook_url: str) -> bool:
    """
    Validate Slack webhook URL format
    
    Args:
        webhook_url: URL to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not webhook_url:
        return False
    
    return (
        webhook_url.startswith('https://hooks.slack.com/') and
        len(webhook_url) > 50  # Basic length check
    )

def test_slack_connection(webhook_url: str) -> tuple[bool, str]:
    """
    Test Slack webhook connection
    
    Args:
        webhook_url: Slack webhook URL
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        if not validate_webhook_url(webhook_url):
            return False, "Invalid webhook URL format"
        
        test_message = {
            "text": "🧪 Test message from Meeting Summarizer - connection successful!"
        }
        
        response = requests.post(
            webhook_url,
            json=test_message,
            timeout=10,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            return True, "Connection successful"
        else:
            return False, f"HTTP {response.status_code}: {response.text}"
            
    except Exception as e:
        return False, f"Connection failed: {str(e)}"