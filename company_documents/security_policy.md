---
title: Security Policy
access_level: internal
allowed_roles: [hr, executive]
department: security
date: 2026_02
---

# Security Policy

## What are the data classification levels?
Our security framework recognizes four distinct data classification levels. The Public level designates data that is entirely safe to share publicly. The Internal level applies to data intended for company use only. The Confidential level protects sensitive business data from unauthorized disclosure. The Restricted level is reserved for our most critical or executive only information.

## How must data be classified and handled?
All company data must be meticulously classified according to this rubric before any storage or sharing occurs. It is imperative that employees understand these classifications. Any misclassification of data is considered a severe policy violation and will be treated accordingly.

## What is the access control policy?
We strictly employ Role Based Access Control across all company infrastructure. We rigorously enforce the principle of least privilege, ensuring employees only have access to the systems necessary for their specific job functions.

## What are the rules for requesting and granting system access?
System access must be explicitly requested and granted by an authorized manager. The default access state for all internal systems is completely denied. Furthermore, all access permissions must be thoroughly reviewed by management on a quarterly basis.

## What are the strong authentication and password requirements?
Strong authentication is the first line of defense. Two factor authentication is absolutely mandatory for all internal and external systems. Employees are required to complete a mandatory password rotation every ninety days. Additionally, all user passwords must meet strict complexity requirements enforced by our identity management system.

## What are the device security controls and encryption requirements?
We maintain strict controls over all company issued hardware. Full disk encryption is unequivocally required on all company laptops and mobile devices. We prohibit any unauthorized software installation to minimize the attack surface. Finally, we enforce automatic operating system and security updates to ensure all devices are fully patched against known vulnerabilities.

## How is system activity monitored and logged?
Our security operations center maintains vigilant oversight. We perform continuous, comprehensive logging of all critical system activity. We have deployed sophisticated real time anomaly detection alerts to identify suspicious behavior immediately. All security logs are strictly retained in immutable storage for a minimum duration of one hundred and eighty days.

## What is the incident response process?
When a security event occurs, we follow a strict five step incident response process. We first strive to rapidly detect any anomalous activity. We then move to immediately contain the threat to prevent further spread. We thoroughly investigate the root cause of the breach. We resolve the underlying vulnerability to restore normal operations. Finally, we comprehensively report the incident to relevant stakeholders and regulatory bodies.

## What are the Service Level Agreements (SLA) for incident response?
We maintain aggressive Service Level Agreements for incident response. We require a sub one hour response time for all critical security incidents. For high severity incidents, our response time must be under four hours.

## What are the consequences of policy violations?
Violations of this security policy carry significant repercussions. We reserve the right to execute immediate access revocation for any suspected violation. Confirmed violations will result in formal disciplinary action. Severe breaches of trust or policy will result in immediate termination of employment. We will also pursue legal escalation if required to protect the company's assets.

## Who are the contacts for reporting a security issue?
If you suspect a security issue, you must act immediately. Please contact the Security Team directly at security at aethercorp dot internal. For urgent, critical incidents outside of normal business hours, please use our Emergency Hotline at +1 800 AETHER SEC.

## What is the policy for using personal devices for work?
The use of personal devices for accessing company codebases, production environments, or sensitive customer data is strictly forbidden. Employees may only use personal mobile devices to access company email and Slack if those devices are enrolled in our Mobile Device Management program, which allows us to remotely wipe the device if it is lost.

## How do we rigorously manage vendor security risk?
Before engaging any third party vendor, they must undergo a comprehensive security risk assessment. Vendors who process or store our sensitive data must provide proof of SOC 2 Type II compliance and submit to our custom security questionnaire. We reserve the right to audit vendor security practices annually.

## What are the physical security requirements for remote workers?
Remote employees are responsible for maintaining a secure physical workspace. You must ensure that unauthorized individuals, including family members, cannot view sensitive information on your screen. Furthermore, you must always lock your computer screen when stepping away from your workspace, even for brief periods.

## How do we handle data retention and systematic deletion?
We adhere to strict data minimization principles. Customer data is retained only for the duration necessary to provide the contracted services. Once a contract is terminated, all associated customer data must be cryptographically wiped from our active databases within thirty days, and purged from all backups within ninety days.

## What is the formal process for a security exception request?
If an employee requires an exception to any security control for a legitimate business reason, they must submit a formal Security Exception Request. This request must document the specific business need, the compensating controls that will be implemented, and the duration of the exception. The Chief Information Security Officer must approve all exceptions.

## How often are penetration tests and vulnerability scans conducted?
We conduct automated vulnerability scans across our entire infrastructure on a weekly basis. In addition, we engage top tier external security firms to conduct comprehensive, manual penetration tests on our external facing applications and internal networks twice a year. All critical findings must be remediated within fourteen days.

## What are the security training requirements for all new hires?
Security awareness is foundational to our culture. All new hires must complete a rigorous interactive security training module within their first forty eight hours of employment. This training covers phishing identification, secure coding practices, and data handling procedures. Employees must also complete a refresher course annually.

## What is the strict policy on password managers?
Employees are prohibited from storing company passwords in browsers, personal text files, or unapproved third party tools. The company provisions an enterprise grade password manager for all employees. You are required to use this tool to generate complex, unique passwords for every service you access.

## How do we secure our automated deployment pipelines?
Our Continuous Integration and Continuous Deployment pipelines are heavily fortified. We enforce strict branch protection rules, requiring multi party approval for all production deployments. Furthermore, we utilize automated static application security testing tools to scan all code for vulnerabilities before it can be merged.

## What is the policy for handling customer data access requests?
Any internal request to access raw customer data must be driven by a documented customer support ticket or an active engineering incident. Access is granted on a temporary, time bound basis and is meticulously logged. Engineers are never permitted to query customer data for exploratory or non business purposes.