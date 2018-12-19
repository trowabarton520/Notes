from simple_salesforce import Salesforce
import requests
import pprint

session = requests.Session()
sf = Salesforce(username='benb@vmware.com.vmw',
                password='!',
                security_token='')
OwnerID = "0053400000ABdnxAAD"
# Get all the users open cases
myCases = sf.query(
    "SELECT ID, CaseNumber from Case where OwnerID = '$ID' AND Status = 'Open'".replace('$ID', OwnerID))
# sf.query("SELECT Id, AccountId, CaseNumber FROM Case WHERE Id = '50034000014HmlW'")

# Call this with MyCases


def update_cases(cases):
    count = 0
    for case in cases['records']:
        payload = "SELECT ID,OwnerID from Case where CaseNumber = 'CASE'".replace('CASE', case['CaseNumber'])
        print(payload)
        reply = sf.query(payload)
        count += 1
        #    pprint.pprint(reply)
    print(count)


def update_vswarm(owner):
    to_update = sf.query(
        "SELECT ID from Case where OwnerID = '$ID' and Status = 'Open' and SWARM__c = ''".replace('$ID', owner))
    pprint.pprint(to_update)
    if to_update:
        for case in to_update['records']:
            sf.Case.update(case['Id'], {'SWARM__c': 'No'})
#       print("Updated $N cases".replace('$N', str(len(to_update['records']))))


#c = sf.query("SELECT ID from Case where OwnerID = '$ID' and CaseNumber = '18833857706'".replace('$ID', OwnerID))
#pprint.pprint(c['records'][0]['Id'])
#x = sf.case.get(c['records'][0]['Id'])


update_vswarm(OwnerID)


def create_comment(case_id, comment):
    sf.CaseComment.create({'ParentId': case_id, 'CommentBody': comment})


def get_comments():
    # Todo place notes in to text to be copied to cases
    case = "case"
    root='https://www.onenote.com/api/v1.0/'

# create_comment('50034000013sup0AAA')

"""
logFile = open('c:\\Temp\\temp2.txt', 'w', encoding="utf-8")
pprint.pprint(x, logFile)
logFile.write(str(x))
logFile.close()"""
