from flask import Flask, request
import os

app = Flask(__name__)

# HTML templates as Python strings
form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule News App Launch</title>
    <style>
        :root {
            --primary-color: #673AB7;
            --secondary-color: #9575CD;
            --accent-color: #FF5722;
            --background: #f5f0ff;
            --card-bg: #ffffff;
            --text-color: #333333;
            --shadow: 0 4px 6px rgba(0,0,0,0.1);
            --transition: all 0.3s ease;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--background);
            color: var(--text-color);
            line-height: 1.6;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        .container {
            width: 90%;
            max-width: 600px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(103, 58, 183, 0.2);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        h2 {
            margin: 0;
            font-size: 1.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .content {
            padding: 30px;
        }
        
        form {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        
        label {
            font-weight: bold;
            font-size: 1.1rem;
            margin-bottom: 5px;
            display: block;
        }
        
        input[type="time"] {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1rem;
            transition: var(--transition);
        }
        
        input[type="time"]:focus {
            border-color: var(--primary-color);
            outline: none;
            box-shadow: 0 0 0 3px rgba(103, 58, 183, 0.2);
        }
        
        button[type="submit"] {
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: var(--transition);
        }
        
        button[type="submit"]:hover {
            background: #E64A19;
            transform: translateY(-2px);
        }
        
        button[type="submit"]:active {
            transform: translateY(0);
        }
        
        .footer {
            text-align: center;
            padding: 15px;
            font-size: 0.9rem;
            color: #666;
            border-top: 1px solid #eee;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h2>📅 Schedule News App Launch</h2>
        </header>
        <div class="content">
            <form action="/schedule" method="post">
                <div>
                    <label for="time">Enter Time (HH:MM):</label>
                    <input type="time" name="time" id="time" required>
                </div>
                <button type="submit">Schedule Launch</button>
            </form>
        </div>
        <div class="footer">
            Schedule your news application to launch automatically at your preferred time.
        </div>
    </div>
</body>
</html>
'''  # (Keep your existing HTML here – unchanged)

confirmation_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scheduled</title>
    <style>
        :root {
            --primary-color: #673AB7;
            --secondary-color: #9575CD;
            --accent-color: #FF5722;
            --background: #f5f0ff;
            --success-color: #4CAF50;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--background);
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        .container {
            width: 90%;
            max-width: 600px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.2);
            overflow: hidden;
        }
        
        .success-header {
            background: linear-gradient(135deg, var(--success-color), #81C784);
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        h2 {
            margin: 0;
            font-size: 1.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .content {
            padding: 30px;
            text-align: center;
        }
        
        .time-display {
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary-color);
            margin: 20px 0;
        }
        
        .message {
            margin-bottom: 25px;
            font-size: 1.1rem;
        }
        
        .countdown {
            font-size: 1.5em;
            color: var(--accent-color);
            margin: 20px 0;
        }
        
        .home-button {
            display: inline-block;
            background: var(--accent-color);
            color: white;
            text-decoration: none;
            padding: 12px 25px;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
            margin-top: 20px;
        }
        
        .home-button:hover {
            background: #E64A19;
            transform: translateY(-2px);
        }
        
        .note {
            font-size: 0.9em;
            color: #666;
            margin-top: 20px;
        }
        
        a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: bold;
        }
        
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="success-header">
            <h2>✅Your News Website HasBeen Scheduled!</h2>
        </div>
        <div class="content">
            <div class="message">
                Your News Application will launch at:
            </div>
            <div class="time-display">
                {{ time }}
            </div>
            <div class="countdown">
                ⏳ Redirecting in <span id="timer">calculating...</span>
            </div>
            <div class="note">
                If not redirected automatically, <a href="http://13.126.87.128:8080/news">click here</a>.
            </div>
            <a href="/" class="home-button">Schedule Again</a>
        </div>
    </div>
    
    <script>
        window.onload = function () {
            // Get the target time from the server (e.g. "13:45")
            let targetTime = "{{ time }}";
            
            // Parse the current time
            let now = new Date();
            
            // Parse the target time
            let [hour, minute] = targetTime.split(":").map(Number);
            let scheduled = new Date();
            scheduled.setHours(hour);
            scheduled.setMinutes(minute);
            scheduled.setSeconds(0);
            
            // If the scheduled time is already past, assume next day
            if (scheduled < now) {
                scheduled.setDate(scheduled.getDate() + 1);
            }
            
            // Get the countdown display element
            let countdownElement = document.getElementById("timer");
            
            // Function to update the countdown
            function updateCountdown() {
                let now = new Date();
                let remaining = scheduled - now;
                
                if (remaining <= 0) {
                    // Time's up! Redirect to the news app
                    window.location.href = "http://13.126.87.128:8080/news";
                } else {
                    // Calculate remaining time
                    let seconds = Math.floor((remaining / 1000) % 60);
                    let minutes = Math.floor((remaining / (1000 * 60)) % 60);
                    let hours = Math.floor((remaining / (1000 * 60 * 60)) % 24);
                    
                    // Format display with leading zeros
                    let displayHours = hours.toString().padStart(2, '0');
                    let displayMinutes = minutes.toString().padStart(2, '0');
                    let displaySeconds = seconds.toString().padStart(2, '0');
                    
                    // Update countdown display
                    countdownElement.innerText = `${displayHours}h ${displayMinutes}m ${displaySeconds}s`;
                    
                    // Schedule next update
                    setTimeout(updateCountdown, 1000);
                }
            }
            
            // Start the countdown
            updateCountdown();
        };
    </script>
</body>
</html>
'''  # (Keep your existing confirmation HTML here – unchanged)

# Custom template rendering function
def render_template(template, **context):
    result = template
    for key, value in context.items():
        placeholder = f"{{{{ {key} }}}}"
        result = result.replace(placeholder, str(value))
    return result

@app.route('/')
def index():
    return form_html

@app.route('/schedule', methods=['POST'])
def schedule():
    time = request.form['time']  # Expected format: HH:MM

    # 🕒 Schedule the 'start-container.sh' to run at the given time using `at`
    
     # Expected format: HH:MM

    # 🕒 Schedule the 'start-container.sh' to run at the given time using `at`
    
    os.system(f'echo "/home/ubuntu/start-container.sh >> /tmp/debug.log 2>&1" | at {time}')

    # ✅ Confirmation screen with countdown
    
    # ✅ Confirmation screen with countdown
    return render_template(confirmation_html, time=time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
