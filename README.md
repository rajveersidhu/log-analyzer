# **🔍 Log Analyzer for Suspicious Activity**  
🚀 **A Python-based tool that detects suspicious login attempts and unauthorized access from system logs.**  

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)  
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)  

---

## **📌 Features**
✅ Parses **SSH, Apache/Nginx, and system logs** to detect:  
- **Brute force attacks** (multiple failed login attempts)  
- **Unauthorized access attempts**  
- **Suspicious IP addresses**  

✅ Sends alerts via **Email/Slack** for real-time monitoring  
✅ (Optional) **Checks IPs** against **AbuseIPDB** threat database  
✅ (Optional) Stores logs in **Elasticsearch** for visualization in **Kibana**  
✅ (Optional) Web UI for displaying suspicious activity  

---

## **🛠️ Installation**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/rajveersidhu/log-analyzer.git
cd log-analyzer
```

### **2️⃣ Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## **🚀 Usage**
### **🔍 Run the Log Parser**
```bash
python parser.py
```
This will scan logs and output suspicious activity.

### **📨 Send Alerts**
```bash
python alerts.py
```
Make sure to **update your email credentials** in `alerts.py` before running.

### **🌍 (Optional) Run the Web UI**
```bash
python app.py
```
Then open **`http://127.0.0.1:5000`** in your browser.

---

## **⚙️ Configuration**
Modify these variables in `config.py` to suit your needs:

```python
LOG_FILE = "/var/log/auth.log"  # Change to your log file path
EMAIL_ALERTS = True  # Set to False to disable email alerts
```

---

## **📊 Example Output**
```
🚨 Suspicious Login Attempt - User: root, IP: 192.168.1.105
🚨 Brute Force Detected - Multiple Failed Logins from 203.0.113.42
```

---

## **📦 Dependencies**
- Python 3.8+
- Pandas
- Flask (for Web UI)
- Requests (for API calls)
- Elasticsearch (optional)

To install them:
```bash
pip install -r requirements.txt
```

---

## **🛡️ Security Considerations**
- Ensure sensitive credentials (email passwords, API keys) are **stored in environment variables**.
- Regularly update the **threat database** to keep detection accurate.
- Consider adding **rate limiting** to prevent abuse.

---

## **📸 Screenshots (Optional)**
📌 **CLI Output**  
![CLI Output](https://user-images.githubusercontent.com/yourimage.png)

📌 **Web UI Example**  
![Web UI](https://user-images.githubusercontent.com/yourimage2.png)

---

## **🛠️ Contributing**
Contributions are welcome!  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature-new`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to your branch (`git push origin feature-new`)  
5. Create a **Pull Request**  

---

## **📜 License**
This project is licensed under the **MIT License** – see the [`LICENSE`](LICENSE) file for details.

---

## **💡 Future Improvements**
📌 Add **GeoIP location tracking** for attack sources  
📌 Integrate with **fail2ban** for automatic blocking  
📌 Build a **machine learning model** for anomaly detection  
