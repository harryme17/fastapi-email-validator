import whois
import dns.resolver
import redis
from datetime import datetime
from validate_email_address import validate_email

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

async def check_email_validity(email: str):
    """Validate email and check domain information."""
    
    # Check if cached result exists
    if redis_client.exists(email):
        return eval(redis_client.get(email))
    
    try:
        domain = email.split("@")[-1]

        # WHOIS lookup
        domain_info = whois.whois(domain)
        registration_date = domain_info.creation_date
        expiry_date = domain_info.expiration_date

        # Calculate domain age
        if isinstance(registration_date, list):
            registration_date = registration_date[0]  # Handle multiple entries
        domain_age = (datetime.now() - registration_date).days if registration_date else None
        
        # Check MX records
        try:
            dns.resolver.resolve(domain, "MX")
            mx_valid = True
        except:
            mx_valid = False
        
        # Check if the email is disposable
        disposable_domains = ["tempmail.com", "10minutemail.com", "mailinator.com"]
        is_disposable = domain in disposable_domains

        # Blacklist check (mocked)
        blacklist = ["baddomain.com", "spam.com"]
        is_blacklisted = domain in blacklist

        # Validate full email via SMTP (mocked, implement if needed)
        smtp_valid = validate_email(email, verify=True)

        # Response
        response = {
            "email": email,
            "valid_syntax": validate_email(email),
            "mx_valid": mx_valid,
            "smtp_valid": smtp_valid,
            "disposable": is_disposable,
            "blacklisted": is_blacklisted,
            "registration_date": str(registration_date),
            "domain_age_days": domain_age,
            "expiry_date": str(expiry_date)
        }

        # Cache the result in Redis
        redis_client.set(email, str(response), ex=86400)  # Cache for 1 day
        
        return response

    except Exception as e:
        return {"error": "WHOIS lookup failed", "details": str(e)}
