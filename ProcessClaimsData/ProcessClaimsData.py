claims_list = [
    {
        "claim_id": "C001",
        "patient_id": "P001",
        "provider_id": "PR001",
        "claim_amount": 250.0,
        "claim_date": "2025-05-01",
        "status": "approved"
    },
    {
        "claim_id": "C002",
        "patient_id": "P002",
        "provider_id": "PR002",
        "claim_amount": 150.0,
        "claim_date": "2025-05-02",
        "status": "denied"
    },
    {
        "claim_id": "C003",
        "patient_id": "P001",
        "provider_id": "PR001",
        "claim_amount": 300.0,
        "claim_date": "2025-05-03",
        "status": "approved"
    }
]


def process (claims_list):
    total_claims = 0
    # total unique patients
    approved_amount = 0
    patient_list = []
    provider_list = []
    claim_per_provider = {}
    
    claims_per_status = {
        "approved" : 0,
        "denied" : 0,
        "pending" : 0
    }
    
    for claim in claims_list:
        total_claims += 1
        if claim["status"] == "approved":
            claims_per_status["approved"] +=1
            approved_amount += claim["claim_amount"]
        elif claim["status"] == "denied":
            claims_per_status["denied"] +=1
        else:
            claims_per_status["pending"] +=1
        
        if claim["patient_id"] not in patient_list:
            patient_list.append(claim["patient_id"])

        # need to claims per provider
        if claim["provider_id"] in claim_per_provider:
            claim_per_provider[claim["provider_id"]] = {
                "total_claim_amount": claim_per_provider[claim["provider_id"]]["total_claim_amount"] + claim["claim_amount"],
                "number_of_claims" : claim_per_provider[claim["provider_id"]]["number_of_claims"] + 1
            }
        else:
            claim_per_provider[claim["provider_id"]] = {
                "total_claim_amount": claim["claim_amount"],
                "number_of_claims" : 1
            }

        if claim["provider_id"] not in provider_list:
            provider_list.append(claim["provider_id"])
    
    return_map = {
        "total_claims" : total_claims,
        "total_approved_amount": approved_amount,
        "unique_patients": len(patient_list),
        "claims_per_status": claims_per_status,
        "average_claim_per_provider": {}
    }

    for provider in provider_list:
        return_map["average_claim_per_provider"][provider] = claim_per_provider[provider]["total_claim_amount"] / claim_per_provider[provider]["number_of_claims"]

    return return_map


print(process(claims_list))