# змінний неупорядкований набір неповторюючихся об'єктів

# НЕзмінні :
"""
1. Int
2. Float
3. Boolean
4. Tuple
5. String
при можливих змінах створюється НОВИЙ об'єкт!
"""
# a = (1, 2, 3)
# b = a
# print('a=', a, id(a))
# print('b=', b, id(b))
# b += (5,)
# print('a=', a, id(a))
# print('b=', b, id(b))

#############################################

# Змінні :
"""
1. List
2. Set
a = b створюється ПСЕВДОНИМ того же самого об'єкта!
"""

# a = [1, 2, 3]
# b = a
# print('a=', a, id(a))
# print('b=', b, id(b))
# b += [5]
# # b.add(5)
# print('a=', a, id(a))
# print('b=', b, id(b))

#################################################

# SET - змінний неупорядкований набір неповторюючихся об'єктів
# a = {8, 11, 3, 3, 5, 'abc', True, False, 'ABC', 4, 2, 11, 11, 11, 11, 3}
# b = {8, 11, 3, 3, 5, 'abc', True, False, 'ABC', 4, 2, 5, 5, 5, 5, 5, 5, 5, 3}
# c = {8, 11, 3, 5, 'abc', True, False, 'ABC', 4, 2, 11, 3}
# # print(c[0])
# print("len(a) =", len(a))
# print("len(b) =", len(b))
# print("len(c) =", len(c))
# print('a =', a, id(a))
# print('b =', b, id(b))
# print('c =', c, id(c))
# print(a == c)
# print(a is c)

##################################
# a = 4
# b = 4**1
# c = 3 + 1
# print('a =', a, id(a))
# print('b =', b, id(b))
# print('c =', c, id(c))

##################################

# a = []
# a = list()
# print(a, type(a))

# a = set()
# a = {}
# print(a, type(a))

# a = {}
# a = dict()
# print(a, type(a))




##############################################

# text = input('text: ')
# # text = 'rsdxredxyrfjh ctrxtrvhjgxtxcghvghdxghcffgxhjgefchjfdxdfhgygyucdghxhgfd'
# print(len(text), text)
#
# print(len(set(text)), set(text))
#
# print('повторів: ', len(text) - len(set(text)))


##############################################


# a = set(range(5))
# print('a =', a, id(a))
# b = a
# a.add(333)
# # b = a + b
# print('a =', a, id(a))
# print('b =', b, id(b))

##########################################




# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {4, 5, 6, 7, 8, 9}
# s3 = set()
# print('s1 =', s1, type(s1), id(s1))
# print('s2 =', s2, type(s2), id(s2))

# .................................
# s3 = s1.union(s2)
# s3 = s1 | s2


# .................................
# s1.update(s2)
# s1 = s1 | s2
# s1 |= s2
# s1 = s1.union(s2)
# print(s1.update(s2))
# print(s1.union(s2))

# .................................
# s3 = s1.intersection(s2)
# s3 = s1 & s2


# .................................
# s1.intersection_update(s2)
# s1 = s1 & s2
# s1 &= s2


# .................................
# s3 = s1.difference(s2)
# s3 = s1 - s2


# .................................
# s1.difference_update(s2)
# s1 = s1 - s2
# s1 -= s2

# .................................
# s3 = s1.symmetric_difference(s2)
# s3 = s1 ^ s2
# s3 = (s1 | s2) - (s1 & s2)


# .................................
# s1.symmetric_difference_update(s2)
# s1 ^= s2


# .................................
# print('.' * 80)
# print('s1=', s1, id(s1))
# print('s2=', s2, id(s2))
# print('s3=', s3, id(s3))

##############################################

# s1 = set(range(5))
#
# s1.add(888)
# s2 = s1.add(888)
# print('s1=', s1, id(s1))
# print('s2=', s2, id(s2), type(s2))

############################################

# s1 = set(range(5))
# s1.add(999)
# s2 = set(range(5))
# print('s1 =', s1)
# print('s2 =', s2)
# print('.' * 80)


# print(s2.issubset(s1))
# print(s2 <= s1)
# #................................
#
# print(s1.issuperset(s2))
# print(s1 >= s2)

#.................................


# print(s1 < s2)
# print(s1 > s2)
# print(len(s1))
# #.................................
#
# print(1 in s2)
# print(44 in s1)
# print(55 in range(22, 56))
#.................................

# ########################################
# print(s1.isdisjoint(s2))
# s3 = s1
# s3 = s1.copy()
# s3 = set(s1)
#
# s3.add('ss')
# print('s1 =', s1, type(s1), id(s1))
# print('s2 =', s2, type(s2), id(s2))
# print('s3 =', s3, type(s3), id(s3))
# s1[0] = 888
# print(s1[0])

# text = 'Hello'
# print(text[0])

#.................................

# s1 = list(s1)
# print(type(s1), s1, s1[-1])
# s1[0] = 888
# print(type(s1), s1)
# s1 = set(s1)
# print(type(s1), s1)
# #.................................
#
#
# s1.add(89)
# s1.remove(22)
# print(type(s1), 's1 =', s1, id(s1))
#
# s1.pop()
# print(type(s1), 's1 =',  s1, id(s1))
# print('s1.pop() =', s1.pop())
# s4 = s1.pop()
# print('s4 =', s4)
# print(type(s1), 's1 =', s1, id(s1))
# s1.add(s4)
# print(type(s1), 's1 =', s1, id(s1))
#
# s1.discard(42)
# s1.remove(42)
# print(type(s1), 's1 =', s1, id(s1))


# s1.clear()
# s1 = set()
# print(type(s1), 's1 =', s1, id(s1))


###########################################
# s1 = set(range(5))
# print('s1=', s1, id(s1))
# s1 = frozenset(s1)

# print(*dir(s1), sep='\n')

# s1.clear()
# s1.pop()
# s1.remove(2)
# s1.add(5555)
# del s1
# print('s1=', s1, id(s1))
# s2 = s1 | frozenset({234, 456})
# s2 = frozenset(s1) | {234, 456}
# print('s1=', s1, id(s1))
# print('s2=', s2, id(s2))
# s2 = set(s2)
# print('s1=', s1, id(s1))
# print('s2=', s2, id(s2))

########################################

# text = 'Hello, world!'
# print(list(text))
# print(tuple(text))
# print(set(text))

##############################################


# text = '''While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.
# Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.
# The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.
# In addition to the standard library, there is a growing collection of several thousand components (from individual programs and modules to packages and entire application development frameworks), available from the Python Package Index.
# '''



# text = """
# What is Python?
# Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming. Python combines remarkable power with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems, and is extensible in C or C++. It is also usable as an extension language for applications that need a programmable interface. Finally, Python is portable: it runs on many Unix variants including Linux and macOS, and on Windows.
#
# To find out more, start with The Python Tutorial. The Beginner’s Guide to Python links to other introductory tutorials and resources for learning Python.
#
# What is the Python Software Foundation?
# The Python Software Foundation is an independent non-profit organization that holds the copyright on Python versions 2.1 and newer. The PSF’s mission is to advance open source technology related to the Python programming language and to publicize the use of Python. The PSF’s home page is at https://www.python.org/psf/.
#
# Donations to the PSF are tax-exempt in the US. If you use Python and find it helpful, please contribute via the PSF donation page.
#
# Are there copyright restrictions on the use of Python?
# You can do anything you want with the source, as long as you leave the copyrights in and display those copyrights in any documentation about Python that you produce. If you honor the copyright rules, it’s OK to use Python for commercial use, to sell copies of Python in source or binary form (modified or unmodified), or to sell products that incorporate Python in some form. We would still like to know about all commercial use of Python, of course.
#
# See the license page to find further explanations and the full text of the PSF License.
#
# The Python logo is trademarked, and in certain cases permission is required to use it. Consult the Trademark Usage Policy for more information.
#
# Why was Python created in the first place?
# Here’s a very brief summary of what started it all, written by Guido van Rossum:
#
# I had extensive experience with implementing an interpreted language in the ABC group at CWI, and from working with this group I had learned a lot about language design. This is the origin of many Python features, including the use of indentation for statement grouping and the inclusion of very-high-level data types (although the details are all different in Python).
#
# I had a number of gripes about the ABC language, but also liked many of its features. It was impossible to extend the ABC language (or its implementation) to remedy my complaints – in fact its lack of extensibility was one of its biggest problems. I had some experience with using Modula-2+ and talked with the designers of Modula-3 and read the Modula-3 report. Modula-3 is the origin of the syntax and semantics used for exceptions, and some other Python features.
#
# I was working in the Amoeba distributed operating system group at CWI. We needed a better way to do system administration than by writing either C programs or Bourne shell scripts, since Amoeba had its own system call interface which wasn’t easily accessible from the Bourne shell. My experience with error handling in Amoeba made me acutely aware of the importance of exceptions as a programming language feature.
#
# It occurred to me that a scripting language with a syntax like ABC but with access to the Amoeba system calls would fill the need. I realized that it would be foolish to write an Amoeba-specific language, so I decided that I needed a language that was generally extensible.
#
# During the 1989 Christmas holidays, I had a lot of time on my hand, so I decided to give it a try. During the next year, while still mostly working on it in my own time, Python was used in the Amoeba project with increasing success, and the feedback from colleagues made me add many early improvements.
#
# In February 1991, after just over a year of development, I decided to post to USENET. The rest is in the Misc/HISTORY file.
#
# What is Python good for?
# Python is a high-level general-purpose programming language that can be applied to many different classes of problems.
#
# The language comes with a large standard library that covers areas such as string processing (regular expressions, Unicode, calculating differences between files), internet protocols (HTTP, FTP, SMTP, XML-RPC, POP, IMAP), software engineering (unit testing, logging, profiling, parsing Python code), and operating system interfaces (system calls, filesystems, TCP/IP sockets). Look at the table of contents for The Python Standard Library to get an idea of what’s available. A wide variety of third-party extensions are also available. Consult the Python Package Index to find packages of interest to you.
#
# How does the Python version numbering scheme work?
# Python versions are numbered “A.B.C” or “A.B”:
#
# A is the major version number – it is only incremented for really major changes in the language.
#
# B is the minor version number – it is incremented for less earth-shattering changes.
#
# C is the micro version number – it is incremented for each bugfix release.
#
# Not all releases are bugfix releases. In the run-up to a new feature release, a series of development releases are made, denoted as alpha, beta, or release candidate. Alphas are early releases in which interfaces aren’t yet finalized; it’s not unexpected to see an interface change between two alpha releases. Betas are more stable, preserving existing interfaces but possibly adding new modules, and release candidates are frozen, making no changes except as needed to fix critical bugs.
#
# Alpha, beta and release candidate versions have an additional suffix:
#
# The suffix for an alpha version is “aN” for some small number N.
#
# The suffix for a beta version is “bN” for some small number N.
#
# The suffix for a release candidate version is “rcN” for some small number N.
#
# In other words, all versions labeled 2.0aN precede the versions labeled 2.0bN, which precede versions labeled 2.0rcN, and those precede 2.0.
#
# You may also find version numbers with a “+” suffix, e.g. “2.2+”. These are unreleased versions, built directly from the CPython development repository. In practice, after a final minor release is made, the version is incremented to the next minor version, which becomes the “a0” version, e.g. “2.4a0”.
#
# See the Developer’s Guide for more information about the development cycle, and PEP 387 to learn more about Python’s backward compatibility policy. See also the documentation for sys.version, sys.hexversion, and sys.version_info.
#
# How do I obtain a copy of the Python source?
# The latest Python source distribution is always available from python.org, at https://www.python.org/downloads/. The latest development sources can be obtained at https://github.com/python/cpython/.
#
# The source distribution is a gzipped tar file containing the complete C source, Sphinx-formatted documentation, Python library modules, example programs, and several useful pieces of freely distributable software. The source will compile and run out of the box on most UNIX platforms.
#
# Consult the Getting Started section of the Python Developer’s Guide for more information on getting the source code and compiling it.
#
# How do I get documentation on Python?
# The standard documentation for the current stable version of Python is available at https://docs.python.org/3/. PDF, plain text, and downloadable HTML versions are also available at https://docs.python.org/3/download.html.
#
# The documentation is written in reStructuredText and processed by the Sphinx documentation tool. The reStructuredText source for the documentation is part of the Python source distribution.
#
# I’ve never programmed before. Is there a Python tutorial?
# There are numerous tutorials and books available. The standard documentation includes The Python Tutorial.
#
# Consult the Beginner’s Guide to find information for beginning Python programmers, including lists of tutorials.
#
# Is there a newsgroup or mailing list devoted to Python?
# There is a newsgroup, comp.lang.python, and a mailing list, python-list. The newsgroup and mailing list are gatewayed into each other – if you can read news it’s unnecessary to subscribe to the mailing list. comp.lang.python is high-traffic, receiving hundreds of postings every day, and Usenet readers are often more able to cope with this volume.
#
# Announcements of new software releases and events can be found in comp.lang.python.announce, a low-traffic moderated list that receives about five postings per day. It’s available as the python-announce mailing list.
#
# More info about other mailing lists and newsgroups can be found at https://www.python.org/community/lists/.
#
# How do I get a beta test version of Python?
# Alpha and beta releases are available from https://www.python.org/downloads/. All releases are announced on the comp.lang.python and comp.lang.python.announce newsgroups and on the Python home page at https://www.python.org/; an RSS feed of news is available.
#
# You can also access the development version of Python through Git. See The Python Developer’s Guide for details.
# """


# text = """
# Trump says Modi told him that India would stop importing Russian oil
# Apparent hackers take over PA systems at 4 North American airports
# Syria’s interim president visits Putin in Moscow for first meeting since fall of Assad regime
# Afghanistan and Pakistan agree ceasefire after trading their deadliest fire in years. Here’s what we know
# Madagascar’s president rose to power off youth discontent and was taken down by it
# Nobel Peace Prize winner in hiding says Trump deserves the honor 1:44
# """


# l1 = text.split()
# print('len(l1) =', len(l1))
# print('l1 =', l1)
# print('.' * 80)
#
# s1 = set(l1)
# print('len(s1) =', len(s1))
# print('s1 =', s1)
# print('.' * 80)
# print(len(l1)-len(s1))
#############################################


########### аналіз тексту ###################

# l1 = text
# print('len(l1) =', len(l1))
# print('l1 =', l1)
# print('.' * 80)
# l2 = []
# for letter in l1:
#     if letter.isalpha() or letter == ' ' or letter == '’' or letter == '-' or letter == '\n':
#         l2.append(letter.lower())
#
# print('len(l2) =', len(l2))
# print('l2 =', l2)
# print('.' * 80)
#
# text = ''.join(l2)
# print('len(text) =', len(text))
# print('text :', text)
# print('.' * 80)
#
# list_text = text.split()
# print('list_text =', list_text)
# print('len(list_text) =', len(list_text))
# print('.' * 80)
#
# print('len(set(list_text))', len(set(list_text)))
#
# list_set_text = list(set(list_text))
# print('list_set_text =', list_set_text)
# print('.' * 80)
#
# result = []
# for word in list_set_text:
#     result.append((word, list_text.count(word)))
# print('result =', result)
# print('.' * 80)
#
# result.sort(key=lambda x: x[1], reverse=True)
# print('result(sort) =', result)
# print('.' * 80)
#
# for word in result:
#     print(*word, sep='\t')
#
#
# el = ['the', 'a', 'an', 'on', 'as', 'at', 'you', 'or', 'of', 'to', 'in', 'that', 'and', 'is', 'for', 'are', 'it', 'by', 'with', 'i']
# limit = 2
# res = []
# for word in result:
#     if not (word[0] in el or int(word[1]) < limit):
#         res.append(word)
# print('-'*80)
# for word in res:
#     print(*word, sep='\t')



################ 1 - True, 0 - False ##################
# l1 = [1.0, 0, 1.0, True, True, False, 1, 1.0, True, 0, False]
#
# d = set(l1)
# print(1==1.0)
# print(1==True)
# print(0==False)
#
# print(len(d))
# print(d)

# for n in range(5):
#     print(n, (n>3) * 5 + (n<3) * 10)

################################################
############ "заморозка-разморозка" ##############
# s1 = set()
# s2 = frozenset()
#
# print(*dir(s1), sep='\n')
# print(*dir(s2), sep='\n')



#
# a = frozenset([2, 3, 4, 5, 6, 6, 6])
# print('a =', type(a), a, id(a))
#
# b = set(a)
# print('b =', type(b), b, id(b))
#
# b.add(99)
# print('b =', type(b), b, id(b))
#
# b.remove(99)
# print('b =', type(b), b, id(b))
#
# c = frozenset(b)
# print('c =', type(c), c, id(c))

print('c is a ->', c is a)
print('c = a ->', c == a)

#######################################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! end !!!!!!!!!!!!!!!!!!!!!!!!!!!












#### ЗАДАЧА - Угадай число-2##################
# num_list = set(str(x) for x in range(1, int(input('n = '))+1))
# while True:
#     beatr = set(input().split())
#     if 'HELP' in beatr:
#         break
#     if len(beatr & num_list) > len(num_list - beatr):
#         print('YES')
#         num_list &= beatr
#     else:
#         print('NO')
#         num_list -= beatr
# num_list = list(map(int, num_list))
# print(' '.join([str(x) for x in sorted(num_list)]))
##################################################

########## задача ПОЛИГЛОТЫ#############
# n = [[] for i in range(int(input('к-во шк = ')))]
# for i in range(len(n)):
#     n[i] = [int(input('к-во яз = '))]
#     for j in range(1, n[i][0]+1):
#         n[i] += [input('яз = ')]
# all_lang = set()
# all_pup = set()
# for i in range(len(n)):
#     all_lang = all_lang | set(n[i][1:])
# for i in range(len(n)):
#     all_pup = all_lang & set(n[i][1:])
# all_pup = list(sorted(all_pup))
# print(len(all_pup), *all_pup, sep='\n')
# # for i in all_pup:
# #     print(i)
# all_lang = list(sorted(all_lang))
# print(len(all_lang), *all_lang, sep='\n')
# # for i in all_lang:
# #     print(i)
################################# ЗАДАЧА ДЗ ####################

# students = [{input('Language = ') for j in range(int(input('Number of languages = ')))} for i in range(int(input('Number of students = ')))]
# everyone, someone = set.intersection(*students), set.union(*students)
# print(len(everyone), *sorted(everyone), sep='\n')
# print(len(someone), *sorted(someone), sep='\n')
########################

################## Задача ЗАБАСТОВКИ ##################
# n, k = map(int, input('number of days = ').split())
# zab = set()
# for i in range(k):
#     a_i, b_i = [int(s) for s in input('a_i b_i = ').split()]
#     while a_i <= n:
#         zab.add(a_i)
#         a_i += b_i
# print(len(zab - set(range(0, n+1, 7)) - set(range(6, n+1, 7))))
# s1 = set(d)
# s2 = set(range(0, n+1, 7))
# s3 = set(range(6, n+1, 7))
# print(set(s1), len(s1))
# print(set(s2), len(s2))
# print(set(s3), len(s3))
# print(set(d), len(d))
# s = s1 - s2 - s3
# print(s, len(s))
