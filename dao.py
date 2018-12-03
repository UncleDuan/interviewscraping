import pymysql

# 持久层

def dao(urls):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='mysql')
    cur = conn.cursor()
    cur.execute("use interview")
    for index in range(len(urls[0])):
        cur.execute("INSERT INTO `interview` (`url`,`title`) VALUES (\"%s\",\"%s\")", (urls[0][index],urls[1][index]))
        cur.connection.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    urls = [["https"], ["title"]]
    dao(urls)
