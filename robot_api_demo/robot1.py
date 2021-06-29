from robot.api import TestSuite

suite = TestSuite('Activate Skynet')
suite.resource.imports.library('OperatingSystem')
test = suite.tests.create('Should Activate Skynet', tags=['smoke'])
test.keywords.create('Set Environment Variable', args=['SKYNET', 'activated'])
test.keywords.create('Environment Variable Should Be Set', args=['SKYNET'])
print(test)
print(test.keywords)
print(suite.resource.imports.visit)
for i in suite.resource.imports:print(i)
# suite.run()
