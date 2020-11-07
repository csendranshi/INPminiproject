<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
        <table border="1">
            <tr bgcolor="#eeeeee">
                <th style="text-align:left">Category</th>
                <th style="text-align:left">Title</th>
                <th style="text-align:left">Id</th>

            </tr>
            <xsl:for-each select="prevpost/singlepost">
                <tr>
                    <td>
                        <xsl:value-of select="category"/>
                    </td>
                    <td>
                        <xsl:value-of select="title"/>
                    </td>
                    <td>
                        <xsl:value-of select="id"/>
                    </td>
                </tr>
            </xsl:for-each>
        </table>
          </body>
        </html>
    </xsl:template>
</xsl:stylesheet>