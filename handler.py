import xml.etree.ElementTree as ET
import json
import requests


def format_babelway_request(soap_body):
    return "<?xml version='1.0'?>" + \
           '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">' + \
           '  <soap:Body>' + \
           '    <ns2:postMessage xmlns:ns2="http://xmlns.babelway.com/2007/soapgatewayin">' + \
           '      <message>' + \
           '        <xmlPayload>' + \
           f"         {soap_body}" + \
           '        </xmlPayload>' + \
           '      </message>' + \
           '    </ns2:postMessage>' + \
           '  </soap:Body>' + \
           '</soap:Envelope>'


def basic_auth_wsdl_forwarder(event, context):
    body = event['body']
    auth = event['headers']['Authorization']
    root = ET.fromstring(body)
    soap_body = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')

    if soap_body:
        babelway_req_content = format_babelway_request(ET.tostring(soap_body, encoding='unicode', method='xml'))
        with requests.Session() as s:
            headers = {'Content-Type': 'application/xml', 'Authorization': auth}
            babelway_response = s.post(url="http://xxxx.tradeshift.com/ws/SoapIn", data=babelway_req_content,
                                       headers=headers)
            req_body = babelway_response.text
            return {
                'headers': dict(babelway_response.headers),
                'statusCode': babelway_response.status_code,
                'body': req_body
            }
    else:
        return {
            'statusCode': 400,
            'body': ''
        }


body = "<SOAP:Envelope xmlns:SOAP='http://schemas.xmlsoap.org/soap/envelope/'>" \
       "  <SOAP:Body>" \
       "    <SOAP:Fault>" \
       "      <faultcode>SOAP:Server</faultcode>" \
       "      <faultstring>Server Error</faultstring>" \
       "      <detail>" \
       "        <s:SystemError xmlns:s='http://sap.com/xi/WebService/xi2.0'>" \
       "          <context>XIAdapter</context>" \
       "          <code>ADAPTER.JAVA_EXCEPTION</code>" \
       "          <text>some content</text>" \
       "        </s:SystemError>" \
       "      </detail>" \
       "    </SOAP:Fault>" \
       "  </SOAP:Body>" \
       "</SOAP:Envelope>"

auth = "Basic dHJhZGVzaGlmdDp0cmFkZXNoaWZ0"

event = {'body': body, 'headers': {'Authorization': auth}}

response = basic_auth_wsdl_forwarder(event, None)

print(response)
