#node.js, mongoDB 서버쪽 
#handlebars - 클라이언트쪽
#array incluing (list, tuple)/ dict is very similar to Map(Hashmap-nonblock의개념 Hashtable-block의 개념)/ set(set)
#해쉬코드는 메모리 주소와 밀접한 관련이 있다.

# { A : {'a':'A1', 'b':'A2', 'c':'A3'}}, {B : {'a':'B1', 'b':'B2', 'c':'B3'}}

from bs4 import BeautifulSoup

html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
</table>
'''

companies = {}
tempDic = {}

soup = BeautifulSoup(html, 'html.parser')
data=soup.select('table tr th')
# data1=soup.select_one('tr td').text
print(data)

# for tr in data:
#     company = tr.select_one('td')
#     print(company)
    # contents = tr.select_one('tr td')
    
    # k_company = tr.select_one('tr:nth-of-type(1) th:nth-of-type(1)').text
    # company1 = tr.select_one('tr:nth-of-type(1) th:nth-of-type(2)').text
    # company2 = tr.select_one('tr:nth-of-type(1) th:nth-of-type(3)').text
    # company3 = tr.select_one('tr:nth-of-type(1) th:nth-of-type(4)').text
    # print(company1)

    # k_address = tr.select_one('tr:nth-of-type(2) th').text
    # k_employee = tr.select_one('tr:nth-of-type(3) th').text
    # k_tel = tr.select_one('tr:nth-of-type(4) th').text
    # k_email = tr.select_one('tr:nth-of-type(5) th').text
    
    # address = tr.select_one('td').text
    # employee = tr.select_one('tr:nth-of-type(3) td').text
    # tel = tr.select_one('tr:nth-of-type(4) td').text
    # email = tr.select_one('tr:nth-of-type(5)').text
    # print(contents)
    # print(address)


# for tr in data:
#     companyname = tr.select_one('tr:nth-of-type(1) ').text
#     print(companyname)
#     
# 
# # prac2 = tr.select_one('th:nth-of-type(1)').text

    # prac2 = tr.select_one('td:nth-of-type(0)')
    # prac1 = tr.select_one('td:nth-of-type(1)')
    # address = tr.select_one('td:nth-of-type(2)')
    # employees= i.select_one('tr:nth-of-type(3)').text
    # tel= i.select_one('tr:nth-of-type(4)').text
    # mail = i.select_one('tr:nth-of-type(5)').text
    # print([companyname, address, employees, tel, mail])
    # companies[companyname]={'address':address}
    # print(prac2)   
    
    # companies= {companyname:{"address" : address, "employees" : employees, "tel" : tel, "mail" : mail}}
    # print(companies)
# companies = ['A', 'B', 'C']
# rows = [*'abcdefgh']

# print(rows)

# for c in companies:
#     prac = {c : }
