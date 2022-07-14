dimensions_fields_mapping = {
    'COSTTYPE': [
        'RECORDNO',
        "PROJECTKEY",
        "PROJECTID",
        "PROJECTNAME",
        "TASKKEY",
        "TASKID",
        "TASKNAME",
        "COSTTYPEID",
        "NAME",
        "STATUS",
        "ACCOUNTKEY",
        "ACCOUNTNO",
        "ITEMKEY",
        "ITEMID",
        "ITEMNAME",
    ],
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
        'TOTALENTERED',
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
    'CUSTOMER': [
        'RECORDNO',
        'CUSTOMERID',
        'NAME',
        'ENTITY',
        'PARENTKEY',
        'PARENTID',
        'PARENTNAME',
        'CUSTREPNAME',
        'TOTALDUE',
        'GLGRPKEY',
        'GLGROUP',
        'STATUS',
        'ONETIME',
        'ONHOLD',
        'WHENCREATED',
        'CREATEDBY',
        'MODIFIEDBY',
        'OBJECTRESTRICTION'
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
    ],
    'TAXDETAIL': [
        'RECORDNO',
        'DETAILID',
        'TAXUID',
        'DESCRIPTION',
        'TAXTYPE',
        'VALUE',
        'MINTAXABLE',
        'MAXTAXABLE',
        'INCLUDE',
        'MINTAX',
        'MAXTAX',
        'GLACCOUNT',
        'TAXAUTHORITY',
        'STATUS',
        'REVERSECHARGE',
        'TAXRATE',
        'TAXSOLUTIONID',
        'MEGAENTITYKEY',
        'MEGAENTITYID',
        'MEGAENTITYNAME'
    ],
    'ARINVOICE': [
        'RECORDNO',
        'RECORDID',
        'STATE',
        'CUSTOMERID',
        'CUSTOMERNAME',
        'CUSTMESSAGEID',
        'CUSTMESSAGE.MESSAGE',
        'DOCNUMBER',
        'DESCRIPTION',
        'DESCRIPTION2',
        'TERMNAME',
        'WHENCREATED',
        'WHENPOSTED',
        'WHENDISCOUNT',
        'WHENDUE',
        'WHENPAID',
        'BASECURR',
        'CURRENCY',
        'EXCH_RATE_DATE',
        'EXCH_RATE_TYPE_ID',
        'EXCHANGE_RATE',
        'TOTALENTERED',
        'TOTALSELECTED',
        'TOTALPAID',
        'TOTALDUE',
        'BILLTOPAYTOCONTACTNAME',
        'SHIPTORETURNTOCONTACTNAME',
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
        'SHIPTO.CONTACTNAME',
        'SHIPTO.PREFIX',
        'SHIPTO.FIRSTNAME',
        'SHIPTO.INITIAL',
        'SHIPTO.LASTNAME',
        'SHIPTO.COMPANYNAME',
        'SHIPTO.PRINTAS',
        'SHIPTO.PHONE1',
        'SHIPTO.PHONE2',
        'SHIPTO.CELLPHONE',
        'SHIPTO.PAGER',
        'SHIPTO.FAX',
        'SHIPTO.EMAIL1',
        'SHIPTO.EMAIL2',
        'SHIPTO.URL1',
        'SHIPTO.URL2',
        'SHIPTO.VISIBLE',
        'SHIPTO.MAILADDRESS.ADDRESS1',
        'SHIPTO.MAILADDRESS.ADDRESS2',
        'SHIPTO.MAILADDRESS.CITY',
        'SHIPTO.MAILADDRESS.STATE',
        'SHIPTO.MAILADDRESS.ZIP',
        'SHIPTO.MAILADDRESS.COUNTRY',
        'SHIPTO.MAILADDRESS.COUNTRYCODE',
        'BILLTO.CONTACTNAME',
        'BILLTO.PREFIX',
        'BILLTO.FIRSTNAME',
        'BILLTO.INITIAL',
        'BILLTO.LASTNAME',
        'BILLTO.COMPANYNAME',
        'BILLTO.PRINTAS',
        'BILLTO.PHONE1',
        'BILLTO.PHONE2',
        'BILLTO.CELLPHONE',
        'BILLTO.PAGER',
        'BILLTO.FAX',
        'BILLTO.EMAIL1',
        'BILLTO.EMAIL2',
        'BILLTO.URL1',
        'BILLTO.URL2',
        'BILLTO.VISIBLE',
        'BILLTO.MAILADDRESS.ADDRESS1',
        'BILLTO.MAILADDRESS.ADDRESS2',
        'BILLTO.MAILADDRESS.CITY',
        'BILLTO.MAILADDRESS.STATE',
        'BILLTO.MAILADDRESS.ZIP',
        'BILLTO.MAILADDRESS.COUNTRY',
        'BILLTO.MAILADDRESS.COUNTRYCODE',
        'PRBATCH',
        'SYSTEMGENERATED',
        'AUWHENCREATED',
        'WHENMODIFIED',
        'DUE_IN_DAYS',
        'SHIPTO.TAXGROUP.NAME',
        'SHIPTO.TAXID',
        'SHIPTO.TAXGROUP.RECORDNO',
        'TAXSOLUTIONID',
        'TAXMETHOD',
        'RETAINAGEPERCENTAGE',
        'TRX_TOTALRETAINED',
        'TRX_TOTALRELEASED',
        'TOTALRETAINED',
        'MEGAENTITYKEY',
        'MEGAENTITYID',
        'MEGAENTITYNAME'
    ],
    'GLDETAIL': [
        'RECORDNO',
        'BATCHKEY',
        'BATCH_DATE',
        'BATCH_TITLE',
        'SYMBOL',
        'BATCH_NO',
        'BOOKID',
        'CHILDENTITY',
        'MODIFIED',
        'REFERENCENO',
        'ADJ',
        'MODULEKEY',
        'OWNERSHIPKEY',
        'LINE_NO',
        'ENTRY_DATE',
        'TR_TYPE',
        'DOCUMENT',
        'ACCOUNTNO',
        'ACCOUNTTITLE',
        'STATISTICAL',
        'DEPARTMENTID',
        'DEPARTMENTTITLE',
        'LOCATIONID',
        'LOCATIONNAME',
        'CURRENCY',
        'BASECURR',
        'DESCRIPTION',
        'DEBITAMOUNT',
        'CREDITAMOUNT',
        'AMOUNT'
    ],
    'CLASS': [
        'RECORDNO',
        'CLASSID',
        'NAME',
        'DESCRIPTION',
        'STATUS',
        'PARENTKEY',
        'PARENTID',
        'WHENCREATED',
        'WHENMODIFIED',
        'CREATEDBY',
        'MODIFIEDBY',
        'MEGAENTITYKEY',
        'MEGAENTITYID',
        'MEGAENTITYNAME',
        'RECORD_URL'
    ],
    'GLBATCH': [
        'JOURNAL',
        'BATCH_DATE',
        'BATCH_TITLE',
        'TAXIMPLICATIONS',
        'VATVENDORID',
        'VATCUSTOMERID',
        'VATCONTACTID',
        'REFERENCENO',
        'BASELOCATION_NO',
        'STATE',
        'TAXSOLUTIONID'
    ],
    'REVRECSCHEDULE': [
        'RECORDNO',
        'REVRECTEMPLATEKEY',
        'REVRECTEMPLATEID',
        'TEMPLATEPOSTINGMETHOD',
        'RECMETHOD',
        'MILESTONESOURCE',
        'PACALCSOURCE',
        'PACALCHOURS',
        'SCHEDULEPERIOD',
        'POSTINGDAY',
        'STATUS',
        'INVOICENO',
        'INVOICEDATE',
        'RECORDKEY',
        'DOCHDRKEY',
        'DOCID',
        'DOCUMENTDATE',
        'DESCRIPTION',
        'PRENTRYKEY',
        'DOCENTRYKEY',
        'REVRECCATKEY',
        'CHANGECATEGORY',
        'CHANGEMEMO',
        'DAYSLASTPERIOD',
        'PROJECTID',
        'PROJECTNAME',
        'TASKNAME',
        'TASKID',
        'WHENCREATED',
        'WHENMODIFIED',
        'CREATEDBY',
        'MODIFIEDBY',
        'MEGAENTITYKEY',
        'MEGAENTITYID',
        'MEGAENTITYNAME'
    ],
    'REVRECSCHEDULEENTRY': [
        'RECORDNO',
        'REVRECSCHEDULEKEY',
        'POSTED',
        'POSITION',
        'NEXT',
        'POSTINGDATE',
        'REVACCTKEY',
        'ACCOUNTNO',
        'ACCOUNTTITLE',
        'JOURNALKEY',
        'GLJOURNAL',
        'DEFERREDREVACCTKEY',
        'AMOUNT',
        'GLBATCHKEY',
        'SCHOPKEY',
        'TR_TYPE',
        'TRX_AMOUNT',
        'CURRENCY',
        'POSTED_AMOUNT',
        'BASECURR',
        'EXCH_RATE_DATE',
        'EXCH_RATE_TYPE_ID',
        'EXCHANGE_RATE',
        'DESCRIPTION',
        'PARENTSTATUS',
        'UNSCHEDULED',
        'BUDGETQTY',
        'ESTQTY',
        'PLANNEDQTY',
        'ACTUALQTY',
        'PERCENTCOMPLETED',
        'PERCENTRECOGNIZED',
        'OBSPERCENTCOMPLETE',
        'BUDGETEDCOST',
        'TOTALCOST',
        'WHENCREATED',
        'WHENMODIFIED',
        'CREATEDBY',
        'MODIFIEDBY',
        'CUSTOMERDIMKEY',
        'CUSTOMERID',
        'CUSTOMERNAME',
        'ITEMDIMKEY',
        'ITEMID',
        'ITEMNAME',
        'VENDORDIMKEY',
        'VENDORID',
        'VENDORNAME',
        'EMPLOYEEDIMKEY',
        'EMPLOYEEID',
        'EMPLOYEENAME',
        'CLASSDIMKEY',
        'CLASSID',
        'CLASSNAME',
        'PROJECTDIMKEY',
        'PROJECTID',
        'PROJECTNAME',
        'TASKDIMKEY',
        'TASKID',
        'TASKNAME'
    ]
}
