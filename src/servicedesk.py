import os
import json
import base64
import requests
import logging

# for servicedesk api
class ServicedeskApi:
    def __init__(self):
        self.base_url = os.environ["SERVICEDESK_BASE_URL"]
        self.username = os.environ["ATLASSIAN_USERNAME"]
        self.password = os.environ["ATLASSIAN_PASSWORD"]
        self.b64_username_password = base64.b64encode(
            f"{self.username}:{self.password}".encode("utf-8")
        ).decode()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.b64_username_password}",
        }

    def update_issue(self, issue_key: str, reporter: str, component_list: list):
        data = {
            "update": {
                "reporter": [{"set": {"name": reporter}}],
                "components": [{"set": component_list}],
            }
        }
        url = f"{self.base_url}/rest/api/2/issue/{issue_key}"
        data_encoded = json.dumps(data).encode("utf-8")
        req = requests.put(url, data=data_encoded, headers=self.headers)

    def upload_attachments(self, issue_key: str, attachments: list):
        files = []
        for attachment in attachments:
            attachment_content = attachment
            attachment_name = attachment.name
            attachment_content_type = 'image/png'
            files.append(
                ("file", (attachment_name, attachment_content, attachment_content_type))
            )
        if len(files) > 0:
            headers = {
                "Authorization": self.headers["Authorization"],
                "X-Atlassian-Token": "no-check",
            }
            url = f"{self.base_url}/rest/api/2/issue/{issue_key}/attachments"
            req = requests.post(url, files=files, headers=headers)
            print(req.text)
            # contents = req.json()
            contents = None
        else:
            contents = None
        return contents

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('screenshot.png', 'rb')
    attachment_list = []
    attachment_list.append(f)
    servicedesk = ServicedeskApi()
    servicedesk.upload_attachments('INFR-7357', attachment_list)


