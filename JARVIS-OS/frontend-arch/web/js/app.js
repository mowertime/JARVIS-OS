class App {
    constructor() {
        this.session = new SessionManager();
        this.voice = new VoiceManager();
        this.isProcessing = false;
        
        this._initElements();
        this._bindEvents();
        this._initVoice();
        this._checkConnection();
    }

    _initElements() {
        this.messages = document.getElementById('messages');
        this.textInput = document.getElementById('text-input');
        this.sendBtn = document.getElementById('send-btn');
        this.voiceBtn = document.getElementById('voice-btn');
        this.statusIndicator = document.getElementById('status-indicator');
        this.connectionStatus = document.getElementById('connection-status');
        this.settingsBtn = document.getElementById('settings-btn');
        this.settingsModal = document.getElementById('settings-modal');
        this.nodeIpInput = document.getElementById('node-ip');
        this.sessionIdDisplay = document.getElementById('session-id-display');
        this.saveSettingsBtn = document.getElementById('save-settings');
    }

    _bindEvents() {
        this.sendBtn.addEventListener('click', () => this._handleSend());
        this.textInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this._handleSend();
            }
        });
        this.voiceBtn.addEventListener('click', () => this._handleVoiceToggle());
        this.settingsBtn.addEventListener('click', () => this._showSettings());
        document.querySelector('.close').addEventListener('click', () => this._hideSettings());
        this.saveSettingsBtn.addEventListener('click', () => this._saveSettings());
        
        window.addEventListener('click', (e) => {
            if (e.target === this.settingsModal) this._hideSettings();
        });
    }

    _initVoice() {
        if (this.voice.init()) {
            this.voice.onWakeWord = () => {
                this._setStatus('speaking');
                this.voice.start();
            };
            
            this.voice.onResult = (transcript) => {
                this._setStatus('active');
                this._processInput(transcript, 'voice');
            };
        } else {
            this.voiceBtn.style.display = 'none';
        }
    }

    async _checkConnection() {
        const connected = await this.session.checkHealth();
        this.connectionStatus.textContent = connected ? 'Connected' : 'Disconnected';
        this.connectionStatus.className = connected ? 'connected' : '';
        setTimeout(() => this._checkConnection(), 30000);
    }

    async _handleSend() {
        const content = this.textInput.value.trim();
        if (!content || this.isProcessing) return;
        
        this.textInput.value = '';
        await this._processInput(content, 'text');
    }

    async _processInput(content, inputType) {
        this.isProcessing = true;
        this._setStatus('active');
        
        this._addMessage(content, 'user');
        this._showTyping();
        
        try {
            const response = await this.session.sendRequest(content, inputType);
            this._removeTyping();
            
            const statusClass = response.status === 'failed' ? 'error' : 'jarvis';
            let outputText = response.output || 'No response';
            
            if (response.steps && response.steps.length > 1) {
                const stepInfo = response.steps.map(s => 
                    `Step ${s.id}: ${s.model} - ${s.instruction.substring(0, 50)}...`
                ).join('\n');
                outputText += `\n\n[Pipeline: ${response.steps.length} steps]`;
            }
            
            if (response.tool_calls && response.tool_calls.length > 0) {
                outputText += `\n[Tools: ${response.tool_calls.length} executed]`;
            }
            
            this._addMessage(outputText, statusClass);
            
            if (response.status === 'failed') {
                this._addMessage(`Error: ${response.error?.message || 'Unknown error'}`, 'error');
            }
            
            if (inputType === 'voice') {
                this.voice.speak(response.output || 'Processing complete.');
            }
            
            this._setStatus('idle');
        } catch (error) {
            this._removeTyping();
            this._addMessage(`Connection error: ${error.message}`, 'error');
            this._setStatus('idle');
            this.connectionStatus.textContent = 'Disconnected';
            this.connectionStatus.className = '';
        }
        
        this.isProcessing = false;
    }

    _handleVoiceToggle() {
        const nowListening = this.voice.toggle();
        this.voiceBtn.classList.toggle('listening', nowListening);
        this.voiceBtn.title = nowListening ? 'Listening... (Click to stop)' : 'Voice Input';
    }

    _addMessage(text, type) {
        const div = document.createElement('div');
        div.className = `message ${type}`;
        
        const content = document.createElement('div');
        content.textContent = text;
        
        const timestamp = document.createElement('div');
        timestamp.className = 'timestamp';
        timestamp.textContent = new Date().toLocaleTimeString();
        
        div.appendChild(content);
        div.appendChild(timestamp);
        this.messages.appendChild(div);
        this._scrollToBottom();
    }

    _showTyping() {
        const div = document.createElement('div');
        div.className = 'message jarvis';
        div.id = 'typing-indicator';
        
        const indicator = document.createElement('div');
        indicator.className = 'typing-indicator';
        indicator.innerHTML = '<span></span><span></span><span></span>';
        
        div.appendChild(indicator);
        this.messages.appendChild(div);
        this._scrollToBottom();
    }

    _removeTyping() {
        const typing = document.getElementById('typing-indicator');
        if (typing) typing.remove();
    }

    _setStatus(state) {
        this.statusIndicator.className = `status-${state}`;
    }

    _scrollToBottom() {
        const container = document.getElementById('chat-container');
        container.scrollTop = container.scrollHeight;
    }

    _showSettings() {
        this.nodeIpInput.value = this.session.getNodeUrl();
        this.sessionIdDisplay.textContent = this.session.getSessionId();
        this.settingsModal.classList.remove('hidden');
    }

    _hideSettings() {
        this.settingsModal.classList.add('hidden');
    }

    _saveSettings() {
        const url = this.nodeIpInput.value.trim();
        if (url) {
            this.session.setNodeUrl(url);
        }
        this._hideSettings();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
