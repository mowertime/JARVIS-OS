class SessionManager {
    constructor() {
        this.sessionId = this._loadSessionId();
        this.nodeUrl = this._loadNodeUrl();
    }

    _generateUUID() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            const r = Math.random() * 16 | 0;
            return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
        });
    }

    _loadSessionId() {
        let id = localStorage.getItem('jarvis_session_id');
        if (!id) {
            id = this._generateUUID();
            localStorage.setItem('jarvis_session_id', id);
        }
        return id;
    }

    _loadNodeUrl() {
        return localStorage.getItem('jarvis_node_url') || 'http://localhost:8000';
    }

    setNodeUrl(url) {
        this.nodeUrl = url;
        localStorage.setItem('jarvis_node_url', url);
    }

    getSessionId() { return this.sessionId; }
    getNodeUrl() { return this.nodeUrl; }

    async sendRequest(content, inputType = 'text') {
        const response = await fetch(`${this.nodeUrl}/v1/jarvis`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                session_id: this.sessionId,
                timestamp: Date.now(),
                input_type: inputType,
                content: content,
                context: { device: 'arch', state: 'active' }
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        return await response.json();
    }

    async checkHealth() {
        try {
            const response = await fetch(`${this.nodeUrl}/v1/health`);
            return response.ok;
        } catch {
            return false;
        }
    }
}
