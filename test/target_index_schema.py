#!/usr/bin/python3

import copy
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / 'schema' / 'TargetIndex.xsd'


class TargetIndexSchemaTests(unittest.TestCase):
    def setUp(self):
        self.index = ET.fromstring('''
            <index schemaVersion="1.0.0">
              <vendor>MyVendor</vendor>
              <url>https://example.com/pack/</url>
              <timestamp>2026-11-09T12:00:00Z</timestamp>
              <devices>
                <device vendor="Device Vendor:123" name="Device.Name+1">
                  <pdsc url="https://example.com/pack/" vendor="MyVendor"
                        name="Device_DFP" version="1.2.3"/>
                </device>
              </devices>
              <boards>
                <board vendor="Board Vendor" name="Board (Demo)" revision="Rev. A">
                  <pdsc url="https://example.com/pack/" vendor="MyVendor"
                        name="Board-BSP" version="2.0.0-beta.1+build.2"/>
                  <mountedDevice vendor="Device Vendor:123" name="Device.Name+1" index="0"/>
                </board>
              </boards>
            </index>
        ''')

    def assert_valid(self, index, valid=True):
        result = subprocess.run(
            ['xmllint', '--noout', '--schema', str(SCHEMA), '-'],
            input=ET.tostring(index, encoding='utf-8'), capture_output=True,
        )
        self.assertEqual(result.returncode, 0 if valid else 3,
                         result.stderr.decode('utf-8', errors='replace'))

    def test_schema_version(self):
        schema = ET.parse(SCHEMA).getroot()
        self.assertEqual(schema.get('version'), '1.0.0')
        self.assertIn('SchemaVersion=1.0.0', SCHEMA.read_text(encoding='utf-8'))
        self.assert_valid(self.index)

    def test_empty_repository(self):
        self.index.find('devices').clear()
        self.index.find('boards').clear()
        self.index.remove(self.index.find('timestamp'))
        self.assert_valid(self.index)

    def test_nil_root(self):
        index = ET.fromstring('''
            <index schemaVersion="1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:nil="true"/>
        ''')
        self.assert_valid(index)
        del index.attrib['schemaVersion']
        self.assert_valid(index, False)
        index.set('schemaVersion', '1.0.0')
        ET.SubElement(index, 'devices')
        self.assert_valid(index, False)

    def test_optional_target_metadata(self):
        board = self.index.find('boards/board')
        del board.attrib['revision']
        board.remove(board.find('mountedDevice'))
        self.assert_valid(self.index)

    def test_multiple_entries(self):
        for path in ('devices/device', 'boards/board', 'boards/board/mountedDevice'):
            parent_path, _ = path.rsplit('/', 1)
            self.index.find(parent_path).append(copy.deepcopy(self.index.find(path)))
        self.assert_valid(self.index)

    def test_required_root_content(self):
        for tag in ('vendor', 'url', 'devices', 'boards'):
            with self.subTest(tag=tag):
                index = copy.deepcopy(self.index)
                index.remove(index.find(tag))
                self.assert_valid(index, False)
        del self.index.attrib['schemaVersion']
        self.assert_valid(self.index, False)

    def test_required_attributes(self):
        for path, attributes in (
            ('devices/device', ('vendor', 'name')),
            ('boards/board', ('vendor', 'name')),
            ('boards/board/mountedDevice', ('vendor', 'name')),
            ('devices/device/pdsc', ('url', 'vendor', 'name', 'version')),
            ('boards/board/pdsc', ('url', 'vendor', 'name', 'version')),
        ):
            for attribute in attributes:
                with self.subTest(path=path, attribute=attribute):
                    index = copy.deepcopy(self.index)
                    del index.find(path).attrib[attribute]
                    self.assert_valid(index, False)

    def test_exactly_one_provider(self):
        for path in ('devices/device', 'boards/board'):
            for count in (0, 2):
                with self.subTest(path=path, count=count):
                    index = copy.deepcopy(self.index)
                    target = index.find(path)
                    provider = target.find('pdsc')
                    if count == 0:
                        target.remove(provider)
                    else:
                        target.insert(0, copy.deepcopy(provider))
                    self.assert_valid(index, False)

    def test_element_order(self):
        for path in ('.', 'boards/board'):
            with self.subTest(path=path):
                index = copy.deepcopy(self.index)
                parent = index.find(path)
                parent[:] = list(reversed(parent))
                self.assert_valid(index, False)

    def test_duplicate_root_elements(self):
        for tag in ('vendor', 'url', 'timestamp', 'devices', 'boards'):
            with self.subTest(tag=tag):
                index = copy.deepcopy(self.index)
                element = index.find(tag)
                index.insert(list(index).index(element), copy.deepcopy(element))
                self.assert_valid(index, False)

    def test_restricted_package_identifiers(self):
        namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
        restriction_path = "xs:simpleType[@name='RestrictedString']/xs:restriction"
        target_restriction = ET.parse(SCHEMA).find(restriction_path, namespaces)
        pack_restriction = ET.parse(ROOT / 'schema' / 'PackIndex.xsd').find(restriction_path, namespaces)
        self.assertEqual(target_restriction.attrib, pack_restriction.attrib)
        self.assertEqual(
            [(facet.tag, facet.attrib) for facet in target_restriction],
            [(facet.tag, facet.attrib) for facet in pack_restriction],
        )
        for path, attribute in (('vendor', None), ('devices/device/pdsc', 'vendor'),
                                ('devices/device/pdsc', 'name'), ('boards/board/pdsc', 'replacement')):
            for value, valid in (('', False), ('My_Vendor-123', True), ('My Vendor', True),
                                 ('My.Vendor', True), (' Vendor', False), ('Vendor ', False),
                                 ('Vendor/Pack', True)):
                with self.subTest(path=path, attribute=attribute, value=value):
                    index = copy.deepcopy(self.index)
                    element = index.find(path)
                    if attribute is None:
                        element.text = value
                    else:
                        element.set(attribute, value)
                    self.assert_valid(index, valid)

    def test_nonempty_target_identifiers(self):
        for path, attributes in (
            ('devices/device', ('vendor', 'name')),
            ('boards/board', ('vendor', 'name', 'revision')),
            ('boards/board/mountedDevice', ('vendor', 'name')),
        ):
            for attribute in attributes:
                for value in ('', ' \t\n '):
                    with self.subTest(path=path, attribute=attribute, value=value):
                        index = copy.deepcopy(self.index)
                        index.find(path).set(attribute, value)
                        self.assert_valid(index, False)

    def test_mounted_device_index(self):
        for value, valid in ((None, True), ('0', True), ('12345678901234567890', True),
                             ('-1', False), ('1.5', False), ('first', False)):
            with self.subTest(value=value):
                index = copy.deepcopy(self.index)
                mounted = index.find('boards/board/mountedDevice')
                if value is None:
                    del mounted.attrib['index']
                else:
                    mounted.set('index', value)
                self.assert_valid(index, valid)

    def test_provider_metadata(self):
        provider = self.index.find('devices/device/pdsc')
        provider.attrib.update(date='2026-11-09', deprecated='2026-12-01',
                               replacement='Next_DFP', size='4294967295')
        self.assert_valid(self.index)
        for attribute, value in (('date', '2026-13-01'), ('deprecated', 'yesterday'),
                                 ('size', '-1'), ('size', '4294967296'), ('size', '1.5')):
            with self.subTest(attribute=attribute, value=value):
                index = copy.deepcopy(self.index)
                index.find('devices/device/pdsc').set(attribute, value)
                self.assert_valid(index, False)

    def test_versions(self):
        for path, attribute in (('.', 'schemaVersion'), ('devices/device/pdsc', 'version')):
            for value, valid in (('1.0.0', True), ('1.2.3-rc.1+build.7', True),
                                 ('1.0', False), ('v1.0.0', False), ('1.0.0-01', False)):
                with self.subTest(path=path, value=value):
                    index = copy.deepcopy(self.index)
                    index.find(path).set(attribute, value)
                    self.assert_valid(index, valid)

    def test_timestamp(self):
        self.index.find('timestamp').text = 'not-a-timestamp'
        self.assert_valid(self.index, False)

    def test_unknown_content(self):
        for path in ('.', 'devices/device', 'boards/board', 'boards/board/mountedDevice'):
            with self.subTest(path=path):
                index = copy.deepcopy(self.index)
                ET.SubElement(index.find(path), 'unknown')
                self.assert_valid(index, False)
                index = copy.deepcopy(self.index)
                index.find(path).set('unknown', 'value')
                self.assert_valid(index, False)

    def test_documented_example(self):
        documentation = (ROOT / 'doxygen' / 'src' / 'pack_publish.txt').read_text(encoding='utf-8')
        section = documentation.split('\\subsection tidxFile ', 1)[1].split('\\subsection ', 1)[0]
        examples = re.findall(r'\\code\{\.xml\}\s*(.*?)\\endcode', section, re.DOTALL)
        self.assertTrue(examples, 'TIDX documentation must contain an XML example')
        for example in examples:
            self.assert_valid(ET.fromstring(example))


if __name__ == '__main__':
    unittest.main()
