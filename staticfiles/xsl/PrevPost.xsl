<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <table border="1">
            <tr bgcolor="#eeeeee">
                <th style="text-align:left">Category</th>
                <th style="text-align:left">Title</th>
            </tr>
            <xsl:for-each select="previouspost/singlepost">
                <tr>
                    <td>
                        <xsl:value-of select="category"/>
                    </td>
                    <td>
                        <xsl:value-of select="title"/>
                    </td>
                </tr>
            </xsl:for-each>
        </table>
    </xsl:template>
</xsl:stylesheet>