import requests
import os.path

class main:

	def __init__(self):
		dev_key = "your_api_key"
		print("*"*30)
		print("*"," "*26,"*")
		print("*"," "*3,"PASTEBIN UPLOADER"," "*4,"*")
		print("*"," "*26,"*")
		print("*"*30)
		try:
			print("Result:",self.proc(dev_key))
		except KeyboardInterrupt:
			print("\nUpload Cancelled!")

	def inp_fileOrText(self, inp_fileOrText):
		if inp_fileOrText == "text" or inp_fileOrText == "2":
			inp = input("Enter your text: ")
		elif inp_fileOrText == "file" or inp_fileOrText == "1":
			file = input("Enter name your file: ")
			if os.path.isfile("./file/"+file) == False:
				inp = False
			else:
				inp = open("./file/"+file, "r").read()
		elif inp_fileOrText == "":
			inp = input("Enter your text: ")
		else:
			return False;
		return inp

	def api_format(self, choose):
		try:
			if choose == "yes" or choose == "1":
				self.dict_view_format()
				inp_api_format = input("Enter your format(Default none)(Enter number!): ")
				res = self.def_dict_format(int(inp_api_format)-1)
			elif choose == "no" or choose == "2":
				res = ""
			elif choose == "":
				res = ""
			else:
				res = False
			return res
		except ValueError:
			return False

	def api_expire_date(self, choose):
		dict_expire = {
		1:"N",
		2:"10M",
		3:"1H",
		4:"1D",
		5:"1W",
		6:"2W",
		7:"1M",
		8:"6M",
		9:"1Y"
		}
		try:
			if choose == "":
				return "N"
				pass
			elif isinstance(int(choose), int):
				return dict_expire[int(choose)]
			else:
				return False
		except ValueError:
			return False

	def proc(self, api_key):
		print("1. File\n2. Text")
		choose_fileOrText = input("Enter text or file(Default 1)(Enter 1 or 2): ")
		enter_code = self.inp_fileOrText(choose_fileOrText)

		# check var enter_code
		if enter_code == False:
			print("Enter the options correctly or Check file!")
			exit()

		choose_formatOrNo = input("Make format yes/no (Default no): ")
		enter_formatOrNo = self.api_format(choose_formatOrNo)

		# checck var enter format or no
		if enter_formatOrNo == False:
			print("Enter the options correctly!")
			exit()

		self.view_expire_date()
		choose_expire_date = input("How long does it expire? (Default No)(Enter number!): ")
		enter_expire_date = self.api_expire_date(choose_expire_date)

		# check expire date
		if enter_expire_date == False:
			print("Enter the options correctly")
			exit()

		req = requests.post("https://pastebin.com/api/api_post.php",data={"api_dev_key":api_key, "api_paste_expire_date":enter_expire_date, "api_paste_code":enter_code, "api_option":"paste", "api_paste_format":enter_formatOrNo})
		return req.text

	def view_expire_date(self):
		print("\n1. Never\n2. 10 Minutes\n3. 1 Hour\n4. 1 Day\n5. 1 Week\n6. 2 Weeks\n7. 1 Month\n8. 6 Months\n9. 1 Year")

	def dict_view_format(self):
		print("""\n1. 4CS\n2. 6502 ACME Cross Assembler\n3. 6502 Kick Assembler\n4. 6502 TASM/64TASS\n5. ABAP\n6. ActionScript\n7. ActionScript 3\n8. Ada\n9. AIMMS\n10. ALGOL 68\n11. Apache Log\n12. AppleScript\n13. APT Sources\n14. Arduino\n15. ARM\n16. ASM (NASM)\n17. ASP\n18. Asymptote\n19. Autoconf\n20. AutoHotkey\n21. AutoIt\n22. Avisynth\n23. Awk\n24. BASCOM AVR\n25. Bash\n26. Basic4GL\n27. DOS Batch\n28. BibTeX\n29. Blitz3D\n30. Blitz Basic\n31. BlitzMax\n32. BNF\n33. BOO\n34. BrainFuck\n35. C\n36. C#\n37. C (WinAPI)\n38. C++\n39. C++ (WinAPI)\n40. C++ (with Qt extensions)\n41. C: Loadrunner\n42. CAD DCL\n43. CAD Lisp\n44. Ceylon\n45. CFDG\n46. C for Macs\n47. ChaiScript\n48. Chapel\n49. C Intermediate Language (CIL)\n50. Clojure\n51. Clone C\n52. Clone C++\n53. CMake\n54. COBOL\n55. CoffeeScript\n56. ColdFusion\n57. CSS\n58. Cuesheet\n59. D\n60. Dart\n61. DCL\n62. DCPU-16\n63. DCS\n64. Delphi\n65. Delphi Prism (Oxygen)\n66. Diff\n67. DIV\n68. DOT\n69. E\n70. Easytrieve\n71. ECMAScript\n72. Eiffel\n73. Email\n74. EPC\n75. Erlang\n76. Euphoria\n77. F#\n78. Falcon\n79. Filemaker\n80. FO Language\n81. Formula One\n82. Fortran\n83. FreeBasic\n84. FreeSWITCH\n85. GAMBAS\n86. Game Maker\n87. GDB\n88. GDScript\n89. Genero\n90. Genie\n91. GetText\n92. Go\n93. Godot GLSL\n94. Groovy\n95. GwBasic\n96. Haskell\n97. Haxe\n98. HicEst\n99. HQ9 Plus\n100. HTML\n101. HTML 5\n102. Icon\n103. IDL\n104. INI file\n105. Inno Script\n106. INTERCAL\n107. IO\n108. ISPF Panel Definition\n109. J\n110. Java\n111. Java 5\n112. JavaScript\n113. JCL\n114. jQuery\n115. JSON\n116. Julia\n117. KiXtart\n118. Kotlin\n119. KSP (Kontakt Script)\n120. LaTeX\n121. LDIF\n122. Liberty BASIC\n123. Linden Scripting\n124. Lisp\n125. LLVM\n126. Loco Basic\n127. Logtalk\n128. LOL Code\n129. Lotus Formulas\n130. Lotus Script\n131. LScript\n132. Lua\n133. M68000 Assembler\n134. MagikSF\n135. Make\n136. MapBasic\n137. Markdown\n138. MatLab\n139. Mercury\n140. MetaPost\n141. mIRC\n142. MIX Assembler\n143. MK-61/52\n144. Modula 2\n145. Modula 3\n146. Motorola 68000 HiSoft Devpac\n147. MPASM\n148. MXML\n149. MySQL\n150. Nagios\n151. NetRexx\n152. newLISP\n153. Nginx\n154. Nim\n155. NullSoft Installer\n156. Oberon 2\n157. Objeck Programming Language\n158. Objective C\n159. OCaml\n160. OCaml Brief\n161. Octave\n162. OpenBSD PACKET FILTER\n163. OpenGL Shading Language\n164. Open Object Rexx\n165. Openoffice BASIC\n166. Oracle 8\n167. Oracle 11\n168. Oz\n169. ParaSail\n170. PARI/GP\n171. Pascal\n172. Pawn\n173. PCRE\n174. Per\n175. Perl\n176. Perl 6\n177. Phix\n178. PHP\n179. PHP Brief\n180. Pic 16\n181. Pike\n182. Pixel Bender\n183. PL/I\n184. PL/SQL\n185. PostgreSQL\n186. PostScript\n187. POV-Ray\n188. PowerBuilder\n189. PowerShell\n190. ProFTPd\n191. Progress\n192. Prolog\n193. Properties\n194. ProvideX\n195. Puppet\n196. PureBasic\n197. PyCon\n198. Python\n199. Python for S60\n200. q/kdb+\n201. QBasic\n202. QML\n203. R\n204. Racket\n205. Rails\n206. RBScript\n207. REBOL\n208. REG\n209. Rexx\n210. Robots\n211. Roff Manpage\n212. RPM Spec\n213. Ruby\n214. Ruby Gnuplot\n215. Rust\n216. SAS\n217. Scala\n218. Scheme\n219. Scilab\n220. SCL\n221. SdlBasic\n222. Smalltalk\n223. Smarty\n224. SPARK\n225. SPARQL\n226. SQF\n227. SQL\n228. SSH Config\n229. StandardML\n230. StoneScript\n231. SuperCollider\n232. Swift\n233. SystemVerilog\n234. T-SQL\n235. TCL\n236. Tera Term\n237. TeXgraph\n238. thinBasic\n239. TypeScript\n240. TypoScript\n241. Unicon\n242. UnrealScript\n243. UPC\n244. Urbi\n245. Vala\n246. VB.NET\n247. VBScript\n248. Vedit\n249. VeriLog\n250. VHDL\n251. VIM\n252. VisualBasic\n253. VisualFoxPro\n254. Visual Pro Log\n255. WhiteSpace\n256. WHOIS\n257. Winbatch\n258. XBasic\n259. XML\n260. Xojo\n261. Xorg Config\n262. XPP\n263. YAML\n264. YARA\n265. Z80 Assembler\n266. ZXBasic""")


	def def_dict_format(self, format):
		dict_format = {
		0: '4cs',
		1: '6502acme',
		2: '6502kickass',
		3: '6502tasm',
		4: 'abap',
		5: 'actionscript',
		6: 'actionscript3',
		7: 'ada',
		8: 'aimms',
		9: 'algol68',
		10: 'apache',
		11: 'applescript',
		12: 'apt_sources',
		13: 'arduino',
		14: 'arm',
		15: 'asm',
		16: 'asp',
		17: 'asymptote',
		18: 'autoconf',
		19: 'autohotkey',
		20: 'autoit',
		21: 'avisynth',
		22: 'awk',
		23: 'bascomavr',
		24: 'bash',
		25: 'basic4gl',
		26: 'dos',
		27: 'bibtex',
		28: 'b3d',
		29: 'blitzbasic',
		30: 'bmx',
		31: 'bnf',
		32: 'boo',
		33: 'bf',
		34: 'c',
		35: 'csharp',
		36: 'c_winapi',
		37: 'cpp',
		38: 'cpp-winapi',
		39: 'cpp-qt',
		40: 'c_loadrunner',
		41: 'caddcl',
		42: 'cadlisp',
		43: 'ceylon',
		44: 'cfdg',
		45: 'c_mac',
		46: 'chaiscript',
		47: 'chapel',
		48: 'cil',
		49: 'clojure',
		50: 'klonec',
		51: 'klonecpp',
		52: 'cmake',
		53: 'cobol',
		54: 'coffeescript',
		55: 'cfm',
		56: 'css',
		57: 'cuesheet',
		58: 'd',
		59: 'dart',
		60: 'dcl',
		61: 'dcpu16',
		62: 'dcs',
		63: 'delphi',
		64: 'oxygene',
		65: 'diff',
		66: 'div',
		67: 'dot',
		68: 'e',
		69: 'ezt',
		70: 'ecmascript',
		71: 'eiffel',
		72: 'email',
		73: 'epc',
		74: 'erlang',
		75: 'euphoria',
		76: 'fsharp',
		77: 'falcon',
		78: 'filemaker',
		79: 'fo',
		80: 'f1',
		81: 'fortran',
		82: 'freebasic',
		83: 'freeswitch',
		84: 'gambas',
		85: 'gml',
		86: 'gdb',
		87: 'gdscript',
		88: 'genero',
		89: 'genie',
		90: 'gettext',
		91: 'go',
		92: 'godot-glsl',
		93: 'groovy',
		94: 'gwbasic',
		95: 'haskell',
		96: 'haxe',
		97: 'hicest',
		98: 'hq9plus',
		99: 'html4strict',
		100: 'html5',
		101: 'icon',
		102: 'idl',
		103: 'ini',
		104: 'inno',
		105: 'intercal',
		106: 'io',
		107: 'ispfpanel',
		108: 'j',
		109: 'java',
		110: 'java5',
		111: 'javascript',
		112: 'jcl',
		113: 'jquery',
		114: 'json',
		115: 'julia',
		116: 'kixtart',
		117: 'kotlin',
		118: 'ksp',
		119: 'latex',
		120: 'ldif',
		121: 'lb',
		122: 'lsl2',
		123: 'lisp',
		124: 'llvm',
		125: 'locobasic',
		126: 'logtalk',
		127: 'lolcode',
		128: 'lotusformulas',
		129: 'lotusscript',
		130: 'lscript',
		131: 'lua',
		132: 'm68k',
		133: 'magiksf',
		134: 'make',
		135: 'mapbasic',
		136: 'markdown',
		137: 'matlab',
		138: 'mercury',
		139: 'metapost',
		140: 'mirc',
		141: 'mmix',
		142: 'mk-61',
		143: 'modula2',
		144: 'modula3',
		145: '68000devpac',
		146: 'mpasm',
		147: 'mxml',
		148: 'mysql',
		149: 'nagios',
		150: 'netrexx',
		151: 'newlisp',
		152: 'nginx',
		153: 'nim',
		154: 'nsis',
		155: 'oberon2',
		156: 'objeck',
		157: 'objc',
		158: 'ocaml',
		159: 'ocaml-brief',
		160: 'octave',
		161: 'pf',
		162: 'glsl',
		163: 'oorexx',
		164: 'oobas',
		165: 'oracle8',
		166: 'oracle11',
		167: 'oz',
		168: 'parasail',
		169: 'parigp',
		170: 'pascal',
		171: 'pawn',
		172: 'pcre',
		173: 'per',
		174: 'perl',
		175: 'perl6',
		176: 'phix',
		177: 'php',
		178: 'php-brief',
		179: 'pic16',
		180: 'pike',
		181: 'pixelbender',
		182: 'pli',
		183: 'plsql',
		184: 'postgresql',
		185: 'postscript',
		186: 'povray',
		187: 'powerbuilder',
		188: 'powershell',
		189: 'proftpd',
		190: 'progress',
		191: 'prolog',
		192: 'properties',
		193: 'providex',
		194: 'puppet',
		195: 'purebasic',
		196: 'pycon',
		197: 'python',
		198: 'pys60',
		199: 'q',
		200: 'qbasic',
		201: 'qml',
		202: 'rsplus',
		203: 'racket',
		204: 'rails',
		205: 'rbs',
		206: 'rebol',
		207: 'reg',
		208: 'rexx',
		209: 'robots',
		210: 'roff',
		211: 'rpmspec',
		212: 'ruby',
		213: 'gnuplot',
		214: 'rust',
		215: 'sas',
		216: 'scala',
		217: 'scheme',
		218: 'scilab',
		219: 'scl',
		220: 'sdlbasic',
		221: 'smalltalk',
		222: 'smarty',
		223: 'spark',
		224: 'sparql',
		225: 'sqf',
		226: 'sql',
		227: 'sshconfig',
		228: 'standardml',
		229: 'stonescript',
		230: 'sclang',
		231: 'swift',
		232: 'systemverilog',
		233: 'tsql',
		234: 'tcl',
		235: 'teraterm',
		236: 'texgraph',
		237: 'thinbasic',
		238: 'typescript',
		239: 'typoscript',
		240: 'unicon',
		241: 'uscript',
		242: 'upc',
		243: 'urbi',
		244: 'vala',
		245: 'vbnet',
		246: 'vbscript',
		247: 'vedit',
		248: 'verilog',
		249: 'vhdl',
		250: 'vim',
		251: 'vb',
		252: 'visualfoxpro',
		253: 'visualprolog',
		254: 'whitespace',
		255: 'whois',
		256: 'winbatch',
		257: 'xbasic',
		258: 'xml',
		259: 'xojo',
		260: 'xorg_conf',
		261: 'xpp',
		262: 'yaml',
		263: 'yara',
		264: 'z80',
		265: 'zxbasic'
		}
		return dict_format[format];

os.system("clear")
main()
