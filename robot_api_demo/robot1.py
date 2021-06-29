from robot.api import TestSuite
from robot.api import ResultWriter

suite = TestSuite('Activate Skynet')
suite.resource.imports.library('OperatingSystem')
test = suite.tests.create('Should Activate Skynet', tags=['smoke'])
test.keywords.create('Set Environment Variable', args=['SKYNET', 'activated'])
test.keywords.create('Environment Variable Should Be Set', args=['SKYNET'])
# suite.run()
suite1 = TestSuite('Activate Skynet11')
suite1.resource.imports.library('OperatingSystem')
test1 = suite1.tests.create('Should Activate Skynet', tags=['smoke'])
test1.keywords.create(assign=["${abc}"],name='Set Variable', args=[ 'abc'])
test1.keywords.create(name='Should Be Equal As Strings', args=["${abc}",'abc'])

result=suite.run(output="out.xml")
result1=suite1.run(output="out1.xml")
ResultWriter("out.xml","out1.xml").write_results(report="result.html",log="log.html")