# FastAPI Email Validator API 🚀  

A API to validate email addresses by checking domain validity, MX records, blacklist status, and more.  

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


## 🛠️ Tech Stack

- 🚀 **FastAPI** → High-performance Python web framework  
- 📦 **Redis** → Used for caching & rate limiting  
- 📡 **WHOIS** → Fetches domain registration details  
- 📩 **dnspython** → Checks MX records for email validation  
- 📮 **SMTP** → Verifies email existence  
- 🐳 **Docker (Optional)** → For containerized deployment  

## 🔗 API Usage  
### **Check Email Validity**  
``` 
httpPOST/check_email?email=example@gmail.com
```


## ⚙️ Installation
```
git clone https://github.com/YOUR_GITHUB_USERNAME/fastapi-email-validator.git
cd fastapi-email-validator
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```


🚀 Start using the API today! 🚀
