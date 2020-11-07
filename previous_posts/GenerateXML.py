import os

from django.db import connection


def GenerateXML(email_id):
    with connection.cursor() as cursor:
        cursor.execute('CALL news_database.get_the_previous_posts_of_user(%s)', [email_id])
        rows = cursor.fetchall()
        email_id = email_id.replace("@", "_")
        email_id = email_id.replace(".", "_")
        list_of_prev_posts = []
        if os.path.exists(f"./templates/XMLFILES/{email_id}PrevPost.xml"):
            os.remove(f"./templates/XMLFILES/{email_id}PrevPost.xml")
        else:
            print("The file does not exist")
        with open(f"./templates/XMLFILES/{email_id}PrevPost.xml", "a") as files:
            files.write(
                """<?xml version="1.0" encoding="ISO-8859-1"?>\n
<?xml-stylesheet type="text/xml" href="#stylesheet"?>\n
<!DOCTYPE catelog [\n
        <!ATTLIST xsl:stylesheet\n
                id    ID  #REQUIRED>\n
        ]>\n
<prevpost>\n
    <xsl:stylesheet id="stylesheet" version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\n
        <xsl:template match="/">\n
            <html>\n
                <head>\n
                    <style>\n
                        html,body{\n
                        background-color: #303841;\n
                        font-family:serif;\n
                        }\n
                        .prev-post-user {\n
                        width: 100%;\n
                        background-color: #222222;\n
                        margin: 50px auto;\n
                        border-radius: 10px;\n
                        }\n

                        #prev-post-css-table {\n

                        margin: auto;\n
                        width: 100%;\n
                        border-spacing: 2px;\n


                        }\n

                        #prev-post-css-table tr {\n
                        color: #303841;\n
                        text-align: center;\n
                        background-color: rgba(48, 56, 65, 0.8);\n


                        }\n

                        #prev-post-css-table tr:nth-child(even) {\n
                        background-color: rgba(48, 56, 65, 0.9);\n
                        }\n

                        #prev-post-css-table thead th {\n

                        color: #eeeeee;\n
                        background-color: #3a4750;\n
                        text-align: center;\n
                        text-transform: uppercase;\n
                        font-weight: bold;\n
                        font-family: 'Lato', serif;\n
                        padding: 10px;\n
                        border-radius: 8px;\n

                        }\n

                        #prev-post-css-table td {\n
                        border-radius: 8px;\n
                        padding: 10px;\n
                        font-family: 'Lato', serif;\n
                        color: #eeeeee;\n
                        }\n
                    </style>\n
                </head>\n
                <body>\n
                    <div class="prev-post-user">\n
                                            <h2 style="margin:50px 40%;color:#eeeeee;">User's Previous Post's</h2>\n

                        <table id="prev-post-css-table">\n
                            <thead>\n
                                <th>id</th>\n
                                <th>title</th>\n
                                <th>category</th>\n
                                <th>posted at</th>\n
                                <th>Section</th>\n


                            </thead>\n
                            <xsl:for-each select="prevpost/singlepost">\n
                                <tr>\n
                                    <td>\n
                                        <xsl:value-of select="id"/>\n
                                    </td>\n
                                    <td>\n
                                        <xsl:value-of select="title"/>\n
                                    </td>\n
                                    <td>\n
                                        <xsl:value-of select="category"/>\n
                                    </td>\n
                                    <td>\n
                                        <xsl:value-of select="timeofpost"/>\n
                                    </td>\n
                                    <td>\n
                                        <xsl:value-of select="section"/>\n
                                    </td>\n


                                </tr>\n
                            </xsl:for-each>\n
                        </table>\n
                    </div>\n

                </body>\n
            </html>\n
        </xsl:template>\n
    </xsl:stylesheet>\n""")

            for post in rows:
                files.write("<singlepost>\n")
                files.write(f"<id>{post[0]}</id>\n")
                files.write(f"<title>{post[1]}</title>\n")
                files.write(f"<category>{post[2].split('-')[0]}</category>\n")
                files.write(f"<timeofpost>{post[3]}</timeofpost>\n")
                files.write(f"<section>{post[4]}</section>\n")
                files.write("</singlepost>\n")

                prev_posts = {
                    'actual_category': post[2],
                    'category': post[2].split('-')[0],
                    'title': post[1],
                    'news_unique_id': post[0],
                    'time_of_post': post[3],
                    'section': post[4]
                }
                list_of_prev_posts.append(prev_posts)
            files.write("</prevpost>")
            print("File Written")
