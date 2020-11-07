import xml.etree.ElementTree as gfg


def GenerateXML(fileName):
    root = gfg.Element("PreviousPost")

    m1 = gfg.Element("mobile")
    root.append(m1)

    b1 = gfg.SubElement(m1, "brand")
    b1.text = "Redmi"
    b2 = gfg.SubElement(m1, "price")
    b2.text = "6999"

    m2 = gfg.Element("mobile")
    root.append(m2)

    c1 = gfg.SubElement(m2, "brand")
    c1.text = "Samsung"
    c2 = gfg.SubElement(m2, "price")
    c2.text = "9999"

    m3 = gfg.Element("mobile")
    root.append(m3)

    d1 = gfg.SubElement(m3, "brand")
    d1.text = "RealMe"
    d2 = gfg.SubElement(m3, "price")
    d2.text = "11999"

    tree = gfg.ElementTree(root)

    with open(fileName, "wb") as files:
        tree.write(files)

    # Driver Code


if __name__ == "__main__":
    GenerateXML("templates/PrevPost.xml")