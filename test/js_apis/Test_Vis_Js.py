import json
from unittest import TestCase

from browser import Browser_Lamdba_Helper
from view_helpers.Vis_Js import Vis_Js
from pbx_gs_python_utils.utils.Assert import Assert
from pbx_gs_python_utils.utils.Dev import Dev


class Test_Vis_Js(TestCase):
    def setUp(self):
        self.headless = False
        self.vis_js   = Vis_Js(self.headless)
        self.browser  = self.vis_js.browser()

    def tearDown(self):
        png_data = self.browser.sync__screenshot_base64()
        Browser_Lamdba_Helper().save_png_data(png_data)


    def test_add_node(self):
        (
            self.vis_js.add_node('1','first node')
                       .add_node('2', '2nd node')
                       .add_edge('1','2')
        )

    def test_add_node__100_nodes(self):
        colors = ['#9999FF','lightred','lightgreen']
        js_codes = []
        js_codes.append(self.vis_js.add_node__js_code('root', 'root_node','box'))

        for i in range(0,100):
            color = colors[i % 3]
            js_codes.append(self.vis_js.add_node__js_code(i,i, color=color))
            js_codes.append(self.vis_js.add_edge__js_code('root', i))

        self.vis_js.exec_js(js_codes)

    #def test_set_nodes

    def test_setup(self):
        Assert(self.browser                        ).is_class   ('API_Browser'                          )
        Assert(self.vis_js.web_root                ).contains   ('serverless-render/src/web_root'       )
        Assert(self.browser.sync__url()            ).is_equal   ('about:blank')
        Dev.print(self.browser.sync__url())
        #Assert(self.browser.sync__url()            ).match_regex('http://localhost:.*/vis-js/empty.html')

    def test_exec_js(self):
        self.vis_js.load_page(True)
        js_code = """
                network.body.data.nodes.add({id:'1',label:'1st node..'})
                network.body.data.nodes.add({id:'12',label:'new node'})
                network.body.data.edges.add({from:'12',to:'1'})
                """
        self.vis_js.exec_js(js_code)

    def test_create_graph(self):
        nodes   = [{'id':'123','label': 'aaaa','x':-20 ,'fixed': {'x': True,'y':True}},
                   {'id':'aaa','label': '123' , 'x':200,'fixed': {'x': True}}]
        edges   = [{'from':'123','to' :'aaa'}]
        options = {}
        self.vis_js.create_graph(nodes, edges, options)


    def test_create_graph___large_graph(self):
        payload = {'params': ['vis_js', '{"nodes": [{"id": "RISK-1610", "label": "RISK-1610"}, {"id": "RISK-1494", "label": "RISK-1494"}, {"id": "RISK-1495", "label": "RISK-1495"}, {"id": "RISK-1496", "label": "RISK-1496"}, {"id": "RISK-1498", "label": "RISK-1498"}, {"id": "RISK-1534", "label": "RISK-1534"}, {"id": "RISK-1592", "label": "RISK-1592"}, {"id": "GSSP-25", "label": "GSSP-25"}, {"id": "GSSP-26", "label": "GSSP-26"}, {"id": "GSSP-27", "label": "GSSP-27"}, {"id": "GSSP-50", "label": "GSSP-50"}, {"id": "GSSP-51", "label": "GSSP-51"}, {"id": "GSSP-52", "label": "GSSP-52"}, {"id": "GSSP-53", "label": "GSSP-53"}, {"id": "GSSP-54", "label": "GSSP-54"}, {"id": "GSSP-56", "label": "GSSP-56"}, {"id": "GSSP-57", "label": "GSSP-57"}, {"id": "GSSP-61", "label": "GSSP-61"}, {"id": "GSSP-63", "label": "GSSP-63"}, {"id": "GSSP-80", "label": "GSSP-80"}, {"id": "GSSP-81", "label": "GSSP-81"}, {"id": "GSSP-82", "label": "GSSP-82"}, {"id": "GSSP-84", "label": "GSSP-84"}, {"id": "GSSP-95", "label": "GSSP-95"}, {"id": "GSSP-141", "label": "GSSP-141"}, {"id": "GSSP-254", "label": "GSSP-254"}, {"id": "GSSP-255", "label": "GSSP-255"}, {"id": "GSSP-256", "label": "GSSP-256"}, {"id": "GSSP-257", "label": "GSSP-257"}, {"id": "GSSP-259", "label": "GSSP-259"}, {"id": "GSSP-263", "label": "GSSP-263"}, {"id": "RISK-1571", "label": "RISK-1571"}, {"id": "RISK-1527", "label": "RISK-1527"}, {"id": "RISK-1529", "label": "RISK-1529"}, {"id": "RISK-1581", "label": "RISK-1581"}, {"id": "RISK-1582", "label": "RISK-1582"}, {"id": "RISK-873", "label": "RISK-873"}, {"id": "RISK-1522", "label": "RISK-1522"}, {"id": "RISK-1523", "label": "RISK-1523"}, {"id": "RISK-1524", "label": "RISK-1524"}, {"id": "RISK-1528", "label": "RISK-1528"}, {"id": "RISK-1525", "label": "RISK-1525"}, {"id": "RISK-1516", "label": "RISK-1516"}, {"id": "RISK-1517", "label": "RISK-1517"}, {"id": "RISK-1518", "label": "RISK-1518"}, {"id": "RISK-1519", "label": "RISK-1519"}, {"id": "RISK-1520", "label": "RISK-1520"}, {"id": "RISK-1513", "label": "RISK-1513"}, {"id": "RISK-1515", "label": "RISK-1515"}, {"id": "RISK-1629", "label": "RISK-1629"}, {"id": "RISK-1526", "label": "RISK-1526"}, {"id": "RISK-1530", "label": "RISK-1530"}, {"id": "RISK-1531", "label": "RISK-1531"}, {"id": "RISK-1532", "label": "RISK-1532"}, {"id": "RISK-1533", "label": "RISK-1533"}, {"id": "RISK-1559", "label": "RISK-1559"}, {"id": "RISK-1593", "label": "RISK-1593"}, {"id": "RISK-1594", "label": "RISK-1594"}, {"id": "RISK-1595", "label": "RISK-1595"}, {"id": "RISK-1596", "label": "RISK-1596"}, {"id": "GSSP-239", "label": "GSSP-239"}, {"id": "GSOKR-915", "label": "GSOKR-915"}, {"id": "RISK-871", "label": "RISK-871"}, {"id": "VULN-563", "label": "VULN-563"}, {"id": "VULN-2230", "label": "VULN-2230"}, {"id": "GSSP-229", "label": "GSSP-229"}, {"id": "GSSP-236", "label": "GSSP-236"}, {"id": "GSSP-237", "label": "GSSP-237"}, {"id": "GSSP-238", "label": "GSSP-238"}, {"id": "GSSP-260", "label": "GSSP-260"}, {"id": "GSSP-265", "label": "GSSP-265"}, {"id": "GSSP-5", "label": "GSSP-5"}, {"id": "GSSP-55", "label": "GSSP-55"}, {"id": "GSSP-226", "label": "GSSP-226"}, {"id": "GSOKR-873", "label": "GSOKR-873"}, {"id": "GSOKR-875", "label": "GSOKR-875"}, {"id": "RISK-888", "label": "RISK-888"}, {"id": "RISK-889", "label": "RISK-889"}, {"id": "RISK-1625", "label": "RISK-1625"}, {"id": "RISK-1573", "label": "RISK-1573"}, {"id": "GSSP-133", "label": "GSSP-133"}, {"id": "GSSP-370", "label": "GSSP-370"}, {"id": "IA-448", "label": "IA-448"}, {"id": "GSSP-130", "label": "GSSP-130"}, {"id": "GSOKR-874", "label": "GSOKR-874"}, {"id": "RISK-1765", "label": "RISK-1765"}, {"id": "RISK-1766", "label": "RISK-1766"}, {"id": "RISK-1767", "label": "RISK-1767"}, {"id": "RISK-1768", "label": "RISK-1768"}, {"id": "RISK-1769", "label": "RISK-1769"}, {"id": "RISK-1770", "label": "RISK-1770"}, {"id": "RISK-1607", "label": "RISK-1607"}, {"id": "RISK-1398", "label": "RISK-1398"}, {"id": "RISK-1771", "label": "RISK-1771"}, {"id": "RISK-1772", "label": "RISK-1772"}, {"id": "RISK-1773", "label": "RISK-1773"}, {"id": "RISK-1774", "label": "RISK-1774"}, {"id": "GSSP-295", "label": "GSSP-295"}, {"id": "GSOKR-679", "label": "GSOKR-679"}, {"id": "GSOKR-681", "label": "GSOKR-681"}, {"id": "GSOKR-682", "label": "GSOKR-682"}, {"id": "GSOKR-909", "label": "GSOKR-909"}, {"id": "VULN-2205", "label": "VULN-2205"}, {"id": "RISK-1783", "label": "RISK-1783"}, {"id": "GSOKR-683", "label": "GSOKR-683"}, {"id": "GSOKR-281", "label": "GSOKR-281"}, {"id": "GSOKR-160", "label": "GSOKR-160"}, {"id": "GSSP-8", "label": "GSSP-8"}, {"id": "GSSP-291", "label": "GSSP-291"}, {"id": "GSSP-293", "label": "GSSP-293"}, {"id": "RISK-1613", "label": "RISK-1613"}, {"id": "RISK-1617", "label": "RISK-1617"}, {"id": "RISK-1775", "label": "RISK-1775"}, {"id": "RISK-1780", "label": "RISK-1780"}, {"id": "GSSP-203", "label": "GSSP-203"}, {"id": "RISK-1777", "label": "RISK-1777"}, {"id": "RISK-1779", "label": "RISK-1779"}, {"id": "RISK-1179", "label": "RISK-1179"}, {"id": "RISK-1776", "label": "RISK-1776"}, {"id": "RISK-1781", "label": "RISK-1781"}, {"id": "RISK-22", "label": "RISK-22"}, {"id": "RISK-1563", "label": "RISK-1563"}, {"id": "RISK-1616", "label": "RISK-1616"}, {"id": "RISK-1615", "label": "RISK-1615"}, {"id": "RISK-152", "label": "RISK-152"}, {"id": "RISK-172", "label": "RISK-172"}, {"id": "RISK-1639", "label": "RISK-1639"}, {"id": "RISK-1246", "label": "RISK-1246"}, {"id": "RISK-1257", "label": "RISK-1257"}, {"id": "GSSP-202", "label": "GSSP-202"}, {"id": "RISK-1587", "label": "RISK-1587"}, {"id": "RISK-1642", "label": "RISK-1642"}, {"id": "RISK-1189", "label": "RISK-1189"}, {"id": "VULN-1388", "label": "VULN-1388"}, {"id": "RISK-1727", "label": "RISK-1727"}, {"id": "RISK-1728", "label": "RISK-1728"}, {"id": "RISK-1729", "label": "RISK-1729"}, {"id": "RISK-1730", "label": "RISK-1730"}, {"id": "RISK-1731", "label": "RISK-1731"}, {"id": "RISK-1732", "label": "RISK-1732"}, {"id": "RISK-1733", "label": "RISK-1733"}, {"id": "RISK-1734", "label": "RISK-1734"}, {"id": "RISK-1735", "label": "RISK-1735"}, {"id": "RISK-1736", "label": "RISK-1736"}, {"id": "RISK-1737", "label": "RISK-1737"}, {"id": "RISK-1738", "label": "RISK-1738"}, {"id": "RISK-1723", "label": "RISK-1723"}, {"id": "RISK-1724", "label": "RISK-1724"}, {"id": "RISK-1725", "label": "RISK-1725"}, {"id": "RISK-1726", "label": "RISK-1726"}, {"id": "RISK-1758", "label": "RISK-1758"}, {"id": "RISK-1722", "label": "RISK-1722"}, {"id": "RISK-1739", "label": "RISK-1739"}, {"id": "RISK-1740", "label": "RISK-1740"}, {"id": "RISK-1741", "label": "RISK-1741"}, {"id": "RISK-1743", "label": "RISK-1743"}, {"id": "RISK-1760", "label": "RISK-1760"}, {"id": "RISK-1742", "label": "RISK-1742"}, {"id": "RISK-1744", "label": "RISK-1744"}, {"id": "RISK-1745", "label": "RISK-1745"}, {"id": "GSOKR-904", "label": "GSOKR-904"}, {"id": "GSSP-252", "label": "GSSP-252"}, {"id": "GSSP-365", "label": "GSSP-365"}, {"id": "GSSP-366", "label": "GSSP-366"}, {"id": "GSOKR-902", "label": "GSOKR-902"}, {"id": "RISK-1761", "label": "RISK-1761"}, {"id": "RISK-1485", "label": "RISK-1485"}, {"id": "GSSP-218", "label": "GSSP-218"}, {"id": "GSOKR-678", "label": "GSOKR-678"}, {"id": "GSOKR-903", "label": "GSOKR-903"}, {"id": "RISK-1601", "label": "RISK-1601"}, {"id": "GSOKR-920", "label": "GSOKR-920"}, {"id": "RISK-532", "label": "RISK-532"}, {"id": "RISK-1785", "label": "RISK-1785"}, {"id": "RISK-1786", "label": "RISK-1786"}, {"id": "RISK-1787", "label": "RISK-1787"}, {"id": "RISK-1577", "label": "RISK-1577"}, {"id": "GSSP-261", "label": "GSSP-261"}, {"id": "GSSP-262", "label": "GSSP-262"}, {"id": "RISK-1609", "label": "RISK-1609"}, {"id": "RISK-1626", "label": "RISK-1626"}, {"id": "RISK-1627", "label": "RISK-1627"}, {"id": "RISK-1628", "label": "RISK-1628"}, {"id": "RISK-1579", "label": "RISK-1579"}, {"id": "GSSP-58", "label": "GSSP-58"}, {"id": "VULN-371", "label": "VULN-371"}, {"id": "RISK-1640", "label": "RISK-1640"}, {"id": "RISK-1608", "label": "RISK-1608"}, {"id": "RISK-1622", "label": "RISK-1622"}, {"id": "VULN-2277", "label": "VULN-2277"}, {"id": "GSSP-6", "label": "GSSP-6"}, {"id": "GSSP-140", "label": "GSSP-140"}, {"id": "RISK-1621", "label": "RISK-1621"}, {"id": "SEC-10387", "label": "SEC-10387"}, {"id": "GSOKR-680", "label": "GSOKR-680"}, {"id": "RISK-1597", "label": "RISK-1597"}, {"id": "RISK-1598", "label": "RISK-1598"}, {"id": "RISK-1619", "label": "RISK-1619"}, {"id": "RISK-1599", "label": "RISK-1599"}], "edges": [{"from": "RISK-1610", "to": "RISK-1494", "label": "is parent of"}, {"from": "RISK-1610", "to": "RISK-1495", "label": "is parent of"}, {"from": "RISK-1610", "to": "RISK-1496", "label": "is parent of"}, {"from": "RISK-1610", "to": "RISK-1498", "label": "is parent of"}, {"from": "RISK-1610", "to": "RISK-1534", "label": "is parent of"}, {"from": "RISK-1610", "to": "RISK-1592", "label": "is parent of"}, {"from": "RISK-1494", "to": "GSSP-25", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-26", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-27", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-50", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-51", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-52", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-53", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-54", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-56", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-57", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-61", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-63", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-80", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-81", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-82", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-84", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-95", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-141", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-254", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-255", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-256", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-257", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-259", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "GSSP-263", "label": "risk reduced by"}, {"from": "RISK-1494", "to": "RISK-1571", "label": "is created by R2"}, {"from": "RISK-1494", "to": "RISK-1527", "label": "is created by R2"}, {"from": "RISK-1494", "to": "RISK-1529", "label": "is created by R2"}, {"from": "RISK-1494", "to": "RISK-1581", "label": "is created by R2"}, {"from": "RISK-1494", "to": "RISK-1582", "label": "is created by R2"}, {"from": "RISK-1494", "to": "RISK-873", "label": "is created by R2"}, {"from": "RISK-1495", "to": "RISK-1522", "label": "is created by R2"}, {"from": "RISK-1495", "to": "RISK-1523", "label": "is created by R2"}, {"from": "RISK-1495", "to": "RISK-1524", "label": "is created by R2"}, {"from": "RISK-1495", "to": "RISK-1528", "label": "is created by R2"}, {"from": "RISK-1495", "to": "RISK-1525", "label": "is created by R2"}, {"from": "RISK-1495", "to": "RISK-1516", "label": "is created by R2"}, {"from": "RISK-1496", "to": "RISK-1517", "label": "is created by R2"}, {"from": "RISK-1496", "to": "RISK-1518", "label": "is created by R2"}, {"from": "RISK-1496", "to": "RISK-1519", "label": "is created by R2"}, {"from": "RISK-1496", "to": "RISK-1520", "label": "is created by R2"}, {"from": "RISK-1498", "to": "RISK-1513", "label": "is created by R2"}, {"from": "RISK-1498", "to": "RISK-1515", "label": "is created by R2"}, {"from": "RISK-1498", "to": "RISK-1629", "label": "is created by R2"}, {"from": "RISK-1534", "to": "RISK-1526", "label": "is created by R2"}, {"from": "RISK-1534", "to": "RISK-1530", "label": "is created by R2"}, {"from": "RISK-1534", "to": "RISK-1531", "label": "is created by R2"}, {"from": "RISK-1534", "to": "RISK-1532", "label": "is created by R2"}, {"from": "RISK-1534", "to": "RISK-1533", "label": "is created by R2"}, {"from": "RISK-1534", "to": "RISK-1559", "label": "is created by R2"}, {"from": "RISK-1592", "to": "RISK-1593", "label": "is created by R2"}, {"from": "RISK-1592", "to": "RISK-1594", "label": "is created by R2"}, {"from": "RISK-1592", "to": "RISK-1595", "label": "is created by R2"}, {"from": "RISK-1592", "to": "RISK-1596", "label": "is created by R2"}, {"from": "RISK-1571", "to": "GSSP-239", "label": "risk reduced by"}, {"from": "RISK-1571", "to": "GSOKR-915", "label": "risk reduced by"}, {"from": "RISK-1571", "to": "RISK-871", "label": "is created by R3"}, {"from": "RISK-1571", "to": "VULN-563", "label": "is created by R3"}, {"from": "RISK-1571", "to": "VULN-2230", "label": "is created by R3"}, {"from": "RISK-1527", "to": "GSSP-229", "label": "risk reduced by"}, {"from": "RISK-1527", "to": "GSSP-236", "label": "risk reduced by"}, {"from": "RISK-1527", "to": "GSSP-237", "label": "risk reduced by"}, {"from": "RISK-1527", "to": "GSSP-238", "label": "risk reduced by"}, {"from": "RISK-1527", "to": "GSSP-260", "label": "risk reduced by"}, {"from": "RISK-1527", "to": "GSSP-265", "label": "risk reduced by"}, {"from": "RISK-1527", "to": "GSOKR-915", "label": "risk reduced by"}, {"from": "RISK-1529", "to": "GSSP-5", "label": "risk reduced by"}, {"from": "RISK-1529", "to": "GSSP-55", "label": "risk reduced by"}, {"from": "RISK-1529", "to": "GSSP-226", "label": "risk reduced by"}, {"from": "RISK-1529", "to": "GSOKR-873", "label": "risk reduced by"}, {"from": "RISK-1529", "to": "GSOKR-875", "label": "risk reduced by"}, {"from": "RISK-1529", "to": "RISK-888", "label": "is created by R3"}, {"from": "RISK-1529", "to": "RISK-889", "label": "is created by R3"}, {"from": "RISK-1529", "to": "RISK-1625", "label": "is created by R3"}, {"from": "RISK-1529", "to": "RISK-1573", "label": "is created by R3"}, {"from": "RISK-1581", "to": "GSSP-5", "label": "risk reduced by"}, {"from": "RISK-1581", "to": "GSOKR-873", "label": "risk reduced by"}, {"from": "RISK-1581", "to": "GSOKR-875", "label": "risk reduced by"}, {"from": "RISK-1582", "to": "GSSP-5", "label": "risk reduced by"}, {"from": "RISK-1582", "to": "GSSP-133", "label": "risk reduced by"}, {"from": "RISK-1582", "to": "GSSP-370", "label": "risk reduced by"}, {"from": "RISK-1582", "to": "GSOKR-873", "label": "risk reduced by"}, {"from": "RISK-1582", "to": "GSOKR-875", "label": "risk reduced by"}, {"from": "RISK-873", "to": "IA-448", "label": "RISK affects"}, {"from": "RISK-873", "to": "GSSP-130", "label": "risk reduced by"}, {"from": "RISK-873", "to": "GSOKR-873", "label": "risk reduced by"}, {"from": "RISK-873", "to": "GSOKR-874", "label": "risk reduced by"}, {"from": "RISK-873", "to": "GSOKR-875", "label": "risk reduced by"}, {"from": "RISK-873", "to": "RISK-1765", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1766", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1767", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1768", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1769", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1770", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1607", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1398", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1771", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1772", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1773", "label": "is created by R3"}, {"from": "RISK-873", "to": "RISK-1774", "label": "is created by R3"}, {"from": "RISK-1522", "to": "GSSP-295", "label": "risk reduced by"}, {"from": "RISK-1522", "to": "GSOKR-679", "label": "risk reduced by"}, {"from": "RISK-1522", "to": "GSOKR-681", "label": "risk reduced by"}, {"from": "RISK-1522", "to": "GSOKR-682", "label": "risk reduced by"}, {"from": "RISK-1522", "to": "GSOKR-909", "label": "risk reduced by"}, {"from": "RISK-1522", "to": "VULN-2205", "label": "is created by R3"}, {"from": "RISK-1522", "to": "RISK-1783", "label": "is created by R3"}, {"from": "RISK-1523", "to": "GSOKR-679", "label": "risk reduced by"}, {"from": "RISK-1523", "to": "GSOKR-681", "label": "risk reduced by"}, {"from": "RISK-1523", "to": "GSOKR-683", "label": "risk reduced by"}, {"from": "RISK-1523", "to": "GSOKR-909", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "GSOKR-281", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "GSOKR-160", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "GSSP-5", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "GSSP-8", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "GSSP-291", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "GSSP-293", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "GSOKR-909", "label": "risk reduced by"}, {"from": "RISK-1524", "to": "RISK-1613", "label": "is created by R3"}, {"from": "RISK-1524", "to": "RISK-1617", "label": "is created by R3"}, {"from": "RISK-1524", "to": "RISK-1775", "label": "is created by R3"}, {"from": "RISK-1524", "to": "RISK-1780", "label": "is created by R3"}, {"from": "RISK-1528", "to": "GSSP-5", "label": "risk reduced by"}, {"from": "RISK-1528", "to": "GSSP-8", "label": "risk reduced by"}, {"from": "RISK-1528", "to": "GSSP-203", "label": "risk reduced by"}, {"from": "RISK-1528", "to": "RISK-1777", "label": "is created by R3"}, {"from": "RISK-1528", "to": "RISK-1779", "label": "is created by R3"}, {"from": "RISK-1528", "to": "RISK-1179", "label": "is created by R3"}, {"from": "RISK-1528", "to": "RISK-1776", "label": "is created by R3"}, {"from": "RISK-1528", "to": "RISK-1781", "label": "is created by R3"}, {"from": "RISK-1525", "to": "GSOKR-909", "label": "risk reduced by"}, {"from": "RISK-1525", "to": "RISK-22", "label": "is created by R4"}, {"from": "RISK-1525", "to": "RISK-1563", "label": "is created by R3"}, {"from": "RISK-1525", "to": "RISK-1616", "label": "is created by R3"}, {"from": "RISK-1525", "to": "RISK-1615", "label": "is created by R3"}, {"from": "RISK-1525", "to": "RISK-152", "label": "is created by R3"}, {"from": "RISK-1525", "to": "RISK-172", "label": "is created by R3"}, {"from": "RISK-1525", "to": "RISK-1639", "label": "is created by R3"}, {"from": "RISK-1525", "to": "RISK-1246", "label": "is created by R3"}, {"from": "RISK-1525", "to": "RISK-1257", "label": "is created by R3"}, {"from": "RISK-1516", "to": "GSSP-202", "label": "risk reduced by"}, {"from": "RISK-1516", "to": "GSOKR-679", "label": "risk reduced by"}, {"from": "RISK-1516", "to": "GSOKR-681", "label": "risk reduced by"}, {"from": "RISK-1516", "to": "GSOKR-682", "label": "risk reduced by"}, {"from": "RISK-1516", "to": "GSOKR-909", "label": "risk reduced by"}, {"from": "RISK-1516", "to": "RISK-1587", "label": "is created by R3"}, {"from": "RISK-1516", "to": "RISK-1642", "label": "is created by R3"}, {"from": "RISK-1516", "to": "RISK-1189", "label": "is created by R3"}, {"from": "RISK-1516", "to": "VULN-1388", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1727", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1728", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1729", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1730", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1731", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1732", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1733", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1734", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1735", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1736", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1737", "label": "is created by R3"}, {"from": "RISK-1517", "to": "RISK-1738", "label": "is created by R3"}, {"from": "RISK-1518", "to": "RISK-1723", "label": "is created by R3"}, {"from": "RISK-1518", "to": "RISK-1724", "label": "is created by R3"}, {"from": "RISK-1518", "to": "RISK-1725", "label": "is created by R3"}, {"from": "RISK-1518", "to": "RISK-1726", "label": "is created by R3"}, {"from": "RISK-1518", "to": "RISK-1758", "label": "is created by R3"}, {"from": "RISK-1518", "to": "RISK-1722", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1739", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1740", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1741", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1743", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1760", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1742", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1744", "label": "is created by R3"}, {"from": "RISK-1519", "to": "RISK-1745", "label": "is created by R3"}, {"from": "RISK-1520", "to": "GSOKR-874", "label": "risk reduced by"}, {"from": "RISK-1520", "to": "GSOKR-904", "label": "risk reduced by"}, {"from": "RISK-1513", "to": "GSSP-252", "label": "risk reduced by"}, {"from": "RISK-1513", "to": "GSSP-365", "label": "risk reduced by"}, {"from": "RISK-1513", "to": "GSSP-366", "label": "risk reduced by"}, {"from": "RISK-1513", "to": "GSOKR-902", "label": "risk reduced by"}, {"from": "RISK-1513", "to": "RISK-1761", "label": "is created by R3"}, {"from": "RISK-1513", "to": "RISK-1485", "label": "is created by R3"}, {"from": "RISK-1515", "to": "GSSP-218", "label": "risk reduced by"}, {"from": "RISK-1515", "to": "GSOKR-678", "label": "risk reduced by"}, {"from": "RISK-1515", "to": "GSOKR-903", "label": "risk reduced by"}, {"from": "RISK-1515", "to": "RISK-1601", "label": "is created by R3"}, {"from": "RISK-1526", "to": "GSOKR-909", "label": "risk reduced by"}, {"from": "RISK-1530", "to": "GSSP-26", "label": "risk reduced by"}, {"from": "RISK-1530", "to": "GSOKR-920", "label": "risk reduced by"}, {"from": "RISK-1530", "to": "RISK-532", "label": "is created by R3"}, {"from": "RISK-1530", "to": "RISK-1785", "label": "is created by R3"}, {"from": "RISK-1530", "to": "RISK-1786", "label": "is created by R3"}, {"from": "RISK-1530", "to": "RISK-1787", "label": "is created by R3"}, {"from": "RISK-1530", "to": "RISK-1577", "label": "is created by R3"}, {"from": "RISK-1531", "to": "GSSP-27", "label": "risk reduced by"}, {"from": "RISK-1531", "to": "GSSP-50", "label": "risk reduced by"}, {"from": "RISK-1531", "to": "GSSP-261", "label": "risk reduced by"}, {"from": "RISK-1531", "to": "GSSP-262", "label": "risk reduced by"}, {"from": "RISK-1531", "to": "RISK-1609", "label": "is created by R3"}, {"from": "RISK-1531", "to": "RISK-1626", "label": "is created by R3"}, {"from": "RISK-1531", "to": "RISK-1627", "label": "is created by R3"}, {"from": "RISK-1531", "to": "RISK-1628", "label": "is created by R3"}, {"from": "RISK-1531", "to": "RISK-1579", "label": "is created by R3"}, {"from": "RISK-1532", "to": "GSSP-27", "label": "risk reduced by"}, {"from": "RISK-1532", "to": "GSSP-50", "label": "risk reduced by"}, {"from": "RISK-1532", "to": "GSSP-58", "label": "risk reduced by"}, {"from": "RISK-1532", "to": "GSOKR-873", "label": "risk reduced by"}, {"from": "RISK-1532", "to": "GSOKR-875", "label": "risk reduced by"}, {"from": "RISK-1532", "to": "VULN-371", "label": "is created by R3"}, {"from": "RISK-1532", "to": "VULN-2230", "label": "is created by R3"}, {"from": "RISK-1532", "to": "RISK-1640", "label": "is created by R3"}, {"from": "RISK-1532", "to": "RISK-1608", "label": "is created by R3"}, {"from": "RISK-1559", "to": "GSOKR-920", "label": "risk reduced by"}, {"from": "RISK-1559", "to": "RISK-1622", "label": "is created by R3"}, {"from": "RISK-1593", "to": "VULN-2277", "label": "risk reduced by"}, {"from": "RISK-1593", "to": "GSSP-6", "label": "risk reduced by"}, {"from": "RISK-1593", "to": "GSSP-26", "label": "risk reduced by"}, {"from": "RISK-1593", "to": "GSSP-58", "label": "risk reduced by"}, {"from": "RISK-1593", "to": "GSSP-140", "label": "risk reduced by"}, {"from": "RISK-1593", "to": "RISK-1617", "label": "is created by R3"}, {"from": "RISK-1593", "to": "RISK-1775", "label": "is created by R3"}, {"from": "RISK-1594", "to": "RISK-1621", "label": "is created by R3"}, {"from": "RISK-1596", "to": "SEC-10387", "label": "risk reduced by"}, {"from": "RISK-1596", "to": "GSSP-5", "label": "risk reduced by"}, {"from": "RISK-1596", "to": "GSSP-140", "label": "risk reduced by"}, {"from": "RISK-1596", "to": "GSOKR-680", "label": "risk reduced by"}, {"from": "RISK-1596", "to": "RISK-1597", "label": "is created by R3"}, {"from": "RISK-1596", "to": "RISK-1598", "label": "is created by R3"}, {"from": "RISK-1596", "to": "RISK-1619", "label": "is created by R3"}, {"from": "RISK-1596", "to": "RISK-1599", "label": "is created by R3"}], "options": {}}']}

        data = json.loads(payload.get('params')[1])
        nodes = data.get('nodes')
        edges = data.get('edges')
        options = data.get('options')
        #Dev.print(options)
        self.vis_js.create_graph(nodes, edges, options)


    def test_get_graph_data(self):
        graph_name = 'graph_MKF'             # small          ( 20 nodes,  27 edges)
        #graph_name = 'graph_YT4'            # large one      (199 nodes, 236 edges)
        #graph_name = 'graph_VZ5'            # very large one (367 nodes, 653 edges)
        result = self.vis_js.get_graph_data(graph_name)
        Dev.pprint("{0} nodes, {1} edges".format(len(result.get('nodes')), len(result.get('edges'))))

    def test_show_jira_graph(self):
        label_key = 'Issue Type'
        label_key = 'Summary'
        graph_name = 'graph_MKF'
        #graph_name = 'graph_YT4'
        #graph_name = 'graph_XKW'
        result = self.vis_js.show_jira_graph(graph_name, label_key=label_key)
        #result = self.vis_js.send_screenshot_to_slack(None, None)
        Dev.print(result)





