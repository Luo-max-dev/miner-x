import requests
import xml.etree.ElementTree as ET

class ABNValidator:
    def __init__(self, guid):
        self.guid = guid
        self.url = "https://abr.business.gov.au/abrxmlsearch/AbrXmlSearch.asmx/SearchByABNv201408"

    def check_active_status(self, abn):
        if not self.guid or not abn:
            return False
        params = {
            'searchString': abn, 
            'includeHistoricalDetails': 'N', 
            'authenticationGuid': self.guid
        }
        try:
            r = requests.get(self.url, params=params, timeout=10)
            if r.status_code != 200:
                return False
            root = ET.fromstring(r.text)
            # Handle XML namespace
            ns = {'ns': 'http://abr.business.gov.au/ABRXMLSearch/'}
            status_code = root.find(".//ns:entityStatus/ns:entityStatusCode", ns)
            if status_code is not None:
                return status_code.text == "Active"
            return False
        except Exception as e:
            print(f"ABN Check Error: {e}")
            return False
