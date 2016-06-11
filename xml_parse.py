from lxml import objectify
import pandas as pd

#source http://timhomelab.blogspot.com/2014/01/how-to-read-xml-file-into-dataframe.html




path = 'GrantsDBExtract20160509.xml'
xml = objectify.parse(open(path))
root = xml.getroot()

name=[]

for tags in root.getchildren()[0].getchildren():
    name.append(tags.tag)

root.getchildren()[0].getchildren()

df = pd.DataFrame(columns=name)

for i in range(0,len(root.getchildren())):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(name, obj))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)

for i in range(0,len(root.getchildren()):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['id', 'name'], [obj[0].text, obj[1].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)

import xml.etree.ElementTree as etree
tree = etree.parse(path)
root = tree.getroot()
root

agency = []
ceiling = []


for child in root:
	answer = child.findall('Agency')
	agency.append(answer[0].text)
	answer2 = child.findall('AwardCeiling')
	ceiling.append(answer2[0].text)
	num_of_awards



    <FundingOppSynopsis>
        <PostDate>01302008</PostDate>
        <UserID>None</UserID>
        <Password>None</Password>
        <FundingInstrumentType>CA</FundingInstrumentType>
        <FundingActivityCategory>AG</FundingActivityCategory>
        <FundingActivityCategory>ED</FundingActivityCategory>
        <FundingActivityCategory>O</FundingActivityCategory>
        <OtherCategoryExplanation>Agricultural Risk Management Education</OtherCategoryExplanation>
        <NumberOfAwards>50</NumberOfAwards>
        <EstimatedFunding>500000</EstimatedFunding>
        <AwardCeiling>10000</AwardCeiling>
        <AwardFloor>0</AwardFloor>
        <AgencyMailingAddress>Contact Information</AgencyMailingAddress>
        <FundingOppTitle>Commodity Partnerships Small Sessions Program</FundingOppTitle>
        <FundingOppNumber>USDA-RMA-RME-2008-03</FundingOppNumber>
        <ApplicationsDueDate>03242008</ApplicationsDueDate>
        <ApplicationsDueDateExplanation>Applications are due 5 p.m. EDT. Applications received after this deadline will not be considered for funding.</ApplicationsDueDateExplanation>
        <ArchiveDate>04232008</ArchiveDate>
        <Location>None</Location>
        <Office>Risk Management Agency</Office>
        <Agency>Department of Agriculture</Agency>
        <FundingOppDescription>The Federal Crop Insurance Corporation (FCIC), operating through the Risk Management Agency (RMA), announces the availability of approximately $500,000 (subject to availability of funds) for Commodity Partnerships for Small Agricultural Risk Management Education Sessions (Commodity Partnerships Small Sessions Program). The purpose of this cooperative partnership agreement program is to deliver training and information in the management of production, marketing, and financial risk to U.S. agricultural producers in small sessions. The program is to give priority to educating producers of crops not insurable with Federal crop insurance, specialty crops, and underserved commodities, including livestock and forage. A maximum of 50 cooperative partnership agreements will be funded, five each in ten designated RMA Regions. The maximum award for any agreement will be $10,000. Recipients of awards must demonstrate nonfinancial benefits from a partnership agreement and must agree to the substantial involvement of RMA in the project. Funding availability for this program may be announced at approximately the same time as funding availability for similar but separate programs. CFDA No. 10.455 (Community Outreach and Assistance Partnerships), CFDA No. 10.456 (Risk Management Research Partnerships),  CFDA No. 10.457 (Commodity Partnerships for Risk Management Education) and CFDA No.10.458 (Crop Insurance Education in Targeted States). Prospective applicants should carefully examine and compare the notices for each program.</FundingOppDescription>
        <CFDANumber>10.459</CFDANumber>
        <EligibilityCategory>25</EligibilityCategory>
        <AdditionalEligibilityInfo>Eligible applicants include State departments of agriculture, universities, non-profit agricultural organizations, and other public or private organizations with the capacity to lead a local program of risk management education for farmers and ranchers in an RMA Region.  Individuals are not eligible applicants.</AdditionalEligibilityInfo>
        <CostSharing>N</CostSharing>
        <ObtainFundingOppText FundingOppURL="http://www.rma.usda.gov/aboutrma/agreements/">To obtain a copy of the full announcement and more information on items in the Application Kit (RFA for Risk Management Education).</ObtainFundingOppText>
        <AgencyContact AgencyEmailDescriptor="Contact Information" AgencyEmailAddress="RMA.Risk-Ed@rma.usda.gov">Lon Burke&lt;br/&gt;Grants &amp; Agreements Specialist&lt;br/&gt;Phone 202-720-5265</AgencyContact>
    </FundingOppSynopsis>