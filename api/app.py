from flask import Flask, render_template, request, session, send_file
import requests
import openpyxl
from io import BytesIO
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'

API_KEY = 'AIzaSyCLuH0kKI5lx9JIn5WvPihbbkar5aKZv8M'

def split_address(address):
    parts = address.split(',')
    address_part1 = parts[0].strip() if len(parts) > 0 else ''
    suburb_state_postcode = parts[1].strip() if len(parts) > 1 else ''

    import re
    matches = re.match(r'(.*)\s+([A-Z]{2,3})\s+(\d{4,5})', suburb_state_postcode)
    suburb = matches.group(1).strip() if matches else ''
    state = matches.group(2).strip() if matches else ''
    postcode = matches.group(3).strip() if matches else ''

    country = 'Australia'
    full_address = f"{address_part1}, {suburb} {state} {postcode}, {country}"

    return {
        'Address1': address_part1,
        'Address2': '',
        'Suburb': suburb,
        'State': state,
        'Postcode': postcode,
        'Country': country,
        'Full Address': full_address
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error_messages = []
    extracted_data = []

    if request.method == 'POST' and 'download_results_csv' not in request.form:
        if 'csv_file' in request.files:
            file = request.files['csv_file']
            wb = openpyxl.load_workbook(file)
            sheet = wb.active
            for row in sheet.iter_rows(values_only=True):
                if row[0] != 'Business Name':  # Skip header
                    extracted_data.append(row)

            try:
                for row in extracted_data:
                    if len(row) < 2:
                        error_messages.append("Skipping row: insufficient columns.")
                        continue

                    business_name = row[0].strip()
                    suburb = row[1].strip()

                    if not business_name or not suburb:
                        error_messages.append("Skipping row: empty business name or suburb.")
                        continue

                    search_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
                    response = requests.get(search_url, params={
                        'input': f"{business_name} {suburb}",
                        'inputtype': 'textquery',
                        'fields': 'place_id',
                        'key': API_KEY,
                    })
                    results_arr = response.json()

                    if 'candidates' not in results_arr or not results_arr['candidates']:
                        error_messages.append(f"No results found for {business_name} in {suburb}")
                        continue

                    place_id = results_arr['candidates'][0]['place_id']

                    details_url = 'https://maps.googleapis.com/maps/api/place/details/json'
                    response = requests.get(details_url, params={
                        'place_id': place_id,
                        'fields': 'formatted_address,name,formatted_phone_number',
                        'key': API_KEY,
                    })
                    details = response.json()

                    phone_number = details['result'].get('formatted_phone_number', 'N/A')
                    address = details['result'].get('formatted_address', 'N/A')
                    address_parts = split_address(address)

                    results.append({
                        'Business Name': business_name,
                        'Phone Number': phone_number,
                        'Full Address': address_parts['Full Address'],
                        'Address1': address_parts['Address1'],
                        'Address2': address_parts['Address2'],
                        'Suburb': address_parts['Suburb'],
                        'State': address_parts['State'],
                        'Postcode': address_parts['Postcode'],
                        'Country': address_parts['Country'],
                    })

                session['results'] = results

            except Exception as e:
                error_messages.append(f"General error: {str(e)}")

        else:
            error_messages.append("Please upload a valid CSV or Excel file.")

    if 'download_results_csv' in request.form:
        if 'results' in session:
            si = BytesIO()
            writer = csv.writer(si)
            writer.writerow(['Business Name', 'Phone Number', 'Full Address', 'Address1', 'Address2', 'Suburb', 'State', 'Postcode', 'Country'])
            for row in session['results']:
                writer.writerow([row['Business Name'], row['Phone Number'], row['Full Address'], row['Address1'], row['Address2'], row['Suburb'], row['State'], row['Postcode'], row['Country']])
            si.seek(0)
            return send_file(si, as_attachment=True, attachment_filename='business_details.csv', mimetype='text/csv')

    return render_template('index.html', extracted_data=extracted_data, results=results, error_messages=error_messages)

if __name__ == '__main__':
    app.run(debug=True)
