import MySQLdb as sql
import MySQLdb.converters as converters
import os
import traceback

# Title: Induced Tears
# Date: 2015-11-04 12:00:00
# Tags: anime,
# Category: anime
# Slug: tears

def connect():
    cnx = sql.connect(host='127.0.0.1', user='root', passwd='root', db='blog')
    return cnx

def write_post(row):
    try:
        year = row['post_date'].year

        if not os.path.exists('content/%s' % year):
            os.makedirs('content/%s' % year)

        with open('content/%s/%s_%s.md' % (year, row['ID'], row['post_name'].replace('-', '_')), 'wb') as fp:
            fp.write('Title: %s\n' % row['post_title'])
            fp.write('Date: %s\n' % row['post_date'])
            fp.write('Tags: imported\n')
            fp.write('Category: \n')
            fp.write('Slug: %s\n' % row['post_name'].replace('-', '_'))
            fp.write('\n')
            fp.write(row['post_content'])
            fp.write('\n')
    except Exception, e:
        print(e)
        traceback.print_exec()
        exit()

if __name__ == '__main__':
    cnx = connect()

    with cnx:
        cursor = cnx.cursor(sql.cursors.SSDictCursor)

        cursor.execute("""
            select ID, post_date, post_title, post_name, post_content from wp_posts where post_status = 'publish';
        """)

        rows = cursor.fetchmany(size=10)

        while len(rows) > 0:
            for row in rows:
                print(row['post_name'])
                write_post(row)

            rows = cursor.fetchmany(size=10)
