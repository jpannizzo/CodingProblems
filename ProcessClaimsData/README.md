You are provided with a list of healthcare claim records in JSON format. Each record contains the following fields:

Site Title

claim_id (string)

patient_id (string)

provider_id (string)

claim_amount (float)

claim_date (string in 'YYYY-MM-DD' format)

status (string: 'approved', 'denied', or 'pending')

Your task is to write a Python function that processes this list and returns a summary report as a dictionary with the following information:

Total number of claims

Total approved claim amount

Number of unique patients

Number of claims per status

Average claim amount per provider
