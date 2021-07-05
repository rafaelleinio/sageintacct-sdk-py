dimensions_fields_mapping = {
    'GLACCOUNT': [
        'RECORDNO',
        'ACCOUNTNO',
        'TITLE',
        'ACCOUNTTYPE',
        'NORMALBALANCE',
        'CLOSINGTYPE',
        'STATUS',
        'CATEGORY',
        'ALTERNATIVEACCOUNT'
    ],
    'CHECKINGACCOUNT': [
        'BANKACCOUNTID',
        'BANKACCOUNTNO',
        'GLACCOUNTNO',
        'BANKNAME',
        'ROUTINGNO',
        'BRANCHID',
        'BANKACCOUNTTYPE',
        'DEPARTMENTID',
        'LOCATIONID',
        'STATUS',
        'RECORDNO',
        'ACHBANKID',
        'COMPANYNAME'
    ],
    'CONTACT': [
        'RECORDNO',
        'CONTACTNAME',
        'COMPANYNAME',
        'FIRSTNAME',
        'LASTNAME',
        'INITIAL',
        'PRINTAS',
        'TAXABLE',
        'MAILADDRESS.ADDRESS1'
    ],
    'DEPARTMENT': [
        'RECORDNO',
        'DEPARTMENTID',
        'TITLE',
        'PARENTKEY',
        'PARENTID',
        'SUPERVISORNAME',
        'STATUS',
        'CUSTTITLE'
    ],
    'EXPENSEPAYMENTTYPE': [
        'RECORDNO',
        'NAME',
        'DESCRIPTION',
        'NONREIMBURSABLE',
        'OFFSETACCTNO',
        'OFFSETACCTTITLE',
        'STATUS',
        'WHENCREATED',
        'WHENMODIFIED',
        'CREATEDBY',
        'MODIFIEDBY',
        'MEGAENTITYKEY',
        'MEGAENTITYID',
        'MEGAENTITYNAME'
    ],
    'EEXPENSES': [
        'RECORDNO',
        'RECORD_URL',
        'RECORDID',
        'WHENCREATED',
        'WHENPOSTED',
        'TOTALENTERED',
        'STATE',
        'TOTALDUE',
        'DESCRIPTION',
        'CURRENCY',
        'BASECURR',
        'MEMO'
    ],
    'APBILL': [
        'RECORDNO',
        'RECORDID',
        'RECORD_URL',
        'STATE',
        'VENDORID',
        'VENDORNAME',
        'DOCNUMBER',
        'TERMNAME',
        'WHENCREATED',
        'WHENPOSTED',
        "TOTALENTERED",
        'TOTALSELECTED',
        'TOTALPAID',
        'TOTALDUE',
        'WHENDUE',
        'WHENPAID',
        'RECPAYMENTDATE',
        'PAYMENTPRIORITY',
        'DESCRIPTION',
        'ONHOLD',
        'BASECURR',
        'CURRENCY',
        'WHENMODIFIED',
        'DUE_IN_DAYS',
        'PRBATCH',
    ],
    'CCTRANSACTION': [
        'RECORDNO',
        'RECORDID',
        'RECORD_URL',
        'WHENCREATED',
        'DESCRIPTION',
        'BASECURR',
        'CURRENCY',
        'TOTALENTERED',
        'TRX_TOTALENTERED',
        'TOTALPAID',
        'TRX_TOTALPAID',
        'TOTALSELECTED',
        'TRX_TOTALSELECTED',
        'TOTALDUE',
        'TRX_TOTALDUE',
        'WHENPAID',
        'STATE',
        'RAWSTATE',
        'CLEARED',
        'AUWHENCREATED',
        'WHENMODIFIED',
        'INCLUSIVETAX',
        'TAXSOLUTIONID',
        'TAXMETHOD',
        'MEGAENTITYKEY',
        'MEGAENTITYID',
        'MEGAENTITYNAME',
    ],
    'EEACCOUNTLABEL': [
        'RECORDNO',
        'ACCOUNTLABEL',
        'DESCRIPTION',
        'GLACCOUNTNO',
        'GLACCOUNTTITLE',
        'STATUS',
        'ITEMID'
    ],
    'ITEM': [
        'RECORDNO',
        'ITEMID',
        'STATUS',
        'MRR',
        'NAME',
        'EXTENDED_DESCRIPTION',
        'PRODUCTLINEID',
        'GLGROUP',
        'ITEMTYPE'
    ],
    'LOCATION': [
        'RECORDNO',
        'LOCATIONID',
        'NAME',
        'PARENTID',
        'STATUS',
        'CURRENCY'
    ],
    'PROJECT': [
        'RECORDNO',
        'PROJECTID',
        'NAME',
        'DESCRIPTION',
        'CURRENCY',
        'PROJECTCATEGORY',
        'PROJECTSTATUS',
        'PARENTKEY',
        'PARENTID',
        'PARENTNAME',
        'STATUS',
        'CUSTOMERKEY',
        'CUSTOMERID',
        'CUSTOMERNAME',
        'PROJECTTYPE',
        'DEPARTMENTNAME',
        'LOCATIONID',
        'LOCATIONNAME',
        'BUDGETID',
        'MEGAENTITYID',
        'MEGAENTITYNAME'
    ],
    'TASK': [
        'RECORDNO',
        'TASKID',
        'PARENTKEY',
        'PARENTID',
        'NAME',
        'PARENTTASKNAME',
        'PROJECTKEY',
        'PROJECTID',
        'PROJECTNAME',
        'ITEMKEY',
        'ITEMID',
        'ITEMNAME',
        'DESCRIPTION',
        'BILLABLE',
        'TASKNO',
        'TASKSTATUS',
        'CLASSID',
        'CLASSNAME',
        'CLASSKEY',
        'ROOTPARENTKEY',
        'ROOTPARENTID',
        'ROOTPARENTNAME'
    ],
    'VENDOR': [
        'RECORDNO',
        'NAME',
        'VENDORID',
        'PARENTKEY',
        'PARENTID',
        'PARENTNAME',
        'DISPLAYCONTACT.CONTACTNAME',
        'DISPLAYCONTACT.COMPANYNAME',
        'DISPLAYCONTACT.FIRSTNAME',
        'DISPLAYCONTACT.LASTNAME',
        'DISPLAYCONTACT.INITIAL',
        'DISPLAYCONTACT.PRINTAS',
        'DISPLAYCONTACT.PHONE1',
        'DISPLAYCONTACT.PHONE2',
        'DISPLAYCONTACT.EMAIL1',
        'DISPLAYCONTACT.EMAIL2',
        'VENDORACCOUNTNO',
        'VENDTYPE',
        'ACCOUNTLABEL',
        'APACCOUNT',
        'APACCOUNTTITLE',
        'STATUS'
    ],
    'CREDITCARD': [
        'RECORDNO',
        'CARDID',
        'DESCRIPTION',
        'CARDTYPE',
        'EXP_MONTH',
        'EXP_YEAR',
        'COMMCARD',
        'STATUS',
        'VENDORID',
        'DEPT',
        'LOCATION',
        'LIABILITYTYPE',
        'OUTSOURCECARD'
    ],
    'EMPLOYEE': [
        'RECORDNO',
        'EMPLOYEEID',
        'SSN',
        'TITLE',
        'LOCATIONID',
        'DEPARTMENTID',
        'BIRTHDATE',
        'STARTDATE',
        'ENDDATE',
        'STATUS',
        'EMPLOYEETYPE',
        'EMPLOYEETYPE1099TYPE',
        'GENDER',
        'TERMINATIONTYPE',
        'CONTACT.CONTACTNAME',
        'CONTACT.PREFIX',
        'CONTACT.FIRSTNAME',
        'CONTACT.INITIAL',
        'CONTACT.LASTNAME',
        'CONTACT.COMPANYNAME',
        'CONTACT.PRINTAS',
        'CONTACT.PHONE1',
        'CONTACT.PHONE2',
        'CONTACT.CELLPHONE',
        'CONTACT.PAGER',
        'CONTACT.FAX',
        'CONTACT.EMAIL1',
        'CONTACT.EMAIL2',
        'CONTACT.URL1',
        'CONTACT.URL2',
        'CONTACT.MAILADDRESS.ADDRESS1',
        'CONTACT.MAILADDRESS.ADDRESS2',
        'CONTACT.MAILADDRESS.CITY',
        'CONTACT.MAILADDRESS.STATE',
        'CONTACT.MAILADDRESS.ZIP',
        'CONTACT.MAILADDRESS.COUNTRY',
        'CONTACT.MAILADDRESS.COUNTRYCODE',
        'CURRENCY',
        'WHENCREATED',
        'WHENMODIFIED',
        'PAYMETHODKEY',
        'CONTACTKEY',
        'MEGAENTITYKEY',
        'MEGAENTITYID',
        'MEGAENTITYNAME'
    ],
    'LOCATIONENTITY': [
        'RECORDNO',
        'LOCATIONID',
        'NAME',
        'REPORTPRINTAS',
        'SUPERVISORID',
        'FIRSTMONTH',
        'FIRSTMONTHTAX',
        'WEEKSTART',
        'FEDERALID',
        'STARTDATE',
        'ENDDATE',
        'STATUS',
        'HAS_IE_RELATION',
        'CUSTOMERID',
        'CUSTOMERNAME',
        'VENDORID',
        'VENDORNAME',
        'CURRENCY',
        'TAXID',
        'ENABLELEGALCONTACT',
        'LEGALNAME',
        'LEGALADDRESS1',
        'LEGALADDRESS2',
        'LEGALCITY',
        'LEGALSTATE',
        'LEGALZIPCODE',
        'LEGALCOUNTRY',
        'OPCOUNTRY',
        'ADDRESSCOUNTRYDEFAULT',
        'RECORD_URL'
    ]
}
