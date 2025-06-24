
# 📄 Phishing Email Analysis Report

This file documents detailed observations of multiple phishing email samples as part of a cybersecurity internship task.

---

## 1️⃣ Sample: Monday.com Invitation

**Email Address Used:** support@shared-document.com  
**Legitimate Domain Should Be:** something like support@monday.com

### 🔍 Analysis:
- **Sender Spoofing:** The domain used is `shared-document.com`, which is not associated with Monday.com. This is a classic case of domain spoofing.
- **Urgency Element:** The email states “You were invited to join a Board,” encouraging the user to click quickly without verification.
- **Lack of Personalization:** Generic salutation and body with no direct mention of the recipient’s name or team.
- **Suspicious Link/Button:** “See the board now” button likely redirects to a malicious site imitating Monday.com.

### 🚩 Phishing Traits:
- Fake domain usage
- Call-to-action button leading to unknown URL
- Social engineering through collaboration context
- Missing sender verification

---

## 2️⃣ Sample: Office365 - High Severity Alert

**Email Address Used:** microsoft@email-records.com  
**Legitimate Domain Should Be:** something like @microsoft.com or @office365.com

### 🔍 Analysis:
- **Spoofed Domain:** The sender uses a misleading domain not associated with Microsoft.
- **Scare Tactics:** Subject and body warn of a “high-severity alert” to instill fear and prompt urgent action.
- **Technical Jargon:** Inclusion of message ID, severity level, and activity type is meant to appear authoritative.
- **Ambiguity:** “Sent by Unknown to Unknown” lacks legitimacy and clarity.

### 🚩 Phishing Traits:
- Scare-based social engineering
- Fake technical detail insertion
- URL obfuscation behind “View alert details” button
- Poor metadata handling

---

## 3️⃣ Sample: LastPass Alert

**Email Address Used:** LastPass@secure-monitor.com  
**Legitimate Domain Should Be:** @lastpass.com

### 🔍 Analysis:
- **Domain Impersonation:** `secure-monitor.com` is a deceptive domain.
- **Credential Phishing Attempt:** Prompts users to log into a fake site to “verify” if they were affected.
- **Social Engineering:** Claims of a data breach to provoke action.
- **Deceptive Hyperlink:** Anchor text “this secure web site” links to an unknown domain.

### 🚩 Phishing Traits:
- Pretending to be a trusted security provider
- Urgency to verify compromised data
- Clickbait button “Learn More”
- Spelling/grammar acceptable, but content logic suspicious

---

## 4️⃣ Sample: GoDaddy Email Verification

**Email Address Used:** godaddy@blogdodomains.co  
**Legitimate Domain Should Be:** @godaddy.com

### 🔍 Analysis:
- **Fake Domain:** The sender uses a domain resembling GoDaddy but is clearly unrelated.
- **Urgency and Consequence:** Threat of losing access to domain services if not verified.
- **Embedded Link:** “Verify Email Now” button likely leads to a fake login page.
- **Emotional Manipulation:** Warning tone to rush users into reacting.

### 🚩 Phishing Traits:
- Domain impersonation
- Urgent verification prompt
- Threat of service suspension
- Generic structure without real context

---

## 5️⃣ Sample: ExpressVPN Installation Alert

**Email Address Used:** support@update-wb.com  
**Legitimate Domain Should Be:** @expressvpn.com

### 🔍 Analysis:
- **Misleading Domain:** “update-wb.com” is not related to ExpressVPN.
- **Impersonation of IT Policy:** The email attempts to simulate a mandatory corporate security notice.
- **Grammatical Error:** “Please Advice” instead of “Please Advise.”
- **Malware Risk:** Button labeled “Install ExpressVPN Now” may initiate malicious download.

### 🚩 Phishing Traits:
- Fake update or installation prompt
- Corporate impersonation
- Poor grammar undermines credibility
- Dangerous file download risk

---

## ✅ Summary of Common Phishing Indicators:

- ✅ **Spoofed sender addresses**
- ✅ **Misleading or fake domains**
- ✅ **Urgent call-to-action or scare tactics**
- ✅ **Requests for sensitive information**
- ✅ **Vague or generic messages**
- ✅ **Dangerous links disguised as buttons**

---

⚠️ **Disclaimer:** This report is for educational and training purposes only. Do not interact with suspicious emails or click on unknown links.
