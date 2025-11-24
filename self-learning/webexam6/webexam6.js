// Simple calculator logic: handles clicks and keyboard input
(() => {
    const display = document.getElementById('display');
    let current = '';
    let lastEval = '';

    function updateDisplay(text) {
        display.textContent = text || '0';
    }

    function press(value) {
        if (value === 'C') {
            current = '';
            lastEval = '';
            updateDisplay('0');
            return;
        }
        if (value === '=') {
            try {
                // evaluate safely: replace ×,÷ if present
                const safe = current.replace(/[^0-9.+\-*/() ]/g, '');
                const result = Function(`"use strict"; return (${safe})`)();
                lastEval = String(result);
                current = lastEval;
                updateDisplay(lastEval);
            } catch (e) {
                updateDisplay('Error');
                current = '';
            }
            return;
        }

        // prevent multiple operators
        const operators = ['+', '-', '*', '/'];
        const lastChar = current.slice(-1);
        if (operators.includes(value)) {
            if (current === '' && value !== '-') return; // don't start with +/*/
            if (operators.includes(lastChar)) {
                current = current.slice(0, -1) + value;
            } else {
                current += value;
            }
        } else if (value === '.') {
            // prevent multiple dots in current number
            const parts = current.split(/\+|\-|\*|\//);
            const lastPart = parts[parts.length - 1];
            if (!lastPart.includes('.')) current += value;
        } else {
            current += value;
        }
        updateDisplay(current);
    }

    // click handlers
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('button');
        if (!btn) return;
        const text = btn.textContent.trim();
        press(text);
    });

    // keyboard support
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') { e.preventDefault(); press('='); return; }
        if (e.key === 'Backspace') { e.preventDefault(); current = current.slice(0, -1); updateDisplay(current); return; }
        if (e.key === 'Escape') { press('C'); return; }
        const allowed = '0123456789+-*/.';
        if (allowed.includes(e.key)) { press(e.key); }
    });

    // initialize
    updateDisplay('0');
})();
