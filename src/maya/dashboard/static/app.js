document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('chat-form');
    const input = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-button');
    const chatHistory = document.getElementById('chat-history');
    const activityLog = document.getElementById('activity-log');

    function addMessage(content, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        // Handle line breaks
        contentDiv.innerHTML = content.replace(/\n/g, '<br>');
        
        messageDiv.appendChild(contentDiv);
        chatHistory.appendChild(messageDiv);
        
        // Scroll to bottom
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    function addActivity(text) {
        const item = document.createElement('div');
        item.className = 'activity-item';
        const time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit', second:'2-digit'});
        item.textContent = `[${time}] ${text}`;
        
        activityLog.appendChild(item);
        activityLog.scrollTop = activityLog.scrollHeight;
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = input.value.trim();
        if (!message) return;
        
        // 1. Show user message
        addMessage(message, 'user');
        input.value = '';
        input.disabled = true;
        sendButton.disabled = true;
        
        addActivity(`Received user command...`);
        
        // 2. Add loading indicator
        const loadingId = 'loading-' + Date.now();
        const loadingHtml = `<div id="${loadingId}" class="message maya-message">
            <div class="message-content" style="opacity: 0.7;">Thinking...</div>
        </div>`;
        chatHistory.insertAdjacentHTML('beforeend', loadingHtml);
        chatHistory.scrollTop = chatHistory.scrollHeight;

        try {
            // 3. Send to Python Backend API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const data = await response.json();
            
            // Remove loading indicator
            document.getElementById(loadingId).remove();
            
            // Check history for any Tool calls that happened in the background and show them
            if (data.history) {
                // Find messages that aren't already displayed
                // For simplicity in this demo, we'll just check the last few messages for Tools
                const tools = data.history.filter(msg => msg.role === "tool");
                // In a production app, we'd sync the exact history properly. 
                // For now, if a tool was executed, log it.
                if (tools.length > 0) {
                    const lastTool = tools[tools.length-1];
                    addMessage(`Executed tool: ${lastTool.name}\nResult: ${lastTool.content}`, 'tool');
                    addActivity(`Executed ${lastTool.name}`);
                }
            }

            // 4. Show MAYA response
            addMessage(data.response, 'maya');
            addActivity(`Task complete.`);

        } catch (error) {
            document.getElementById(loadingId).remove();
            addMessage(`Error connecting to MAYA Core: ${error.message}`, 'tool');
            addActivity(`Error encountered.`);
            console.error(error);
        } finally {
            input.disabled = false;
            sendButton.disabled = false;
            input.focus();
        }
    });
});
