# python-
import re
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime

def analyze_url(url):
    risk_score = 0
    findings = []

    print(f"\nAnalyzing: {url}\n")

    # 1️⃣ Check HTTPS
    if not url.startswith("https://"):
        risk_score += 2
        findings.append("⚠️ URL does not use HTTPS")

    # 2️⃣ Check for suspicious keywords
    suspicious_keywords = [
        "login", "verify", "secure", "account",
        "update", "bank", "confirm", "password"
    ]

    for keyword in suspicious_keywords:
        if keyword in url.lower():
            risk_score += 1
            findings.append(f"⚠️ Suspicious keyword found: {keyword}")

    # 3️⃣ Check for IP address in URL
    ip_pattern = r"https?://\d+\.\d+\.\d+\.\d+"
    if re.match(ip_pattern, url):
        risk_score += 3
        findings.append("🚨 URL uses an IP address instead of a domain")

    # 4️⃣ Check domain age
    try:
        domain = urlparse(url).netloc
        domain_info = whois.whois(domain)

        if domain_info.creation_date:
            if isinstance(domain_info.creation_date, list):
                creation_date = domain_info.creation_date[0]
            else:
                creation_date = domain_info.creation_date

            domain_age = (datetime.now() - creation_date).days

            if domain_age < 180:
                risk_score += 2
                findings.append("⚠️ Domain is less than 6 months old")

    except Exception:
        findings.append("⚠️ Could not retrieve WHOIS information")

    # 5️⃣ Final Risk Assessment
    print("Findings:")
    for finding in findings:
        print("-", finding)

    print("\nRisk Score:", risk_score)

    if risk_score >= 6:
        print("🚨 HIGH RISK - Likely Phishing")
    elif risk_score >= 3:
        print("⚠️ MEDIUM RISK - Suspicious")
    else:
        print("✅ LOW RISK - Likely Safe")


if __name__ == "__main__":
    user_url = input("Enter a URL to analyze: ")
    analyze_url(user_url)
