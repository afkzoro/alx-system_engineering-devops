# 0x19-postmortem
Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

#  Summary
On February 28, 2023, our company's application server experienced a significant outage that lasted for approximately 3 hours, resulting in a complete service disruption for our customers. The issue was caused by a hardware failure in one of the server's components.

# Timeline
* 8:00 AM: The first report of an issue is received from our monitoring system, indicating that the server is experiencing high CPU utilization.

* 8:10 AM: The support team begins to investigate the issue and finds that the server is not responding to requests. The team begins to escalate the issue to the IT team.

* 8:30 AM: The IT team receives the first alert regarding the issue and begins investigating.

* 9:00 AM: The IT team identifies the root cause of the issue, which is a hardware failure in one of the server's components. The team begins to work on a fix.

* 10:30 AM: The IT team replaces the failed hardware component and begins to test the server.

* 11:30 AM: The IT team verifies that the server is fully operational and begins to restore services.

* 11:45 AM: The server is fully restored, and all services are operational once again.

# Root cause
The root cause of the outage was a **hardware failure** in one of the server's components. The server's CPU faced damage due voltage spikes. This failure resulted in the server becoming unresponsive and unable to serve requests.

# Corrective and preventive measures
<p align="center">
  <img width="460" height="300" src="">
</p>


To prevent similar issues from occurring in the future, the IT team will be implementing the following remediations:

* The team will be implementing additional monitoring and alerting systems to detect hardware failures more quickly.

* The team will be reviewing and updating the server's disaster recovery plan to ensure that services can be restored more quickly in the event of a failure.

* The team will be conducting regular hardware inspections and replacements to prevent future hardware failures.

