# 🚀 FastAPI Email Validator API  

A high-performance API to validate email addresses by checking domain validity, MX records, blacklist status, and more.  

## ✅ Features  
- Domain Expiry & Age Calculation  
- MX Record Validation  
- Disposable Email Detection  
- Blacklist Status Check  
- Full SMTP Email Validation  
- API Rate Limiting with Redis  

## 📡 How It Works  
1️⃣ Accepts an email address  
2️⃣ Extracts domain details & checks WHOIS  
3️⃣ Validates MX records & SMTP  
4️⃣ Checks for disposable & blacklisted domains  
5️⃣ Returns JSON response with results  

## 🔗 API Usage  
### **Check Email Validity**  
```http POST /check_email?email=example@gmail.com```

## ⚙️ Installation
`{
  "email": "example@gmail.com",
  "valid_syntax": true,
  "mx_valid": true,
  "smtp_valid": true,
  "disposable": false,
  "blacklisted": false,
  "registration_date": "2010-08-15",
  "domain_age_days": 5000,
  "expiry_date": "2030-08-15"
}`

## 🛠️ Tech Stack
🚀 FastAPI → High-performance Python web framework

📦 Redis → Used for caching & rate limiting

📡 WHOIS → Fetches domain registration details

📩 dnspython → Checks MX records for email validation

📮 SMTP → Verifies email existence

🐳 Docker (Optional) → For containerized deployment


