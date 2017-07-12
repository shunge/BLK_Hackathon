import re


class TxtParser:
	@staticmethod
	def parseFile(fileName):

		f = open(fileName, 'r')
		text = f.read()

		match = re.search('([A-Z][a-z]+|\.)(?:\s+([A-Z][a-z]+|\.))*(?:\s+[a-z][a-z\-]+){0,2}\s+([A-Z][a-z]+|\.)', text)
		if match is not None:
			print('Name: ' + match.group())

		match = re.search(
			r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])',
			text)
		if match is not None:
			print('Email: ' + match.group())

		match = re.search(
			'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?',
			text)
		if match is not None:
			print('Phone Number: ' + match.group())

		match = re.search('GPA:? ? (\d+\.?\d?)', text)
		if match is not None:
			print('GPA: ' + match.groups()[0])

		match = re.search('Education\s+(.*\n)', text, re.I)
		if match is not None:
			print('Education: ' + match.groups()[0].rstrip())

		match = re.search('Education(\n.*?)+((Bachelor|Masters|Doctorate).*)', text, re.I)
		if match is not None:
			print('Degree: ' + match.groups()[1])