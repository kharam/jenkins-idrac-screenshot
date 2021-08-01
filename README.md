# IDRAC screenshot and upload to servicedesk

I worked on making IDRAC screenshot side project with uploading its screenshot
to Jira Servicedesk. I hope this would help System Administrator, System
Engineer, and Devops to troubleshoot Dell Cluster better

## How it works

1. main.py call, screenshot.py, and screenshot.py use docker with selenium to
   take screenshot. (Selenium)
1. After calling, screenshot.py, it calls servicedesk.py to upload its picture
   to servicedesk. (RESTFUL API)

## How to use

1. Modify Jenkisn file to your environment.

## Issue?

1. Create a thread in issue tracker.
1. You can always make PR to this project, to make this screenshot better.
