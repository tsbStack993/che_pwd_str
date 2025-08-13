from flask import Flask, render_template_string, request
from che_pwd import check_password_strength

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Password Strength Checker</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-blue-100 to-purple-200 min-h-screen flex items-center justify-center">
    <div class="bg-white shadow-xl rounded-xl p-8 w-full max-w-md">
        <h2 class="text-2xl font-bold mb-6 text-center text-purple-700">🔒 Password Strength Checker</h2>
        <div class="mb-4 text-xs text-yellow-700 bg-yellow-100 border-l-4 border-yellow-400 p-2 rounded">
            <b>Privacy Notice:</b>This tool is for testing purposes only and does not store any passwords.
        </div>
        <form method="post" class="flex flex-col gap-4">
            <div class="relative">
                <input type="password" id="password" name="password" placeholder="Enter password"
                    class="border border-purple-300 rounded px-4 py-2 w-full focus:outline-none focus:ring-2 focus:ring-purple-400 pr-10"
                    required>
                <button type="button" onclick="togglePassword()" tabindex="-1"
                    class="absolute right-2 top-2 text-gray-500 hover:text-purple-600 focus:outline-none">
                    <svg id="eye" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none"
                        viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M2.458 12C3.732 7.943 7.523 5 12 5c4.477 0 8.268 2.943 9.542 7-1.274 4.057-5.065 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                </button>
            </div>
            <button type="submit"
                class="bg-purple-600 hover:bg-purple-700 text-white font-semibold py-2 rounded transition">Check Strength</button>
        </form>
        {% if result %}
        <div class="mt-8">
            <h3 class="text-lg font-semibold mb-2">Result:</h3>
            <div class="flex items-center gap-2 mb-2">
                <span class="font-mono text-gray-700">Strength:</span>
                <span class="font-bold {% if result.is_strong %}text-green-600{% else %}text-red-600{% endif %}">
                    {{ result.strength }} ({{ 'Strong' if result.is_strong else 'Weak' }})
                </span>
            </div>
            <ul class="space-y-1 text-sm">
                <li class="flex items-center justify-between">
                    <span class="font-mono">Length ≥ 8:</span>
                    <span>{% if result.length %}✅{% else %}❌{% endif %}</span>
                </li>
                <li class="flex items-center justify-between">
                    <span class="font-mono">Uppercase:</span>
                    <span>{% if result.uppercase %}✅{% else %}❌{% endif %}</span>
                </li>
                <li class="flex items-center justify-between">
                    <span class="font-mono">Lowercase:</span>
                    <span>{% if result.lowercase %}✅{% else %}❌{% endif %}</span>
                </li>
                <li class="flex items-center justify-between">
                    <span class="font-mono">Digit:</span>
                    <span>{% if result.digit %}✅{% else %}❌{% endif %}</span>
                </li>
                <li class="flex items-center justify-between">
                    <span class="font-mono">Special Char:</span>
                    <span>{% if result.special %}✅{% else %}❌{% endif %}</span>
                </li>
                <li class="flex items-center justify-between">
                    <span class="font-mono">Not Common:</span>
                    <span>{% if result.not_common %}✅{% else %}❌{% endif %}</span>
                </li>
            </ul>
            {% if suggestions %}
            <div class="mt-4 bg-blue-50 border-l-4 border-blue-400 text-blue-800 p-2 rounded text-sm">
                <b>Suggestions:</b>
                <ul class="list-disc ml-6">
                    {% for s in suggestions %}
                    <li>{{ s }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endif %}
            <div class="text-xs text-gray-800 mt-4 bg-gray-100 p-2 rounded text-center">Checked at: {{ result.timestamp }}</div>
        </div>
        {% endif %}
    </div>
    <script>
        function togglePassword() {
            const pwd = document.getElementById('password');
            const eye = document.getElementById('eye');
            if (pwd.type === 'password') {
                pwd.type = 'text';
                eye.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M13.875 18.825A10.05 10.05 0 0112 19c-4.477 0-8.268-2.943-9.542-7a9.956 9.956 0 012.293-3.95m1.414-1.414A9.956 9.956 0 0112 5c4.477 0 8.268 2.943 9.542 7a9.956 9.956 0 01-4.293 5.95M15 12a3 3 0 11-6 0 3 3 0 016 0z" />`;
            } else {
                pwd.type = 'password';
                eye.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M2.458 12C3.732 7.943 7.523 5 12 5c4.477 0 8.268 2.943 9.542 7-1.274 4.057-5.065 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />`;
            }
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    suggestions = []
    if request.method == "POST":
        password = request.form.get("password", "")
        result = check_password_strength(password)
        suggestions = result["suggestions"]
    return render_template_string(HTML, result=result, suggestions=suggestions)

if __name__ == "__main__":
    # For LAN access, use host="0.0.0.0" and consider HTTPS for public deployment
    app.run(debug=True)