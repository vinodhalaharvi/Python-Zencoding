my_zen_settings = {
    'css': {
		'snippets': {
			"def": "{\n\t$0\n}",
		}
    },
	'html': {
		'abbreviations': {
			'jq': '<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>',
			'link:css': '<link rel="stylesheet" type="text/css" href="" media="all" />'
		},
		'snippets': {
			'env': '#!/usr/bin/env python\n',
			'utf8':'#-*- coding:utf-8 -*-\n',
			'get':'def get(self): return self._\n',
			'class':'class ClassName (object):',
			'init':'def __init__(self,):\n\t\tpass',
			'fc':'\n"""\n\t@name:\n\t@description:\n\t@params:\n\t@returns:\n\t@usage:\n\t@text:\n"""', 
			'forrange':'for i in xrange(count):\n\t|',
			'foritems':'for k, v in dct.items():\n\t|',
			'forvalues':'for v in dct.values():\n\t|',
			'forkeys':'for k in dct.keys():\n\t|',
			'fromimport':'from  import |',
			'if':'if |:\n\t|',
			'elif':'elif |:\n\t|',
			'else':'else:\n\t|',
			'def':'\n"""\n\t@name:\n\t@description:\n\t@params:\n\t@returns:\n"""\ndef fname(self, *args, **kwargs):\n\t|',
			'while':'while |:\n\t|',
			'main':"if __name__ == '__main__':\n\t|\nsys.exit(main())",
			'set':'def set(self, newValue): self.| = newValue',
			'try':'try:\n\t |\nexcept Error:\n\t|',
			'dict':"\n{\n\t'|':|,\n}",
			'deco': 'def dname(fn):\n\tdef wrapped():\n\t\treturn "<b>" + fn() + "</b>"\n\treturn wrapped\n@dname\n',

			'dtdd': '<dt>${child}|</dt>\n<dd>|</dd>',
			'cdata': '<![CDATA[\n\t$0\n]]>'
		}
	}
}
