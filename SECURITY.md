# *Security Policy*
## *Section I: Overview*
***1.1.*** *Vulnerabilities account for the largest portion of attack vectors outside of malware. It is crucial that any software be assessed for vulnerabilities and any vulnerabilities be remediated prior to production deployment.*

## *Section II: About coordinated disclosure of security vulnerabilities*
***2.1.*** *Vulnerability disclosure is an area where collaboration between vulnerability reporters, such as security researchers, and project maintainers is particularly important. Both parties need to work together from the moment a potentially harmful security vulnerability is found, right until a vulnerability is disclosed to the world, ideally with a patch available. Typically, when someone lets a maintainer know privately about a security vulnerability, the maintainer develops a fix, validates it, and notifies the users of the project or package. The initial report of a vulnerability is made privately, and the full details are only published once the maintainer has acknowledged the issue, and ideally made remediation's or a patch available, sometimes with a delay to allow more time for the patches to be installed.*

## *2.1. Best practices for vulnerability reporters*
*2.1.1.* *It is good practice to report vulnerabilities privately to maintainers; in our case, through [pedromiguelfilipesimoes@pm.me](mailto:pedromiguelfilipesimoes@pm.me). When possible, as a vulnerability reporter, we recommend you avoid disclosing the vulnerability publicly without giving maintainers a chance to remediate; bypassing the maintainers; disclosing the vulnerability before a fixed version of the code is available; expecting to be compensated for reporting an issue, where no public bounty program exists.*

*2.1.2.* *It is acceptable for vulnerability reporters to disclose a vulnerability publicly after a period if they have tried to contact the maintainers and not received a response or contacted them and been asked to wait too long to disclose it.*

*2.1.3.* *We recommend vulnerability reporters clearly state the terms of their disclosure policy as part of their reporting process. Even if the vulnerability reporter does not adhere to a strict policy, it is a clever idea to set clear expectations for maintainers in terms of timelines on intended vulnerability disclosures.*

## *2.2. Best practices for maintainers*
*2.2.1.* *As a maintainer, it is good practice to clearly indicate how and where you want to receive reports for vulnerabilities. If this information is not clearly available, vulnerability reporters do not know how to contact you, and may resort to extracting developer email addresses from git commit histories to try to find an appropriate security contact. This can lead to friction, lost reports, or the publication of unresolved reports. Maintainers should disclose vulnerabilities in a timely manner. If there is a security vulnerability in your repository, we recommend you:*

*2.2.1.1.* *Treat the vulnerability as a security issue rather than a simple bug, both in your response and your disclosure. For example, you will need to explicitly mention that the issue is a security vulnerability in the release notes.*

*2.2.1.2.* *Acknowledge receipt of the vulnerability report as quickly as possible, even if no immediate resources are available for investigation. This sends the message that you are quick to respond and act, and it sets a positive tone for the rest of the interaction between you and the vulnerability reporter.*

*2.2.1.3.* *Involve the vulnerability reporter when you verify the impact and veracity of the report. It is likely the vulnerability reporter has already spent time considering the vulnerability in a variety of scenarios, some of which you may have not considered yourself.*

*2.2.1.4.* *Remediate the issue in a way that you see fit, taking any concerns and advice provided by the vulnerability reporter into careful consideration. Often the vulnerability reporter will have knowledge of certain corner cases and remediation bypasses that are easy to miss without a security research background.*

*2.2.1.5.* *Always acknowledge the vulnerability reporter when you credit the discovery.*

*2.2.1.6.* *Aim to publish a fix as soon as you can.*

*2.2.1.7.* *Ensure that you make the wider ecosystem aware of the issue and its remediation when you disclose the vulnerability. It is common to see cases where a recognized security issue is fixed in the current development branch of a project, but the commit or subsequent release is not explicitly marked as a security fix or release. This can cause problems with downstream consumers.*

## *Section III: Purpose*
***3.1.*** *The purpose of this policy is to define software security assessments within. Software assessments are performed to identify potential or realized weaknesses because of inadvertent misconfiguration, weak authentication, insufficient error handling, sensitive information leakage, etc. Discovery and subsequent mitigation of these issue will limit the attack surface of services available both internally and externally as well as satisfy compliance with any relevant policies in place.*