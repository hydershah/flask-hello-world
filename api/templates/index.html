<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Business Search</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            margin-top: 50px;
        }
        .card {
            padding: 20px;
            border-radius: 8px;
            border: none;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .result-box {
            width: 100%;
            height: 300px;
            margin-top: 15px;
        }
        .copy-btn {
            margin-top: 10px;
        }
        .btn-primary {
            background-color: #007bff;
            border-color: #007bff;
        }
        #pin-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            color: white;
            flex-direction: column;
        }
        #pin-overlay input {
            margin-top: 10px;
            margin-bottom: 10px;
            width: 200px;
            text-align: center;
        }
        #pin-overlay button {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div id="pin-overlay">
        <div class="text-center">
            <h1>Enter PIN</h1>
            <input type="password" id="pin" class="form-control" placeholder="Enter PIN">
            <button class="btn btn-primary" onclick="checkPin()">Submit</button>
        </div>
    </div>

    <div class="container">
        <div class="card">
            <h1 class="card-title">Business Search</h1>
            <form action="/" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="csv_file">Upload CSV/Excel File:</label>
                    <input type="file" id="csv_file" name="csv_file" class="form-control-file" required>
                </div>
                <button type="submit" class="btn btn-primary">Search</button>
            </form>

            {% if extracted_data %}
                <div class="mt-4">
                    <h3>Extracted Data</h3>
                    <ul>
                        {% for data_row in extracted_data %}
                            <li>{{ ', '.join(data_row) }}</li>
                        {% endfor %}
                    </ul>
                </div>
            {% endif %}

            {% if results %}
                <div class="mt-4">
                    <form action="/" method="post">
                        <textarea class="result-box form-control" id="resultBox" readonly>{% for row in results %}Business Name: {{ row['Business Name'] }}\nPhone Number: {{ row['Phone Number'] }}\nFull Address: {{ row['Full Address'] }}\nAddress1: {{ row['Address1'] }}\nAddress2: {{ row['Address2'] }}\nSuburb: {{ row['Suburb'] }}\nState: {{ row['State'] }}\nPostcode: {{ row['Postcode'] }}\nCountry: {{ row['Country'] }}\n\n{% endfor %}</textarea>
                        <button class="btn btn-secondary copy-btn" type="button" onclick="copyToClipboard()">Copy</button>
                        <button class="btn btn-secondary" name="download_results_csv" type="submit">Download CSV</button>
                    </form>
                </div>
            {% endif %}

            {% if error_messages %}
                <div class="alert alert-danger mt-4">
                    <ul>
                        {% for error_message in error_messages %}
                            <li>{{ error_message }}</li>
                        {% endfor %}
                    </ul>
                </div>
            {% endif %}
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

    <script>
        const correctPin = "995";

        function checkPin() {
            const enteredPin = document.getElementById("pin").value;
            if (enteredPin === correctPin) {
                document.getElementById("pin-overlay").style.display = "none";
                localStorage.setItem('pinVerified', 'true');
            } else {
                alert("Incorrect PIN. Please try again.");
            }
        }

        function copyToClipboard() {
            var copyText = document.getElementById("resultBox");
            copyText.select();
            document.execCommand("copy");
            alert("Copied the text: " + copyText.value);
        }

        if (localStorage.getItem('pinVerified') === 'true') {
            document.getElementById("pin-overlay").style.display = "none";
        } else {
            document.getElementById("pin-overlay").style.display = "flex";
        }

        window.addEventListener('beforeunload', function() {
            localStorage.removeItem('pinVerified');
        });
    </script>
</body>
</html>
