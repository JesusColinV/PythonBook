from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("C:\\Users\\hp2560p\\Documents\\testxml.xml")
collection = DOMTree.documentElement

# Get all the movies in the collection
products = collection.getElementsByTagName("PRODUCT")

for product in products:
   print ("*****Product*****")
   if product.hasAttribute("ITEM"):
      print ("Title: %s" % product.getAttribute("ITEM"))
