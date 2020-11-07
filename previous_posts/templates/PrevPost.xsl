<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <style>
                    .prev-post-user {
                    width: 100%;
                    background-color: #222222;
                    margin: 50px auto;
                    border-radius: 10px;
                    }

                    #prev-post-css-table {


                    {#border-top-right-radius: 10px;#}{#border-bottom-left-radius: 10px;#} margin: auto;
                    width: 100%;
                    border-spacing: 2px;


                    }

                    #prev-post-css-table tr {
                    color: #303841;
                    text-align: center;
                    background-color: rgba(48, 56, 65, 0.8);


                    }

                    #prev-post-css-table tr:nth-child(even) {
                    background-color: rgba(48, 56, 65, 0.9);
                    }

                    #prev-post-css-table thead th {

                    color: #eeeeee;
                    background-color: #3a4750;
                    text-align: center;
                    text-transform: uppercase;
                    font-weight: bold;
                    font-family: 'Lato', serif;
                    padding: 10px;
                    border-radius: 8px;

                    }

                    #prev-post-css-table td {
                    border-radius: 8px;
                    padding: 10px;
                    font-family: 'Lato', serif;
                    color: #eeeeee;
                    }
                </style>
            </head>
            <body>
                <div class="prev-post-user">
                    <table id="prev-post-css-table">
                        <thead>
                            <th>id</th>
                            <th>title</th>
                            <th>category</th>
                            <th>posted at</th>
                            <th>Section</th>


                        </thead>
                        <xsl:for-each select="prevpost/singlepost">
                            <tr>
                                <td>
                                    <xsl:value-of select="id"/>
                                </td>
                                <td>
                                    <xsl:value-of select="title"/>
                                </td>
                                <td>
                                    <xsl:value-of select="category"/>
                                </td>
                                 <td>
                                    <xsl:value-of select="timeofpost"/>
                                </td>
                                <td>
                                    <xsl:value-of select="section"/>
                                </td>


                            </tr>
                        </xsl:for-each>
                    </table>
                </div>

            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>