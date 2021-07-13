import screenshot as sc
import upload as up
import argparse as ag

from typing import Tuple

def getParameter() -> Tuple[str, str, str, str]:
    parser = ag.ArgumentParser(description='Automatically open browser with selenium')
    parser.add_argument('--username', type=str, default='root')
    parser.add_argument('--password', type=str, required=True)
    parser.add_argument('--nodename', type=str, required=True)
    parser.add_argument('--ticket', type=str, required=True)
    args = parser.parse_args()
    username = args.username
    password = args.password
    ticket = args.ticket
    url = f'https://m-{args.nodename}.ipmi.ihme.washington.edu'

    return username, password, url, ticket

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Taking screenshot
    print("Taking screenshot")
    username, password, url, ticket = getParameter()
    sel:sc.Selenium = sc.connect(url, username, password)
    sc.screenshot(sel) # save screenshot to /mnt/screenshot/png

    # Uploading screenshot to the host
    print("uploading screenshot")
    f = open('/mnt/screenshot.png', 'rb')
    attachment_list = []
    attachment_list.append(f)
    servicedesk = up.ServicedeskApi()
    servicedesk.upload_attachments(ticket, attachment_list)

