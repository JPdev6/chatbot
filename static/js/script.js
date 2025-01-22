document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const chatBody = document.getElementById('chat-body');
    const roomMenu = document.getElementById('room-menu');
    const dropdownItems = document.querySelectorAll('.dropdown-item');

    // Function to load history for the selected room
    async function loadHistory(room) {
        try {
            const response = await fetch(`/history?room=${room}`);
            const data = await response.json();

            chatBody.innerHTML = ''; // Clear chat body

            // Display session and persistent history
            data.session_history.forEach((entry) => {
                appendMessage('user', entry.user);
                appendMessage('bot', entry.bot);
            });

            data.persistent_history.forEach((entry) => {
                appendMessage('user', entry.user_message);
                appendMessage('bot', entry.bot_response);
            });
        } catch (error) {
            console.error('Error loading history:', error);
        }
    }

    // Function to append messages to chat body
    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${sender}`;
        messageDiv.innerHTML = `<div class="chat-bubble">${message}</div>`;
        chatBody.appendChild(messageDiv);
        chatBody.scrollTop = chatBody.scrollHeight; // Scroll to bottom
    }

    // Handle room selection
    dropdownItems.forEach((item) => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const selectedRoom = item.dataset.room;

            // Update the dropdown button label
            roomMenu.textContent = `Room: ${item.textContent}`;

            // Highlight the selected room
            dropdownItems.forEach((i) => i.classList.remove('active'));
            item.classList.add('active');

            // Load history for the selected room
            loadHistory(selectedRoom);
        });
    });

    // Handle new message submission
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const userInput = document.getElementById('message-input').value;
        const room = roomMenu.textContent.replace('Room: ', '').toLowerCase(); // Get selected room

        // Display user message immediately
        appendMessage('user', userInput);

        // Clear input field
        document.getElementById('message-input').value = '';

        try {
            // Fetch bot response
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userInput, room }),
            });

            const data = await response.json();

            // Display bot response
            appendMessage('bot', data.reply);
        } catch (error) {
            console.error('Error sending message:', error);

            // Display error message
            appendMessage('bot', 'Error: Unable to fetch response.');
        }
    });

    // Default: Load history for the initial room
    const defaultRoom = 'general';
    roomMenu.textContent = 'Room: General';
    loadHistory(defaultRoom);
});
