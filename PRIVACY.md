# Privacy Policy

**Effective Date:** January 1, 2026  
**Last Updated:** July 15, 2026  
**Organization:** Vane Enterprise LLC / Vane-Guard Sovereign Systems  
**Contact:** privacy@taruglobalaccess.com (via mdabulhossain1008@gmail.com)

---

## 1. Overview

Vane-Guard Sovereign Orchestrator (hereinafter "the Application" or "App") is a GitHub integration application designed to provide deterministic Large Language Model (LLM) orchestration, hallucination mitigation, and repository-level AI governance.

This Privacy Policy describes how the Application processes, stores, and protects data in compliance with international data protection regulations, including GDPR (General Data Protection Regulation), CCPA (California Consumer Privacy Act), and SOC 2 Type II standards.

**Core Principle:** All data processed by Vane-Guard Sovereign Orchestrator remains localized within your GitHub repository infrastructure. **No data is transmitted externally, and no telemetry is collected.**

---

## 2. Data Processing Architecture

### 2.1 Data Locality & Isolation

- **Repository-Bound Processing:** All LLM processing, context anchoring, and hallucination detection operations execute within the scope of your GitHub repository.
- **Zero External Transmission:** No repository content, commit history, pull request data, or issue metadata is transmitted to external servers or third-party APIs.
- **Encrypted in Transit:** All interactions between the GitHub App and GitHub API are encrypted via TLS 1.3.

### 2.2 Supported GitHub Objects Processed

The Application may access and process the following GitHub entities **only for the purposes of LLM context anchoring and hallucination detection:**

| Object Type | Purpose | Data Retained |
|-------------|---------|---------------|
| Pull Requests | Code review context, diff analysis, commit messages | Ephemeral (session-only) |
| Issues | Context extraction, discussion analysis | Ephemeral (session-only) |
| Commits | Commit message validation, change context | Ephemeral (session-only) |
| Repository Content | Semantic understanding, code structure analysis | Ephemeral (session-only) |
| GitHub Actions Logs | Workflow context, deployment validation | Ephemeral (session-only) |

**Ephemeral Processing:** All data is processed in-memory and discarded immediately after the orchestration cycle completes. **No persistent logs are created.**

---

## 3. What Data We Collect

### 3.1 Application Usage Data

**We DO NOT collect:**
- ❌ Repository contents or file contents
- ❌ Pull request diffs or code changes
- ❌ Commit messages or authorship metadata
- ❌ Issue descriptions or discussion content
- ❌ User identities or GitHub usernames
- ❌ Repository names or organizational structure
- ❌ Usage frequency, API call counts, or telemetry
- ❌ IP addresses or device identifiers
- ❌ Session cookies or tracking identifiers

### 3.2 GitHub App Permission Scope

The Application requests only the **minimum permissions** necessary to function:

| Permission | Scope | Justification |
|-----------|-------|---------------|
| `contents:read` | Repository source code | Required to analyze code context for LLM anchoring |
| `pull_requests:read` | Pull request metadata | Required for code review orchestration |
| `issues:read` | Issue discussions | Required for context extraction during AI processing |
| `checks:write` | CI/CD integration | Required to report hallucination detection results |
| `actions:read` | Workflow data | Required to access workflow context (optional) |

**No sensitive permissions are requested.** The Application does **not** request:
- `contents:write` (no code modification)
- `secrets` access (no credential exposure)
- `admin` scope (no repository configuration changes)

---

## 4. Data Retention & Deletion

### 4.1 Retention Policy

- **Session Data:** All in-memory processing data is discarded at session end.
- **Application Logs:** No persistent logs are maintained on Vane-Guard infrastructure.
- **GitHub Integration:** No data is stored in GitHub App storage or cache.

### 4.2 User Data Deletion

You have the right to request complete deletion of any metadata:
- Delete the GitHub App from your repository at any time (GitHub > Settings > Integrations).
- Deletion removes all App access to future repository events.
- Existing usage data is already ephemeral and requires no additional cleanup.

---

## 5. GDPR Compliance

### 5.1 Legal Basis for Processing

Processing is based on:
- **Legitimate Interest:** Enabling repository owners to maintain code quality and prevent AI-driven errors.
- **Contractual Necessity:** Required to provide the GitHub App functionality.

### 5.2 Data Subject Rights (GDPR Articles 15-22)

As a Data Subject under GDPR, you have the right to:

| Right | How to Exercise |
|------|---------------|
| **Access (Art. 15)** | Request all data we hold about you via DPO contact below |
| **Rectification (Art. 16)** | Correct inaccurate information in your GitHub profile |
| **Erasure (Art. 17)** | Request deletion by uninstalling the App and contacting us |
| **Restriction (Art. 18)** | Request we stop processing by removing the App |
| **Portability (Art. 20)** | Request a copy of data in portable format |
| **Objection (Art. 21)** | Opt-out of processing by uninstalling the App |

### 5.3 Data Processing Agreement

Organizations processing EU resident data should request a Data Processing Addendum (DPA) from our security team (see Section 7 below).

---

## 6. CCPA Compliance (California Residents)

Under the California Consumer Privacy Act, California residents have the right to:

- **Know:** What personal information is collected
- **Delete:** Request deletion of personal information (via uninstalling the App)
- **Opt-Out:** Disable the App at any time
- **Non-Discrimination:** No price/service discrimination for exercising CCPA rights

**Vane-Guard does not:**
- Sell personal information
- Share personal information with unaffiliated third parties
- Create detailed profiles or cross-device tracking

---

## 7. Security & SOC 2 Compliance

### 7.1 Security Controls

- **Encryption in Transit:** TLS 1.3 for all API communications
- **Zero External Storage:** No persistent data storage outside your repository
- **Code Execution:** Processing occurs in isolated, ephemeral containers
- **Access Control:** GitHub authentication via OAuth 2.0; no stored credentials

### 7.2 SOC 2 Type II

Vane-Guard Sovereign Orchestrator operates under the following security principles:

| SOC 2 Pillar | Control |
|-------------|----------|
| **CC6.1 (Logical Security)** | OAuth 2.0 authentication; no credential storage |
| **CC7.2 (System Monitoring)** | Activity logging for security events only |
| **CC9.2 (Data Backup)** | No data retention; no backup required |
| **A1.2 (Availability)** | GitHub API SLA; no App-level availability guarantees |

---

## 8. Third-Party Integrations

### 8.1 GitHub API

- **Provider:** GitHub Inc.
- **Data Processed:** Repository metadata, pull requests, issues
- **Privacy:** Governed by [GitHub Privacy Policy](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)

### 8.2 No Other Third Parties

The Application **does not integrate with** external services, analytics platforms, or LLM providers not explicitly configured by you.

**Exception:** If you configure the App to use external LLM APIs (e.g., OpenAI, Google Gemini), please review those providers' privacy policies separately.

---

## 9. Cookies & Tracking

- ❌ **No Cookies:** The Application does not set browser cookies.
- ❌ **No Tracking Pixels:** No analytics or tracking pixels are used.
- ❌ **No Third-Party Scripts:** No external JavaScript libraries for analytics.

---

## 10. Changes to This Privacy Policy

Vane-Guard may update this policy to reflect legal, regulatory, or operational changes. Changes will be posted to this repository with an updated "Last Updated" date.

**Material changes** (affecting data rights or processing practices) will be communicated via:
- GitHub repository commit notifications
- Email to organization administrators (if applicable)

---

## 11. Contact & Security Reporting

### 11.1 Privacy Inquiries

For questions about this policy or data processing practices:

- **Email:** mdabulhossain1008@gmail.com
- **GitHub Issues:** [Open a privacy-related issue](https://github.com/Vane-Enterprise/vane-enterprise.github.io/issues)
- **Organization:** Vane Enterprise LLC
- **Primary Domain Contact:** mdah@taruglobalaccess.com

### 11.2 Security Vulnerability Reporting

**Do NOT open public issues for security vulnerabilities.**

For responsible disclosure:

- **Email:** myou260312@gmail.com
- **GPG Key:** Available upon request
- **Response SLA:** 48 hours for initial acknowledgment; 30 days for resolution target

### 11.3 Data Protection Officer (DPO)

For GDPR-related inquiries, contact our Data Protection Officer:

- **Email:** mdabulhossain1008@gmail.com
- **Response SLA:** 5 business days

---

## 12. Compliance Certifications

- ✅ **GDPR Compliant:** Minimal data collection, user rights enforced
- ✅ **CCPA Compliant:** California resident rights supported
- ✅ **SOC 2 Type II Ready:** Security controls aligned with SOC 2 standards
- ✅ **ISO 27001 Aligned:** Information security practices follow ISO standards

---

## 13. Summary of Your Data Rights

| Scenario | Your Control |
|----------|-------------|
| **Disable the App** | GitHub Settings > Integrations > Remove App |
| **Request Data Export** | Contact mdabulhossain1008@gmail.com |
| **Report a Violation** | Contact myou260312@gmail.com |
| **Delete Your Data** | Uninstall the App (all data is already ephemeral) |
| **Exercise GDPR Rights** | Email mdabulhossain1008@gmail.com |

---

**Version:** 1.0  
**Last Updated:** July 15, 2026  
**Organization:** Vane Enterprise LLC

By using the Vane-Guard Sovereign Orchestrator, you acknowledge that you have read and understood this Privacy Policy.
