class VoiceManager {
    constructor() {
        this.isListening = false;
        this.wakeWord = 'hey jarvis';
        this.recognition = null;
        this.synthesis = window.speechSynthesis;
        this.onWakeWord = null;
        this.onResult = null;
        this.isSpeaking = false;
    }

    init() {
        if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
            console.warn('Speech recognition not available');
            return false;
        }

        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        this.recognition = new SpeechRecognition();
        this.recognition.continuous = true;
        this.recognition.interimResults = true;
        this.recognition.lang = 'en-US';

        this.recognition.onresult = (event) => {
            let finalTranscript = '';
            let interimTranscript = '';

            for (let i = event.resultIndex; i < event.results.length; i++) {
                const transcript = event.results[i][0].transcript.toLowerCase().trim();
                if (event.results[i].isFinal) {
                    finalTranscript += transcript;
                } else {
                    interimTranscript += transcript;
                }
            }

            if (finalTranscript) {
                this._handleTranscript(finalTranscript);
            }
        };

        this.recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            if (event.error === 'not-allowed') {
                this.stop();
            }
        };

        return true;
    }

    _handleTranscript(transcript) {
        if (this.isSpeaking) return;

        if (transcript.includes(this.wakeWord)) {
            if (this.onWakeWord) this.onWakeWord();
            this.speak('Go ahead, sir.');
        } else if (transcript.length > 0) {
            if (this.onResult) this.onResult(transcript);
        }
    }

    start() {
        if (this.recognition) {
            try {
                this.recognition.start();
                this.isListening = true;
                return true;
            } catch (e) {
                console.error('Failed to start recognition:', e);
                return false;
            }
        }
        return false;
    }

    stop() {
        if (this.recognition) {
            try {
                this.recognition.stop();
            } catch (e) { /* ignore */ }
            this.isListening = false;
        }
    }

    speak(text, onEnd = null) {
        if (!this.synthesis) { if (onEnd) onEnd(); return; }
        
        this.synthesis.cancel();
        this.isSpeaking = true;
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        utterance.volume = 1.0;
        
        utterance.onend = () => {
            this.isSpeaking = false;
            if (onEnd) onEnd();
        };

        utterance.onerror = () => {
            this.isSpeaking = false;
            if (onEnd) onEnd();
        };

        this.synthesis.speak(utterance);
    }

    toggle() {
        if (this.isListening) {
            this.stop();
        } else {
            this.start();
        }
        return this.isListening;
    }
}
