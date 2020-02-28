#pip - The Python Package Installer
#pip is the package installer for Python.
import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))